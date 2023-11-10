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
    for i in range(7):
        x = input("Please enter an observation:")
        observations.append(x)
    return observations


def run_tasks2():
    print("Counting observations...")
    stored_list = observed_items()
    observations = set()
    for i in stored_list:
        observations_tuple = (i, stored_list.count(i))
        observations.add(observations_tuple)
    for i in observations:
        print(f"{i[0]} was observed {i[1]} times.")


run_tasks2()
