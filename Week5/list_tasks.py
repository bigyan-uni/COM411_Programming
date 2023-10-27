def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def run_task1():
    print(directions())


if __name__ == "__main__":
    run_task1()

#  variation to demonstrate how to index a list.


def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("Moving...")
    movement_list = movements()
    for i in range(0, len(movement_list), 2):
        print(f"{movement_list[i]} for {movement_list[i+1]} steps")


run_task2()

#  variation to demonstrate how to iterate a list.


def menu():
    print("Please select a direction:")
    movement_list = directions()
    for i in range(len(movement_list)):
        print(f"{i}: {movement_list[i]}")


def run_task3():
    menu()


run_task3()
