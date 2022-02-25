# Dado um num inteiro n, n > 1,
# imprimir sua decomposição em fatores primos,
# indicando também a multiplicidade de cada fator.

# 8 = 2 * 2 * 2
# 20 = 2 * 2 * 5
# 1000 = 2ˆ3 * 5ˆ3

n = int(input("Digite um número inteiro positivo: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print("fator", fator, "multiplicidade", multiplicidade)
    fator = fator + 1
    multiplicidade = 0
