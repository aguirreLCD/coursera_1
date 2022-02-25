import math


def main():

    number = int(input("type a number, please: "))

    if ((number % 5) == 0) and ((number % 3) == 0):
        print("FizzBuzz")

    else:
        print(number)


main()
