from player import Game
from objets import *
import pygame
import random
import threading
import asyncio
from time import sleep
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
class game_engine():
    dificulty=False
    def collisions(objeto1, objeto2, variable):
        colisiones = pygame.sprite.spritecollide(objeto1, objeto2, variable)
        return colisiones
    def all_collisions(group1, group2):
        for sprite1 in group1:
            for sprite2 in group2:
                if pygame.sprite.collide_rect(sprite1, sprite2):
                    sprite2.update(True)
                    return True
        return False
    def dificulty(points):
        if points>100:
            return True
        else:
            return False
    async def shake_screen(screen, intensity=10, duration=1):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < duration:
            dx = intensity * random.choice((-1, 1))
            dy = intensity * random.choice((-1, 1))
            screen.blit(background, (dx, dy))
            pygame.display.flip()
            await asyncio.sleep(0.01)
        screen.blit(background, (0, 0))
        pygame.display.flip()