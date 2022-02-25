def inverte():
    lista = []

    num = int(input("Digite um número: "))

    while num != 0:
        lista.append(num)
        num = int(input("Digite um número: "))

    print()
    lista.reverse()

    for i in range(len(lista)):
        # print("%d: %d" % (i, lista[i]))
        # lista.reverse()
        print("%d" % (lista[i]))

    # print(lista)
    return lista


inverte()
