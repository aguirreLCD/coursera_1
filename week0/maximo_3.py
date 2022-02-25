def main():

    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))

    if (a >= b) and (a > c):
        print(a)
        print("a")

    elif (b > a) and (b > c):
        print(b)
        print("b")

    elif (c >= b) and (c >= a):
        print(c)
        print("c")


main()


# def maximo(a, b, c):

#     if (a >= b) and (a > c):
#         print(a)
#         print("a aqui")

#     elif (b > a) and (b > c):
#         print(b)
#         print("b aqui")

#     elif (c >= b) and (c >= a):
#         print(c)
#         print("c aqui")


# maximo(0, 0, 1)
