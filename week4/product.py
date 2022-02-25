def main():

    sequence = int(
        input("Digite o tamanho da sequência de números a serem multiplicados: "))
    i = 0
    product = 1

    while sequence > i:
        num = int(input("Digite um inteiro para multiplicar: "))
        product = product * num
        i = i + 1

    print(f"O produto da multiplicação desta sequência é: {product}")


main()
