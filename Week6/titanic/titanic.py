import csv

records = []
headings = []


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



