import csv


def read_csv(file_path):
    with open(file_path) as file:
        contents = csv.reader(file)
        headings = next(contents)
        print(f"Headings:\n{headings}")
        print("Values:")
        for values in contents:
            print(values)


def run_task1():
    read_csv("clothing.csv")


if __name__ == "__main__":
    run_task1()


#  Task 2 for CSV files
def extract(file_path):
    print("Extracting...")
    with open(file_path) as file:
        contents = csv.reader(file)
        headings = next(contents)
        names = ""
        for values in contents:
            names += f"{values}\n"
    print("Done!\nThe extracted items are as follows:")
    print(names)


def run_task2():
    extract("clothing.csv")


run_task2()
