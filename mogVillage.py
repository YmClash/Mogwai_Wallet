import pygame
import random
import time
import pytmx
import pyscroll
from Players import Player

pygame.init()

display_largeur = 800
display_hauteur= 600

display = pygame.display.set_mode((display_largeur, display_hauteur))
pygame.display.set_caption("Mog Village ")

tmx_data = pytmx.util_pygame.load_pygame(r"C:\Users\y_mc\PycharmProjects\Mogwai_Wallet\Map\YmMap.tmx")
map_data = pyscroll.data.TiledMapData(tmx_data)
map_layer = pyscroll.orthographic.BufferedRenderer(map_data, display.get_size())

map_layer.zoom = 2

player =Player()




group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
group.add(player)




running = True

while running:
    group.draw(display)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()







