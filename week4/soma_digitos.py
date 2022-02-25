def main():
    number = int(input("Digite um número inteiro: "))

    last_digit = number % 10

    new_num = number // 10

    sum = 0 + last_digit

    while new_num > 0:
        last_digit = new_num % 10
        new_num = new_num // 10
        sum = sum + last_digit

    print(f"{sum}")


main()
