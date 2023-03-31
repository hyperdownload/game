import pygame
import random
import threading
import asyncio
from player import Game
from engine import * 
from objets import *
# Constantes
asteroid_health=10
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
COLOR_FONDO = (0, 0, 0)
VELOCIDAD_NAVE = 5
asteroid_vel=3
bomb_temp=0
bomb_freq=100
FRECUENCIA_ASTEROIDES = 60
FRECUENCIA_ASTEROIDESX = 50
dificulty_level=1000
bomb_velocity=2
max_punt=[]
# Inicialización
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Esquivar Asteroides")
# Sprites
nave = Nave(ANCHO_PANTALLA/2, ALTO_PANTALLA/2)
nave_grupo = pygame.sprite.Group(nave)
asteroides_grupo = pygame.sprite.Group()
asteroidesx_grupo = pygame.sprite.Group()
star_grupo = pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
projectiles=pygame.sprite.Group()
bombs=pygame.sprite.Group()
# Reloj
reloj = pygame.time.Clock()
# Temporizador para generar asteroides
temporizador = 0
#Fondo
temporizador_star = 0
# Puntuación
puntuacion = 0
# Fuente de texto
fuente = pygame.font.Font(None, 36)
# Bucle del juego
jugando = True
#Debug
debug=False
pausado=False
while jugando:
    if pausado:
            # Si el juego está pausado, solo se detectan eventos de despausa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    # Si se presiona la tecla P, se despausa el juego
                    pausado = False
    else:
        kill_bomb=False
        kill_projectile=False
        kill_asteroid=False
        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            if evento.type == pygame.MOUSEBUTTONUP:
                # Se ha presionado el botón izquierdo del mouse
                # Obtener la posición del mouse en el momento del clic
                mouse_pos = pygame.mouse.get_pos()
                # Crear un nuevo proyectil y agregarlo al grupo de proyectiles
                new_projectile = Proyectil(nave.rect.centerx, nave.rect.centery, mouse_pos)
                projectiles.add(new_projectile)
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    # Si se presiona la tecla P, se pausa el juego
                    pausado = True
        # Lógica
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            nave.vel_x = -VELOCIDAD_NAVE
        elif teclas[pygame.K_RIGHT]:
            nave.vel_x = VELOCIDAD_NAVE
        else:
            nave.vel_x = 0

        if teclas[pygame.K_UP]:
            nave.vel_y = -VELOCIDAD_NAVE
        elif teclas[pygame.K_DOWN]:
            nave.vel_y = VELOCIDAD_NAVE
        else:
            nave.vel_y = 0
        # Generar asteroides
        temporizador+=1
        bomb_temp+=1
        temporizador_star+=1
        if temporizador == FRECUENCIA_ASTEROIDES:
            temporizador = 0
            x = random.randint(0, ANCHO_PANTALLA - 50)
            asteroide = Asteroide(x, 0,asteroid_vel)
            asteroides_grupo.add(asteroide)
        if bomb_temp == bomb_freq:
            bomb_temp = 0
            x = random.randint(0, ANCHO_PANTALLA - 50)
            bomb = Bomb(x, 0,10, bomb_velocity)
            bombs.add(bomb)
            game_engine.dificulty(puntuacion)
        if temporizador_star == 4:
            temporizador_star = 0
            x = random.randint(0, ANCHO_PANTALLA - 50)
            star = Star(x, 0)
            star_grupo.add(star)
        # Dibujar pantalla
        pantalla.fill(COLOR_FONDO)
        nave_grupo.draw(pantalla)
        asteroides_grupo.draw(pantalla)
        star_grupo.draw(pantalla)
        projectiles.draw(pantalla)
        bombs.draw(pantalla)
        # Actualizar sprites
        nave_grupo.update()
        asteroides_grupo.update(asteroid_vel,kill_asteroid)
        star_grupo.update()
        projectiles.update(kill_projectile)
        bombs.update(kill_bomb)
        #Colisones
        if game_engine.collisions(nave, asteroides_grupo, True):
            max_punt.append(puntuacion)
            maximo_puntaje=max(max_punt)
            Game.dead(ANCHO_PANTALLA, ALTO_PANTALLA, pantalla, nave, asteroides_grupo, puntuacion, maximo_puntaje)
            puntuacion = 0
            asteroid_vel = 3
            bomb_velocity=2
            FRECUENCIA_ASTEROIDES = 60
            dificulty_level = 1000
            bomb_frequency = 100
        if game_engine.collisions(nave, bombs, True):
            max_punt.append(puntuacion)
            maximo_puntaje=max(max_punt)
            Game.dead(ANCHO_PANTALLA, ALTO_PANTALLA, pantalla, nave, asteroides_grupo, puntuacion, maximo_puntaje)
            puntuacion = 0
            bomb_velocity=2
            asteroid_vel = 3
            FRECUENCIA_ASTEROIDES = 60
            dificulty_level = 1000
            bomb_frequency = 100
        game_engine.all_collisions(projectiles, bombs)  
        game_engine.all_collisions(asteroides_grupo, projectiles)
        #Dificultad
        if puntuacion == dificulty_level:
                asteroid_vel+=1
                bomb_velocity+=1
                FRECUENCIA_ASTEROIDES-=2
                bomb_freq-=4
                dificulty_level+=1000
                print(f"Velocidad objetos:{asteroid_vel}\n"
                    f"Velocidad bombass:{bomb_velocity}\n"
                    f"Frecuencia:{FRECUENCIA_ASTEROIDES}\n"
                    f"Frecuencia bombas:{bomb_freq}\n"
                    f"Dificultad:{dificulty_level}")
        # Mostrar puntuación
        puntuacion += 1
        texto_puntuacion = fuente.render("Puntuación: " + str(puntuacion), True, (255, 255, 255))
        pantalla.blit(texto_puntuacion, (10, 10))
        # Actualizar pantalla
        pygame.display.flip()
        #Debug mode
        if debug:
            print("Asteroides:",len(asteroidesx_grupo))
            print(temporizador)
        # Esperar al siguiente frame
        reloj.tick(60)