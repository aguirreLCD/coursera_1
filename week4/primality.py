

def main():
    # um número X é primo se
    # para todo número N entre 2 e X – 1,
    # n <= x and n <= (x - 1):
    # o resto da divisão entre X e N é diferente de 0

    x = int(input("Digite um número inteiro: "))

    n = 2

    prime = True

    if x == 0 or x == 1:
        prime = False

    if x == 2:
        prime = True

    # if (x >= n) and (x % 2 == 0):
    #     while (n <= x) and (n <= (x - 1)):
    #         check = x % n
    #         print(check)
    #         if check != 0:
    #             prime = True
    #         n = n + 1

    if (x > n) and (x % 2 == 0):
        prime = False

    else:
        check = x % n
        # print(check)
        if check != 0:
            prime = True
        n = n + 1

    if prime:
        print("primo")
    else:
        print("não primo")


main()
