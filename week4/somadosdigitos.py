def main():
    number = int(input("Digite o valor de n: "))

    # i = len(str(number))

    # print(f"{i}")

    last_digit = number % 10

    new_num = number // 10

    sum = 0 + last_digit

    while new_num > 0:
        last_digit = new_num % 10
        new_num = new_num // 10
        sum = sum + last_digit

    print(f"sum: {sum}")


main()
