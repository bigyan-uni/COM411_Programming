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
