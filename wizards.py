class Wizard:
    def __init__(self, name, age, health=10, pwr_level=100):
        self.name = name
        self.health = health
        self.age = age
        self.pwr_level = pwr_level

    def __repr__(self):
        return f"Wizard({self.name}, {self.age}, {self.health}, {self.pwr_level})"


class Pyromancer(Wizard):
    def __init__(self, name, age, health=15, pwr_level=100):
        super().__init__(name, health=health, age=age, pwr_level=pwr_level)


if __name__ == "__main__":
    test_wiz = Pyromancer("Testard", 24)
    print(test_wiz)
