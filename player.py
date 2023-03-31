import pygame
import random
class Game():
    def dead(ANCHO_PANTALLA, ALTO_PANTALLA, pantalla, nave, asteroides_grupo, puntuacion, max_value):
        global jugando

        # Dibujar el botón en pantalla
        boton_rect = pygame.draw.rect(pantalla, (255, 0, 0), (ANCHO_PANTALLA // 2 - 50, ALTO_PANTALLA // 2 + 50, 100, 50))
        fuente = pygame.font.Font(None, 30)
        mensaje = fuente.render("Jugar de nuevo", True, (255, 255, 255))
        mensaje_rect = mensaje.get_rect(center=boton_rect.center)
        pantalla.blit(mensaje, mensaje_rect)

        # Mostrar mensaje de game over
        mensaje = fuente.render(f"GAME OVER, puntuacion:{puntuacion},Puntaje maximo:{max_value}", True, (255, 0, 0))
        mensaje_rect = mensaje.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))
        pantalla.blit(mensaje, mensaje_rect)
        pygame.display.flip()

        # Esperar a que se presione el botón
        presionado = False
        while not presionado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando = False
                    presionado = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_rect.collidepoint(event.pos):
                        jugando = True
                        presionado = True
                        break
        # Reiniciar sprites
        nave.rect.center = (ANCHO_PANTALLA // 2, ALTO_PANTALLA - 50)
        nave.vel_x = 0
        nave.vel_y = 0
        asteroides_grupo.empty()
        # Volver a jugar
        print("Jugador murio!")
    def splash_menu(ANCHO_PANTALLA, ALTO_PANTALLA, pantalla):
        # Dibujar el botón en pantalla
        boton_rect = pygame.draw.rect(pantalla, (255, 0, 0), (ANCHO_PANTALLA // 2 - 50, ALTO_PANTALLA // 2 + 50, 100, 50))
        fuente = pygame.font.Font(None, 30)
        mensaje = fuente.render("Jugar", True, (255, 255, 255))
        mensaje_rect = mensaje.get_rect(center=boton_rect.center)
        pantalla.blit(mensaje, mensaje_rect)
        # Esperar a que se presione el botón
        presionado = False
        while not presionado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando = False
                    presionado = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_rect.collidepoint(event.pos):
                        jugando = True
                        presionado = True
                        return True
                        break
                        
        