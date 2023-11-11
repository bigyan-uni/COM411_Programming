import csv

records = []
headings = []


#  imports data set and separates header from data
def load_data(file_path):
    print("Loading data...")
    with open(file_path) as file:
        contents = csv.reader(file)
        headings = next(contents)
        for line in contents:
            records.append(line)
    print("Done!")


def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option: [{selected_option}]")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survived()
    elif selected_option == 3:
        display_passengers_per_gender()
    else:
        print("Error! Option not recognised!")


#  implementing a menu to process data
def display_menu():
    print("""
    Please select one of the following options:
    [1] Display the names of all passengers
    [2] Display the number of passengers that survived
    [3] Display the number of passengers per gender
    [4] Display the number of passengers per age group
    [5] Display the number of survivors per age group"
    """)
    return int(input())


#  function to display passenger names
def display_passenger_names():
    print("The names of the passengers are...")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


#  function to display number of passengers that survived
def display_num_survived():
    num_survived = 0
    for record in records:
        survived_status = int(record[1])
        if survived_status == 1:
            num_survived += 1
    print(f"{num_survived} passengers survived.")


# function to display the number of passengers per gender
def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender == "male":
            males += 1
        elif gender == "female":
            females += 1
    print(f"Females: {females}, Males: {males}")


run()
