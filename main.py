from pygame import font
from pygame.display import update
from wizards import Pyromancer, Necromancer
import pygame
import sys
import random as rand

pygame.init()
pygame.font.init()

# 1280 x 720 display
WIDTH, HEIGHT = 1280, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wizards")
bg = pygame.image.load("assets/spooky_bg.jpg")
font_casc = pygame.font.SysFont("Cascadia Mono", 50)


def mana_orbs():
    pass


def health_bar(p1_hp, p2_hp):
    if p1_hp < 100:
        bar1_width = 400 * float(f"0.{p1_hp}")
    else:
        bar1_width = 400

    if p2_hp < 100:
        bar2_width = 400 * float(f"0.{p2_hp}")
    else:
        bar2_width = 400

    pygame.draw.rect(window, (33, 33, 33), pygame.Rect(25, 70, 400, 20))
    pygame.draw.rect(window, (33, 33, 33), pygame.Rect(WIDTH - 425, 70, 400, 20))

    pygame.draw.rect(window, (65, 179, 57), pygame.Rect(25, 70, bar1_width, 20))
    pygame.draw.rect(
        window, (65, 179, 57), pygame.Rect(WIDTH - 425, 70, bar2_width, 20)
    )


def spell_board():
    spell_board = pygame.image.load("assets/spell_board.png")
    spell_board_scaled = pygame.transform.scale(
        spell_board,
        [
            int(spell_board.get_width() * 0.7),
            int(spell_board.get_height() * 0.7),
        ],
    )
    window.blit(spell_board_scaled, [25, 575])
    window.blit(spell_board_scaled, [WIDTH - spell_board_scaled.get_width() - 25, 575])


def players(player1, player2):

    scale_multiplier = 0.40

    player1_sprite = pygame.image.load(player1.sprite)
    player1_sprite_scaled = pygame.transform.scale(
        player1_sprite,
        [
            int(player1_sprite.get_width() * scale_multiplier),
            int(player1_sprite.get_height() * scale_multiplier),
        ],
    )

    player2_sprite = pygame.image.load(player2.sprite)
    player2_sprite_scaled = pygame.transform.flip(
        pygame.transform.scale(
            player2_sprite,
            [
                int(player2_sprite.get_width() * scale_multiplier),
                int(player2_sprite.get_height() * scale_multiplier),
            ],
        ),
        True,
        False,
    )

    player1_name = font_casc.render(
        f"{player1.name} {player1.title}", True, (255, 255, 255)
    )
    player2_name = font_casc.render(
        f"{player2.name} {player2.title}", True, (255, 255, 255)
    )

    window.blit(player1_name, [25, 25])
    window.blit(player2_name, [WIDTH - player2_name.get_width() - 25, 25])

    window.blit(player1_sprite_scaled, [200, 250])
    window.blit(
        player2_sprite_scaled, [WIDTH - player2_sprite_scaled.get_width() - 200, 250]
    )


def draw_objects(player1, player2):
    # Draw Health bars (two rectangles should do)
    # Draw mana orbs
    window.blit(bg, [0, 0])
    players(player1, player2)
    health_bar(player1.health, player2.health)
    spell_board()


def update_turn(turn):
    turn_text = font_casc.render(f"Turn {turn}", True, (255, 255, 255))
    window.blit(turn_text, [(WIDTH / 2) - turn_text.get_width() + 25, 25])


player = Pyromancer("Kcorb", 22)
enemy = Necromancer("Melvin", 45)
turn = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_objects(player, enemy)
    update_turn(turn)
    pygame.display.update()
    turn += 1

    player.health -= 1
    enemy.health -= 1
    if player.health < 30 or enemy.health < 30:
        player.health = rand.randint(31, 99)
        enemy.health = rand.randint(31, 99)
