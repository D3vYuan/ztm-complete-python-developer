class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")

    def attack(self):
        pass

class Wizard(User):
    # def __init__(self, name, power, email):
        # super().__init__(email)
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"attacking with arrows: arrows left :- {self.arrows}")

    def check_arrows(self):
        print(f"{self.arrows} remaining")

    def run(self):
        print(f"ran really fast")

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name = name, arrows = arrows)
        Wizard.__init__(self, name = name, power = power)

def player_attack(character):
    character.attack()

wizard1 = Wizard("Pete", 50)
archer1 = Archer("Sam", 100)
# print(wizard1.sign_in())
# wizard1.attack()
# archer1.attack()

# print(f"Wizard1 is also a User - {isinstance(wizard1, User)}")

# player_attack(wizard1)
# player_attack(archer1)

# print(wizard1.email)

# print(dir(wizard1))

hybridBorg = HybridBorg(name = "borgie", power = 50, arrows = 100)
print(hybridBorg.run())