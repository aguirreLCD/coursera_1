def maior_elemento(lista):

    nova_lista = []

    for i in range(len(lista)):
        # print("%d: %d" % (i, lista[i]))
        if lista[i] not in nova_lista:
            # print("if i", i)
            # print("if lista i", lista[i])
            nova_lista.append(lista[i])

            nova_lista.sort()

    lista = nova_lista[-1]
    # print(lista)
    return lista

# maior_elemento(lista=[13, 7, 4, 10])
