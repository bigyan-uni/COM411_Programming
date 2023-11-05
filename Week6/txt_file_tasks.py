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

run()
