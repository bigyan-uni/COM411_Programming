import json


def read(file_path):
    with open(file_path) as file:
        data = json.load(file)
        location = data["location"]
        print(f"Place Name: {location}")
        population = data["population"]
        print(f"Population Size: {population}")
        bots = data["bots"]
        for bot in bots:
            name = bot["name"]
            stats = bot["stats"]
            speed = stats["speed"]
            strength = stats["strength"]
            print(f"{name} has a strength level of {strength} and a speed level of {speed}.")


def run():
    read("futurama.json")


def read_task2(file_path):
    print("Reading...", end="")
    with open(file_path) as file:
        data = json.load(file)
    print("Done!")
    return data


def save(file_path, data):
    print("Exporting...", end="")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print("Done!")


def run_task2():
    data = read_task2("futurama.json")
    save("exported.json", data)


if __name__ == "__main__":
    run_task2()
