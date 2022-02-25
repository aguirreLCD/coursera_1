# Dados números inteiros n e k, com k >= 0, calcular n elevado a k. Por exemplo, dados os números 3 e 4 o seu programa deve escrever o número 81.


def main():
    n = int(input("Digite o valor de n: "))
    k = int(input("Digite o valor de k: "))

    potencia = 1
    i = 0

    while i < k:
        potencia = potencia * n
        i = i + 1

    print("O valor de %d elevado a %d é %d" % (n, k, potencia))


main()
