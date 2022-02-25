def soma_elementos(lista):

    lista = [10, 20, 30]
    soma = 0

    for i in range(len(lista)):
        # print("%d: %d" % (i, lista[i]))
        soma = soma + lista[i]
        # print(soma)

    lista = soma
    # print(lista)
    return lista


# soma_elementos(lista=[10, 20, 30])
# soma_elementos(lista=[1, 2, 3, 4])
# soma_elementos(lista=[5, 5, 5])
