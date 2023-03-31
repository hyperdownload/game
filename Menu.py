import pygame
import csv

pygame.init()

# Define el tamaño de la ventana
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Crea la ventana
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Define el tamaño de los tiles
TILE_SIZE = 32

# Carga el tilemap desde un archivo CSV
with open("tilemap.csv") as f:
    reader = csv.reader(f)
    tilemap = list(reader)

# Carga las imágenes de los tiles
tiles = {}
default_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
default_image.fill((255, 255, 255))
for i in range(len(tilemap)):
    for j in range(len(tilemap[i])):
        tile = tilemap[i][j]
        if tile not in tiles:
            if tile == "-1":
                image = default_image
            if tile == "-4":
                image = pygame.image.load("tile/4.png").convert_alpha()
            else:
                image = pygame.image.load("tile/"+tile + ".png").convert_alpha()
            tiles[tile] = image

# Calcula el ancho y el alto de cada tile
tile_width, tile_height = tiles[tilemap[0][0]].get_size()

# Calcula el ancho y el alto del tilemap en píxeles
map_width = len(tilemap[0]) * tile_width
map_height = len(tilemap) * tile_height

# Dibuja el tilemap en la pantalla
for i in range(len(tilemap)):
    for j in range(len(tilemap[i])):
        tile = tilemap[i][j]
        image = tiles[tile]
        x = j * tile_width
        y = i * tile_height
        screen.blit(image, (x, y))

# Actualiza la pantalla
pygame.display.flip()

# Espera a que el usuario cierre la ventana
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()