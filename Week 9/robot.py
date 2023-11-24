class Robot:

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = 0

    def display(self):
        print(f"I am {self.name}.")

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

    def __str__(self):
        return f"Robot {self.name} is {self.age} years old."


if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(robot)
    print(repr(robot))
