def isPrime(x):

    factor = 2
    if x == 2:
        return True

    while (x % factor != 0) and (factor <= x/2):
        factor = factor + 1
    if (x % factor == 0):
        return False
    else:
        return True


def n_primos(x):

    # x = int(input("Digite um número inteiro maior ou igual a 2: "))

    n = 2

    conta_primos = 0

    while n <= x:
        if isPrime(n):
            conta_primos = conta_primos + 1
            # print(n, end=', ')
        n = n + 1
    print(conta_primos)
    # print(x)
    return conta_primos


n_primos(30)
# print(n_primos(30))
