
def main():
    repeticao = 3
    i = 0

    while i < repeticao:
        number = int(input("type a number, please: "))
        i = i + 1

    print("numbers: %d " % number)

    number1 = int(input("type number 1, please: "))
    number2 = int(input("type number 2, please: "))
    number3 = int(input("type number 3, please: "))

    if number1 < number3:
        number1, number3 = number3, number1

    if number1 < number2:
        number1, number2 = number2, number1

    if number2 < number3:
        number2, number3 = number3, number2

    print(f'a ordem decrescente é {number1}, {number2} e {number3}')


main()
