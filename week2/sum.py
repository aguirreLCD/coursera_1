
# Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma.


def main():
    num = int(input("Digite um inteiro: "))
    soma = 0

    while num != 0:
        soma = soma + num
        num = int(input("Digite um inteiro: "))

    print("A soma eh", soma)


main()
