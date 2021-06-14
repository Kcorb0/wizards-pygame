import pygame
import sys

pygame.init()

# 1280 x 720 display
WIDTH, HEIGHT = 1280, 720

window = pygame.display.set_mode((WIDTH, HEIGHT))


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display
