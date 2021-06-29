import pygame
import sys
import random as rand
from wizards import Pyromancer, Necromancer

# Notes
# Original BG size is (270x152) scaled to (1280x720)
# Sprites and images are scaled by x4.74 from original size
# Change health bar to hears, hearts can be halfed, players start with a row of armored hears which need to be destroyed first
# Armored hearts cannot be healed once destroyed. May add some mechanics for this later.
# Spells should be able to be clicked, but start by using the 123 keys to select spells first or add both

pygame.init()
pygame.font.init()

# 1280 x 720 display
WIDTH, HEIGHT = 1280, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wizards")
bg = pygame.image.load("assets/backgrounds/bg_corridor.jpg")
font_casc_standard = pygame.font.SysFont("Cascadia Mono", 40)
font_casc_small = pygame.font.SysFont("Cascadia Mono", 35)


def mana_orbs(p1_mana, p2_mana):

    mana_orb = pygame.image.load("assets/health_and_mana/mana_orb.png")
    p1_x = 25
    for n in range(0, p1_mana):
        window.blit(mana_orb, [p1_x, 105])
        p1_x += 45
    p2_x = 60
    for n in range(0, p2_mana):
        window.blit(mana_orb, [WIDTH - p2_x, 105])
        p2_x += 45


def health_bar(p1_hearts, p2_hearts):

    heart = pygame.image.load("assets/health_and_mana/heart.png")
    p1_x = 25
    for i in range(0, p1_hearts):
        window.blit(heart, [p1_x, 65])
        p1_x += 45
    p2_x = 60
    for x in range(0, p2_hearts):
        window.blit(heart, [WIDTH - p2_x, 65])
        p2_x += 45


def blit_spell(spell, img_pos, dmg_pos, mana_pos):

    # Blit spell img
    window.blit(spell[3], img_pos)

    dmg_txt = font_casc_small.render(f"{spell[1]}", True, (255, 255, 255))
    window.blit(dmg_txt, dmg_pos)

    mana_txt = font_casc_small.render(f"{spell[2]}", True, (0, 0, 0))
    window.blit(mana_txt, mana_pos)


def generate_spell(player, pos):
    # Spell click range between spell width with mouse pos
    #rand.choice()
    spell1 = player.spellbook[0]
    spell2 = player.spellbook[1]
    spell3 = player.spellbook[2]

    player.spell1 = spell1
    player.spell2 = spell2
    player.spell3 = spell3

    s_dist = 190
    s_ht = 575

    if pos == "left":
        blit_spell(spell1, [37, s_ht], [50, 650], [205, 583])
        blit_spell(spell2, [37+s_dist, s_ht], [50+s_dist, 650], [205+s_dist, 583])
        blit_spell(spell3, [37+(s_dist*2), s_ht], [50+(s_dist*2), 650], [205+(s_dist*2), 583])

    elif pos == "right":
        blit_spell(spell1, [670, s_ht], [683, 650], [838, 583])
        blit_spell(spell2, [670+s_dist, s_ht], [683+s_dist, 650], [838+s_dist, 583])
        blit_spell(spell3, [670+(s_dist*2), s_ht], [683+(s_dist*2), 650], [838+(s_dist*2), 583])


def players(player1, player2):

    # Create player images
    player1_sprite = pygame.image.load(player1.sprite)
    player2_sprite = pygame.transform.flip(pygame.image.load(player2.sprite), True, False)

    # Create player names text
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
    window.blit(player1_sprite, [250, 250])
    window.blit(player2_sprite, [WIDTH - player2_sprite.get_width() - 250, 250])


def draw_objects(player1, player2):

    window.blit(bg, [0, 0])
    players(player1, player2)
    # Create player health bar and mana orbs
    health_bar(player1.health, player2.health)
    mana_orbs(player1.mana, player2.mana)
    # Create generated player spells
    generate_spell(player1, "left")
    generate_spell(player2, "right")


def lightshow(p1, p2):
    # Why not
    if p1.mana > 10:
        p1.mana = 1
        p2.mana = 1

    if p1.health <= 0:
        p1.health += 1
        p2.health += 1

    player.mana += 1
    p2.mana += 1
    p1.health -= .01
    enemy.health -= .01

# Necromancer("Billy", 45)
# Pyromancer("Kcorb", 22)
player = Pyromancer("Kcorb", 10, 10)
enemy = Necromancer("Cerb", 10, 10)
player_turn = True

while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            print(mouse_pos)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                player.cast_spell(enemy, 1)
            if event.key == pygame.K_2:
                player.cast_spell(enemy, 2)
            if event.key == pygame.K_3:
                player.cast_spell(enemy, 3)

    
    draw_objects(player, enemy)
    pygame.display.update()

    # lightshow(player, enemy)
