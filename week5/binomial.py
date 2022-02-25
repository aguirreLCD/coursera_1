def main():

    # leitura do n
    n = int(input("Digite n: "))

    cont = 0
    while cont <= n:
        print("Coeficiente de x^%d y^%d: %d" %
              (n-cont, cont, combinacao(n, cont)))
        cont += 1


def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''

    k_fat = 1
    i = 1

    # COMPLETE ESSA FUNÇÃO

    while i < k:
        i = i + 1
        k_fat = k_fat * i

    return k_fat


def combinacao(m, n):
    '''(int, int) -> int
    Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)
    '''

    # COMPLETE ESSA FUNÇÃO E MUDE O RETURN ABAIXO
    # m!        /  ((m-n)!             n!)
    return fatorial(m) / (fatorial(m-n) * fatorial(n))


# testes
print("Combinacao(4,2) =", combinacao(4, 2))
print("Combinacao(5,2) =", combinacao(5, 2))
print("Combinacao(10,4) =", combinacao(10, 4))

# testes
print("0! =", fatorial(0))
print("1! =", fatorial(1))
print("5! =", fatorial(5))
print("17! =", fatorial(17))


main()
