#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: October 24th, 2023
# this program tells the user if they are older then 25 or younger then 40 to get married.


def main():
    # user inputs the age of the person who wants to get married.
    older_age = int(input("Enter your age if you are older then 25: "))
    younger_age = int(input("Enter your age if you are younger then 40: "))
    print("")

    # terminal will process of the age is older then 25 and younger then 40
    if older_age >= 25 and younger_age >= 40:
        print("you can get married!.")
    else:
        print("you can not get married.")


if __name__ == "__main__":
    main()
