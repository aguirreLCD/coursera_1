import math


def is_hypotenuse(n):

    i = 1
    j = 2

    isHypotenuse = False

    while i <= n - 1:
        while j <= n and not isHypotenuse:
            # executa essa equação, trocando os valores de i, j
            # hypotenuse = ((i ** 2) + (j ** 2))
            # print(f"hipotenusa while: ", hypotenuse)
            # print("n: %d, i: %d, j: %d" % (n, i, j))
            # print(n)

            # printar
            # os primeiros pares de catetos i, j
            # que resultam em uma hipotenusa inteira
            if n == (i ** 2 + j ** 2)**(1/2):
                # print(f"if hip == n", i, j)
                # print(f"numbers to save: i, j", i, j)
                print("%d^2 + %d^2 = %d^2" % (i, j, n))
                isHypotenuse = True
            else:
                # print(f"else ", i, j, n)
                isHypotenuse = False
            j = j + 1

        j = 2
        i = i + 1
        isHypotenuse = False


is_hypotenuse(25)


# i = 27
# j = 39

# hypotenuse = round(math.sqrt(i ** 2 + j ** 2))

# print(hypotenuse)
