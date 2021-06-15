import pygame
import sys

pygame.init()

# 1280 x 720 display
WIDTH, HEIGHT = 1280, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wizards")
bg = pygame.image.load("assets/spooky_bg.jpg")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    window.blit(bg, [0, 0])
    pygame.display.update()
