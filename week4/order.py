def main():
    sequence = int(input("Digite o tamanho da sequência por favor: "))
    number1 = int(
        input("Digite o primeiro número inteiro por favor (n > 0): "))
    i = 0
    crescent = True

    while i < sequence - 1:
        number = int(
            input("Digite o próximo número inteiro por favor (n > 0): "))

        if number < number1:
            crescent = False

        i = i + 1

        number = number1

    if crescent:
        print("Está em ordem crescente")
    else:
        print("Não está em ordem crescente")


main()
