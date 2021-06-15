import pygame


class Wizard:
    def __init__(self, name, age, speed=50, health=30, mana=3):
        self.name = name
        self.health = health
        self.age = age
        self.mana = mana

    def increase_mana(self):
        increment = 1
        self.mana += increment

    def use_spell(self, spell):
        # Method takes a list as arguments ['Cast Doubt', 4, 5, other effects]
        title = spell[0]
        dmg = spell[1]
        mana = spell[2]

        print(
            f"{self.name} uses {title} dealing ({dmg}) damage. Mana reduced by ({mana})."
        )

    def open_spellbook(self):
        pass


class Pyromancer(Wizard):
    def __init__(self, name, age, speed=55, health=30, mana=3):
        super().__init__(name, age, health=health, mana=mana)
        self.spells = {}  # Dict of wizard spells {title: [dmg, mana, other effects]}
        self.sprite = None


class Necromancer(Wizard):
    def __init__(self, name, age, speed=40, health=30, mana=3):
        super().__init__(name, age, health=health, mana=mana)
        self.spells = []  # List of wizard spells [title, dmg, mana, other effects]
        self.sprite = None


if __name__ == "__main__":
    test_wiz = Pyromancer("Clint Eastwood", 25)

    print(test_wiz.mana)
    test_wiz.increase_mana()
    print(test_wiz.mana)
