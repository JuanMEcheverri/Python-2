# if executed print the current date and time and "Executed from the command line"
# if imported print the current date and time and "Imported from {filename}"
import os
import datetime

# from ex1 import print_current_date_and_time, print_name


def print_current_date_and_time():
    print(datetime.datetime.now())


def print_current_working_directory():
    print(os.getcwd())


def print_name():
    print(__name__)


if __name__ == "__main__":  # if its run from command line
    print_current_date_and_time()
    print("Executed from the command line")
else:  # import
    print_current_date_and_time()
    print(f"Imported from {__name__}")
