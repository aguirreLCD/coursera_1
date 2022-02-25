import math


def main():

    i = 0
    pares = 0
    impares = 0

    while i <= 9:
        number = int(input("type a number, please: "))

        if (number % 2) == 0:
            pares = pares + 1

        else:
            impares = impares + 1

        i = i + 1

    print(f"pares: {pares}, impares: {impares}")


main()
