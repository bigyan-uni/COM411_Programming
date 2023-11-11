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


run()
