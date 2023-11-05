#  displays information about the current working directory
import os


#  retrieves file location and files in current working directory
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


#  calls first function
def run():
    print("Processing...")
    cwd()


def display_chars(file_path, num_char):
    with open(file_path) as file:
        char_to_read = file.read(num_char)
        print(f'The first {num_char} characters are:')
        print(char_to_read)


def display_line(file_path):
    with open(file_path) as file:
        first_line = file.readline()
        print()
        print('The first line is:')
        print(first_line)


def display_text(file_path):
    with open(file_path)as file:
        file_data = file.read()
        print('The full text is:')
        print(file_data)


def run_task2():
    display_chars('library.txt', 5)
    display_line('library.txt')
    display_text('library.txt')


if __name__ == '__main__':
    run_task2()


def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        for line in file:
            print(f"Looked in {line.strip()}.")
    print("...Done!")


def runtask3():
    search("library.txt")


runtask3()
