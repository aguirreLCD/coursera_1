def main():
    number = int(input("Digite o valor de n (n > 0): "))

    digito = int(input("Digite o valor do digito (0<=d<=9): "))

    occur = 0

    num = number

    while number > 0:
        last_digit = number % 10

        if digito == last_digit:
            occur = occur + 1
            number = number // 10
        else:
            occur = occur
            number = number // 10

    print(f" occur {occur} times.")

    print(f"O dígito {digito} ocorre {occur} vezes em {num}.")


main()
