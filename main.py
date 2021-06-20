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
bg = pygame.image.load("assets/new_spooky_bg.png")
font_casc_standard = pygame.font.SysFont("Cascadia Mono", 50)
font_casc_small = pygame.font.SysFont("Cascadia Mono", 35)


def mana_orbs(p1_mana, p2_mana):

    mana_orb = pygame.image.load("assets/mana_orb.png")
    mana_orb_scaled = pygame.transform.scale(
        mana_orb, [int(mana_orb.get_width() * 0.14), int(mana_orb.get_height() * 0.14)]
    )

    p1_x = 25
    for i in range(0, p1_mana):
        window.blit(mana_orb_scaled, [p1_x, 100])
        p1_x += 45

    p2_x = 60
    for x in range(0, p2_mana):
        window.blit(mana_orb_scaled, [WIDTH - p2_x, 100])
        p2_x += 45


def health_bar(p1_hp, p2_hp):
    if p1_hp < 1:
        bar1_width = 400 * p1_hp
    else:
        bar1_width = 400

    if p2_hp < 1:
        bar2_width = 400 * p2_hp
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


def generate_spells(player, pos):

    spell1 = player.spellbook[0]
    spell2 = player.spellbook[1]
    spell2 = player.spellbook[2]

    # First spell
    window.blit(spell1[3], [35, 570])
    dmg_txt = font_casc_small.render(f"{spell1[1]}", True, (255, 194, 222))
    window.blit(dmg_txt, [50, 650])
    mana_txt = font_casc_small.render(f"{spell1[2]}", True, (0, 98, 204))
    window.blit(mana_txt, [190, 580])


def players(player1, player2):

    scale_multiplier = 0.30

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

    player1_name = font_casc_standard.render(
        f"{player1.name} {player1.title}", True, (255, 255, 255)
    )
    player2_name = font_casc_standard.render(
        f"{player2.name} {player2.title}", True, (255, 255, 255)
    )

    # Blit player names
    window.blit(player1_name, [25, 25])
    window.blit(player2_name, [WIDTH - player2_name.get_width() - 25, 25])

    # Blit player sprites
    window.blit(player1_sprite_scaled, [250, 300])
    window.blit(
        player2_sprite_scaled, [WIDTH - player2_sprite_scaled.get_width() - 250, 300]
    )


def draw_objects(player1, player2):
    # Draw Health bars (two rectangles should do)
    # Draw mana orbs
    window.blit(bg, [0, 0])
    players(player1, player2)
    health_bar(player1.health, player2.health)
    mana_orbs(player1.mana, player2.mana)
    spell_board()
    generate_spells(player1, "left")


def update_turn(turn):
    turn_text = font_casc_standard.render(f"Turn {turn}", True, (255, 255, 255))
    window.blit(turn_text, [(WIDTH / 2) - turn_text.get_width() + 25, 25])


player = Pyromancer("Kcorb", 22)
enemy = Necromancer("Billy", 45)
player_turn = True
turn = 1

while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if player_turn == True:
            turn += 1
            if 

    draw_objects(player, enemy)
    update_turn(turn)
    pygame.display.update()
