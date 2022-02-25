import math


def main():

    number1 = int(input("type number 1, please: "))
    number2 = int(input("type number 2, please: "))
    number3 = int(input("type number 3, please: "))

    if number1 < number2 and number2 < number3:
        print("crescente")
    else:
        print("não está em ordem crescente")


main()
