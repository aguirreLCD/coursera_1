import math


def é_hipotenusa(n):

    i = 1
    j = 2

    isHypotenuse = False

    while j <= n and not isHypotenuse:
        while i <= n:
            if n == (i ** 2 + j ** 2)**(1/2):
                isHypotenuse = True
                return n, isHypotenuse
            else:
                isHypotenuse = False
            i = i + 1

        i = 1
        j = j + 1
        isHypotenuse = False


def soma_hipotenusas(n):
    count = 0
    soma = 0
    cateto = 0

    while n >= 1:
        if é_hipotenusa(n):
            cateto = n
            soma = soma + cateto
        count = count + 1
        n = n - 1
    return soma
