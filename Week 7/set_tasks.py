#  Task 1
def observed():
    observations = set()
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    print(observed())


run_task1()


#  Task 2
def observed_items():
    observations = []
    for i in range(5):
        x = input("Please enter an observation:")
        observations.append(x)
    return observations


def run_tasks2(stored_list):
    print("Counting observations...")
    observations = set()
    for i in stored_list:
        observations_tuple = (i, stored_list.count(i))
        observations.add(observations_tuple)
    for i in observations:
        print(f"{i[0]} was observed {i[1]} times.")


run_tasks2(observed_items())


#  Task 3
def remove_observations(observations):
    wish_to_remove = input("Do you wish to remove any observations? (yes/no)")
    while wish_to_remove == "yes":
        observation_to_remove = input("What observation would you like to remove?")
        observations.remove(observation_to_remove)
        print("Done!")
        wish_to_remove = input("Do you wish to remove any observations? (yes/no)")
    return observations


def run_task3():
    observations = observed_items()
    run_tasks2(sorted(remove_observations(observations)))


run_task3()
