def main():
    descrescente = True

    anterior = int(input("Digite o primeiro número da sequência: "))

    valor = 1

    while valor != 0 and descrescente:
        valor = int(input("Digite o próximo número da sequência: "))
        if valor > anterior:
            descrescente = False
        anterior = valor

    if descrescente:
        print("A sequência está em ordem descrescente.")
    else:
        print("A sequência não está em ordem descrescente.")


main()
