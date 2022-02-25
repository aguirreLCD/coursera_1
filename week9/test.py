lista = [2, 1, 4, 5, 0, 10, 1]
print(lista)

# guarda_menor_valor = lista[0]
# guarda_index_menor_valor = 0

# for index in range(len(lista) - 1):
#     if lista[index + 1] < guarda_menor_valor:
#         print("menor valor é o da frente, na comparação index+1",
#               lista[index + 1], "index:", index + 1)
#         guarda_menor_valor = lista[index + 1]
#         guarda_index_menor_valor = index + 1
# print("menor valor:", guarda_menor_valor, "index:", guarda_index_menor_valor)


print(lista.index(min(lista)))
