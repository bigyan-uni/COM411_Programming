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


#  Task 3
def export(file_path, export_num):
    print("Exporting...")
    for i in range(export_num):
        with open(file_path, "a") as file:
            item_id = input("Enter the id of the item: ")
            item_name = input("Enter the name of the item: ")
            item_colour = input("Enter the colour of the item: ")
            export_line = f"\n{item_id},{item_name},{item_colour}"
            file.write(export_line)
    print("Done!")


def run_task3():
    export("exported_items.csv", 2)


run_task3()
