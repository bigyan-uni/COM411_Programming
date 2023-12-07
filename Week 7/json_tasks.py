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


if __name__ == "__main__":
    run()
