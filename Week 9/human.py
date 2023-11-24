class Human:

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}.")

    def __repr__(self):
        return f'human(name={self.name}, age={self.age})'

    def __str__(self):
        return f"Human {self.name} is {self.age} years old."


if __name__ == "__main__":
    human = Human()
    human.display()
    print(human)
    print(repr(human))
