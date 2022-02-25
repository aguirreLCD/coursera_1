def main():
    # um número X é primo se
    # para todo número N entre 2 e X – 1,
    # o resto da divisão entre X e N é diferente de 0

    x = int(input("Digite um número inteiro: "))

    n = 2

    prime = True

    if x < n:
        prime = False

    while (n < x) and prime:
        if (x % 2 == 0) or (x % n == 0):
            prime = False
        else:
            prime = True
        n = n + 1

    if prime:
        print("primo")
    else:
        print("não primo")


main()
