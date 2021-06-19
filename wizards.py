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


class Pyromancer(Wizard):
    def __init__(self, name, age, speed=55, health=1, mana=3):
        super().__init__(name, age, speed=speed, health=health, mana=mana)
        self.title = "(Pyromancer)"
        self.sprite = "assets/pyromancer.png"
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
        card_scaled = pygame.transform.scale(
            card, [int(card.get_width() * 0.45), int(card.get_height() * 0.45)]
        )
        description = "Massive damage, destroys surroundings and lowers oponents speed."

        return [title, dmg, cost, card_scaled, description]

    def spell_firewhirl(self):
        title = "Fire Whirl"
        dmg = 3
        cost = 6
        card = pygame.image.load("assets/spells/placeholder.png")
        description = "Flames engulf you and linger. (Take 2 damage for 2 turns)"

        return [title, dmg, cost, card, description]

    def spell_summonspark(self):
        title = "Summon Spark"
        dmg = 1
        cost = 3
        card = pygame.image.load("assets/spells/placeholder.png")
        description = "A sentient spark joins you in combat, dealing 1 damage per turn."

        return [title, dmg, cost, card, description]


class Necromancer(Wizard):
    def __init__(self, name, age, speed=40, health=1, mana=3):
        super().__init__(name, age, speed=speed, health=health, mana=mana)
        self.title = "(Necromancer)"
        self.sprite = "assets/necromancer.png"
        self.spellbook = ["Corrupt"]

    def spell_corrupt(self):
        title = "Corrupt"
        dmg = 8
        cost = 7
        description = "Massive damage, destroys surroundings and lowers oponents speed."

        return [title, dmg, cost, description]


if __name__ == "__main__":
    os.system("cls")
    test_wiz = Pyromancer("Clint Eastwood", 25)
    print(test_wiz.name)
    print(test_wiz.spellbook[0][1])
