import pygame
import sys
import random as rand
from wizards import Pyromancer, Necromancer

# Notes
# Original BG size is (270x152) scaled to (1280x720)
# Sprites and images are scaled by x4.74 from original size
# Change health bar to hears, hearts can be halfed, players start with a row of armored hears which need to be destroyed first
# Armored hearts cannot be healed once destroyed. May add some mechanics for this later.

pygame.init()
pygame.font.init()

# 1280 x 720 display
WIDTH, HEIGHT = 1280, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wizards")
bg = pygame.image.load("assets/backgrounds/bg_corridor.jpg")
font_casc_standard = pygame.font.SysFont("Cascadia Mono", 50)
font_casc_small = pygame.font.SysFont("Cascadia Mono", 35)


def mana_orbs(p1_mana, p2_mana):

    mana_orb = pygame.image.load("assets/health_and_mana/mana_orb.png")

    p1_x = 25
    for i in range(0, p1_mana):
        window.blit(mana_orb, [p1_x, 100])
        p1_x += 45

    p2_x = 60
    for x in range(0, p2_mana):
        window.blit(mana_orb, [WIDTH - p2_x, 100])
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

def blit_spell(spell, img_pos, dmg_pos, mana_pos):

    # Blit spell img
    window.blit(spell[3], img_pos)

    dmg_txt = font_casc_small.render(f"{spell[1]}", True, (255, 255, 255))
    window.blit(dmg_txt, dmg_pos)

    mana_txt = font_casc_small.render(f"{spell[2]}", True, (0, 0, 0))
    window.blit(mana_txt, mana_pos)

def generate_spell(player, pos):
    # Spell click range between spell width with mouse pos
    
    


    spell1 = rand.choice(player.spellbook)
    spell2 = rand.choice(player.spellbook)
    spell3 = rand.choice(player.spellbook)

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


def update_turn(turn):
    turn_text = font_casc_standard.render(f"Turn {turn}", True, (255, 255, 255))
    window.blit(turn_text, [(WIDTH / 2) - turn_text.get_width()+50, 25])


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
player = Pyromancer("Kcorb", 22)
enemy = Necromancer("Cerb", 45)
player_turn = True
turn = 1

while True:
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    #lightshow(player, enemy)
        
    draw_objects(player, enemy)
    update_turn(turn)
    pygame.display.update()
