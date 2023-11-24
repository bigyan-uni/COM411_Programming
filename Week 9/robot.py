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

    def grow(self):
        self.age += 1

    def eat(self, amount):
        new_energy = self.energy + amount
        if new_energy > Robot.MAX_ENERGY:
            self.energy = Robot.MAX_ENERGY
        else:
            self.energy = new_energy

    def move(self, distance):
        distance = int(distance)
        new_energy = self.energy - distance
        if new_energy < 0:
            self.energy = 0
        else:
            self.energy = new_energy


if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(robot)
    print(repr(robot))
    robot.grow()
    print(robot.age)
    robot.energy = 0
    robot.eat(10)
    print(robot.energy)
    robot.eat(115)
    print(robot.energy)
    robot.move(15)
    print(robot.energy)
    robot.move(90)
    print(robot.energy)
