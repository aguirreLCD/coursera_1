def main():

    sequence = int(
        input("Digite o tamanho da sequência de números a serem somados: "))
    i = 0
    soma = 0

    while sequence > i:
        num = int(input("Digite um inteiro para somar: "))
        soma = soma + num
        i = i + 1

    print(f"A soma desta sequência é: {soma}")


main()
