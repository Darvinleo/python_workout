#!/usr/bin/python3

from random import randint


def gues_number():
    secret_number = randint(0, 100)
    print("I thought of a number from 0 to 100, try to guess it ")
    while True:
        user_input = input("Enter number -->  ")
        try:
            user_answer = int(user_input)
            if user_answer == secret_number:
                print("Just Right!")
                return
            elif user_answer > secret_number:
                print("Too High!")
            else:
                print("Too Low!")
        except ValueError:
            print("Only numbers are allowed")
            pass


if __name__ == "__main__":
    gues_number()
