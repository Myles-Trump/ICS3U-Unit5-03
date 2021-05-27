#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program converts celsius into fahrenheit


def grading(inputted_string):

    # process
    if "4+" in inputted_string:
        print("\nYou have a 98%")

    elif "4" in inputted_string:
        print("\nYou have a 91%")

    elif "4-" in inputted_string:
        print("\nYou have a 83%")

    elif "3+" in inputted_string:
        print("\nYou have a 78%")

    elif "3" in inputted_string:
        print("\nYou have a 75%")

    elif "3-" in inputted_string:
        print("\nYou have a 71%")

    elif "2+" in inputted_string:
        print("\nYou have a 68%")

    elif "2" in inputted_string:
        print("\nYou have a 65%")

    elif "2-" in inputted_string:
        print("\nYou have a 61%")

    elif "1+" in inputted_string:
        print("\nYou have a 58%")

    elif "1" in inputted_string:
        print("\nYou have a 55%")

    elif "1-" in inputted_string:
        print("\nYou have a 51%")

    elif "R" in inputted_string:
        print("\nYou have a 49% or below")

    else:
        print("\nYou have entered an invalid input, please try again")
        main()

    # output
    print("")


def main():
    # this function calls other functions as well as
    #   takes input

    # input
    inputted_string = input("Please input your grade (4+ to R): ")

    grading(inputted_string)


if __name__ == "__main__":
    main()
