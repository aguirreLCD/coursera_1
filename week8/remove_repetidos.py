def remove_repetidos(lista):

    nova_lista = []

    for i in range(len(lista)):
        if lista[i] not in nova_lista:
            nova_lista.append(lista[i])
            nova_lista.sort()

    nova_lista.sort()
    lista = nova_lista
    return lista
