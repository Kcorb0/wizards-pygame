import pygame
import os


class Wizard:
    def __init__(self, name, age, speed, health, mana):
        self.name = name
        self.health = health
        self.age = age
        self.mana = mana
        self.speed = speed

    def increase_mana(self):
        increment = 1
        self.mana += increment

    def stat_bars(self, pos):
        return [self.name, self.name, self.age]

    def open_spellbook(self):
        pass

    def idle_stance(self):
        pass

    def battle_stance(self):
        pass


class Pyromancer(Wizard):
    def __init__(self, name, age, speed=55, health=1, mana=3):
        super().__init__(name, age, speed=speed, health=health, mana=mana)
        self.title = "(Pyromancer)"
        self.sprite = "assets/wizards/pyromancer/pyromancer_idle.png"
        self.spellbook = [
            self.spell_explosion(),
            self.spell_firewhirl(),
            self.spell_summonspark(),
        ]

    def spell_explosion(self):
        title = "Explosion"
        dmg = 8
        cost = 7
        card = pygame.image.load("assets/spells/spell_explosion.png")
        description = "Massive damage, destroys surroundings and lowers oponents speed."

        return [title, dmg, cost, card, description]

    def spell_firewhirl(self):
        title = "Fire Whirl"
        dmg = 3
        cost = 6
        card = pygame.image.load("assets/spells/spell_placeholder.png")
        description = "Flames engulf you and linger. (Take 2 damage for 2 turns)"

        return [title, dmg, cost, card, description]

    def spell_summonspark(self):
        title = "Summon Spark"
        dmg = 1
        cost = 3
        card = pygame.image.load("assets/spells/spell_placeholder.png")
        description = "A sentient spark joins you in combat, dealing 1 damage per turn."

        return [title, dmg, cost, card, description]


class Necromancer(Wizard):
    def __init__(self, name, age, speed=40, health=1, mana=3):
        super().__init__(name, age, speed=speed, health=health, mana=mana)
        self.title = "(Necromancer)"
        self.sprite = "assets/wizards/necromancer/necromancer_idle.png"
        self.spellbook = [
            self.spell_corrupt(), 
            self.spell_summon_dead(), 
            self.spell_plague()
        ]

    def spell_corrupt(self):
        title = "Corrupt"
        dmg = 1
        cost = 5
        card = pygame.image.load("assets/spells/spell_placeholder.png")
        description = "Player misses their next 2 turns, thier mind is broken."

        return [title, dmg, cost, card, description]
    
    def spell_summon_dead(self):
        title = "Summon Dead"
        dmg = 2
        cost = 4
        card = pygame.image.load("assets/spells/spell_placeholder.png")
        description = "Summon a dead corpse from surroundings, this guy could be thousands of years old. Deals 2 damage for 4 turns."

        return [title, dmg, cost, card, description]
    
    def spell_plague(self):
        title = "Plague"
        dmg = 4
        cost = 7
        card = pygame.image.load("assets/spells/spell_placeholder.png")
        description = "A strong virus that devours organs when inhailed. Deals 4 damage for 2 turns."

        return [title, dmg, cost, card, description]
