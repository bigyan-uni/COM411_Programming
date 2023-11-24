class Planet:
    def __init__(self):
        self.humans = []
        self.robots = []
        self.name = ""

    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self,human):
        self.humans.remove(human)

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        self.robots.remove(robot)

    def __str__(self):
        print(f"The humans on this planet are: ", end="")
        for i in self.humans:
            print(f"{i}, ", end="")
        print(f"The robots on this planet are: ", end="")
        for i in self.robots:
            print(f"{i}, ", end="")

    def __repr__(self):
        print(f"Humans : {self.humans}")
        print(f"Robots : {self.robots}")


if __name__ == "__main__":
    earth = Planet()
    earth.add_human("Bigyan")
    earth.add_robot("Wall-E")
    earth.add_robot("Eve")
    earth.__str__()
    earth.__repr__()
