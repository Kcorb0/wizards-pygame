import pygame
import os


class Wizard:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana
        self.spell1 = None
        self.spell2 = None
        self.spell3 = None

    def idle_stance(self):
        self.stance = self.sprite[0]

    def battle_stance(self):
        self.stance = self.sprite[1]

    def open_spellbook(self):
        pass


    def cast_spell(self, target, spell_num):
        if spell_num == 1:
            target.health -= self.spell1[1]
            self.mana -= self.spell1[2]
            print(self.spell1[4])
        if spell_num == 2:
            target.health -= self.spell2[1]
            self.mana -= self.spell2[2]
            print(self.spell2[4])
        if spell_num == 3:
            target.health -= self.spell3[1]
            self.mana -= self.spell3[2]
            print(self.spell3[4])


class Pyromancer(Wizard):
    def __init__(self, name, health, mana):
        super().__init__(name, health=health, mana=mana)
        self.title = "(Pyromancer)"
        self.sprite = ["assets/wizards/pyromancer/pyromancer_idle.png", "assets/wizards/pyromancer/pyromancer_bstance.png"]
        self.stance = self.sprite[1]
        self.spellbook = [
            self.spell_explosion(),
            self.spell_firewhirl(),
            self.spell_summonspark(),
        ]

    def spell_explosion(self):
        title = "Explosion"
        dmg = 8
        cost = 7
        card = pygame.image.load("assets/spells/pyromancer/spell_explosion.png")
        description = "Massive damage, destroys surroundings and lowers oponents speed."

        return [title, dmg, cost, card, description]

    def spell_firewhirl(self):
        title = "Fire Whirl"
        dmg = 3
        cost = 6
        card = pygame.image.load("assets/spells/pyromancer/spell_firewhirl.png")
        description = "Flames engulf you and linger. (Take 2 damage for 2 turns)"

        return [title, dmg, cost, card, description]

    def spell_summonspark(self):
        title = "Summon Spark"
        dmg = 1
        cost = 3
        card = pygame.image.load("assets/spells/pyromancer/spell_summonspark.png")
        description = "A sentient spark joins you in combat, dealing 1 damage per turn."

        return [title, dmg, cost, card, description]


class Necromancer(Wizard):
    def __init__(self, name, health, mana):
        super().__init__(name, health=health, mana=mana)
        self.title = "(Necromancer)"
        self.sprite = ["assets/wizards/necromancer/necromancer_idle.png", "assets/wizards/necromancer/necromancer_bstance.png"]
        self.stance = self.sprite[0]
        self.spellbook = [
            self.spell_corrupt(), 
            self.spell_summon_dead(), 
            self.spell_plague()
        ]

    def spell_corrupt(self):
        title = "Corrupt"
        dmg = 1
        cost = 5
        card = pygame.image.load("assets/spells/necromancer/spell_corrupt.png")
        description = "Player misses their next 2 turns, thier mind is broken."

        return [title, dmg, cost, card, description]
    
    def spell_summon_dead(self):
        title = "Summon Dead"
        dmg = 2
        cost = 4
        card = pygame.image.load("assets/spells/necromancer/spell_summondead.png")
        description = "Summon a dead corpse from surroundings, this guy could be thousands of years old. Deals 2 damage for 4 turns."

        return [title, dmg, cost, card, description]
    
    def spell_plague(self):
        title = "Plague"
        dmg = 4
        cost = 7
        card = pygame.image.load("assets/spells/necromancer/spell_plague.png")
        description = "A strong virus that devours organs when inhailed. Deals 4 damage for 2 turns."

        return [title, dmg, cost, card, description]
