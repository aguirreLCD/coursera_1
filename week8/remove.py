def remove_repetidos(lista):

    nova_lista = []

    for i in range(len(lista)):
        # print("%d: %d" % (i, lista[i]))
        if lista[i] not in nova_lista:
            # print("if i", i)
            # print("if lista i", lista[i])
            nova_lista.append(lista[i])

            nova_lista.sort()

    # print("lista", lista)
    # print("nova lista", nova_lista)
    # sorted(nova_lista)
    # nova_lista.sort()
    lista = nova_lista
    print(lista)
    return lista


# remove_repetidos(lista=[2, 4, 2, 2, 3, 3, 1])
# remove_repetidos(lista=[1, 2, 3, 3, 3, 4])
# remove_repetidos(lista=[1, 2, 3, 3, 3, 4])
remove_repetidos(lista=[2, 3, 5, 5, 5, 1, 1])
