class PlayerCharacter():

    # Class Obiect Attribute
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return "done"

    def shout(self):
        print(f"my name is {self.name}")

    @classmethod
    def adding_things(cls, num1, num2): # cls is similar to self
        return cls("Teddy", num1 + num2)

    @staticmethod # staticmethod cannot have access to cls
    def adding_things2(num1, num2):
        return num1 + num2