import pygame
import random
import math
from engine import *
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
COLOR_FONDO = (0, 0, 0)
VELOCIDAD_NAVE = 5
class Nave(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.right > ANCHO_PANTALLA:
            self.rect.right = ANCHO_PANTALLA

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > ALTO_PANTALLA:
            self.rect.bottom = ALTO_PANTALLA

        if self.rect.top < 0:
            self.rect.top = 0

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, x, y, vel):
        super().__init__()
        image_load= pygame.image.load("assets/asteroid.png")
        tam=random.randint(50, 100)
        self.image = pygame.transform.scale(image_load,(tam, tam))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = vel

    def update(self, vel, kill_asteroid):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.right > ANCHO_PANTALLA:
            self.vel_x =+ vel

        if self.rect.left < 0:
            self.vel_x = vel

        if self.rect.top > ALTO_PANTALLA:
            self.kill()
        if kill_asteroid:
            self.kill()
class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y, target_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (5, 5), 5)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 10
        # Calcular la dirección en la que debe moverse el proyectil en función de la posición del mouse
        dx = target_pos[0] - self.rect.centerx
        dy = target_pos[1] - self.rect.centery
        dist = math.sqrt(dx ** 2 + dy ** 2)
        self.vel_x = dx / dist * self.speed
        self.vel_y = dy / dist * self.speed

    def update(self,kill_projectile):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.right < 0 or self.rect.left > ANCHO_PANTALLA or self.rect.bottom < 0 or self.rect.top > ALTO_PANTALLA:
            self.kill()
        if kill_projectile:
            self.kill()
class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = random.randint(2, 5)

        self.image.set_at((2, 2), (255, 255, 255))
        self.image.set_at((1, 1), (200, 200, 200))
        self.image.set_at((3, 3), (200, 200, 200))
        self.image.set_at((1, 3), (200, 200, 200))
        self.image.set_at((3, 1), (200, 200, 200))
        
        self.image.set_at((2, 0), (255, 255, 255))
        self.image.set_at((0, 2), (255, 255, 255))
        self.image.set_at((2, 4), (255, 255, 255))
        self.image.set_at((4, 2), (255, 255, 255))
        
        self.light_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.light_rect = self.light_image.get_rect(center=self.rect.center)

        self.time = 0
        self.opacity = 255

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y 

        if self.rect.right > ANCHO_PANTALLA:
            self.vel_x = -4

        if self.rect.left < 0:
            self.vel_x = 4

        if self.rect.top > ALTO_PANTALLA:
            self.kill()

        # Cambiar la opacidad de la luz cada 0.5 segundos
        if self.opacity == 255:
            self.opacity = 200
        else:
            self.opacity = 255

        # Dibujar la luz de la estrella con la opacidad actual
        pygame.draw.circle(self.light_image, (255, 255, 255, self.opacity), (25, 25), 25)
        self.light_rect.center = self.rect.center

    def draw(self, superficie):
        superficie.blit(self.image, self.rect)
        superficie.blit(self.light_image, self.light_rect)
class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, radio, velocidad):
        super().__init__()
        self.image = pygame.Surface((radio*2, radio*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255,0,0,128), (radio, radio), radio)
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = velocidad

    def update(self,kill_bomb):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.right > ANCHO_PANTALLA:
            self.vel_x = +velocidad

        if self.rect.left < 0:
            self.vel_x = velocidad

        if self.rect.top > ALTO_PANTALLA:
            self.kill()
        if kill_bomb:
            self.kill()
            