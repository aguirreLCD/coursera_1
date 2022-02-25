alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# print(alfabeto[13:])

# print(alfabeto[:13])
# letras = alfabeto[1:10]

# print(letras)


# print(alfabeto[13:27])
# letras = alfabeto[:]
# print(letras)

# print(len(alfabeto))
# print(alfabeto[0:13])


# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = carnes
# carnes2.append("ponta de alcatra")


# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = []
# for cns in carnes:
#     carnes2.append(cns)
# carnes2.append("ponta de alcatra")


# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = carnes[:]
# carnes2.append("ponta de alcatra")


# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
# if "ponta de alcatra" in carnes:
#     print("XXX")
# else:
#     if "ponta de alcatra" in carnes2:
#         print("YYY")
#     else:
#         print("ZZZ")

# carnes1 = ["picanha", "alcatra"]
# carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
# carnes3 = carnes2 + carnes1


# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# x = carnes
# del (x[-1])

# print(carnes)
# print(x)
# print(carnes2)
# print(carnes3)


# pares = [2, 4, 6, 8, 10]
# x = pares * 3
# print(x)

# # print(pares)


lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]

# print(lista1 is lista3)
# print(lista2 is lista3)
print(lista3 is lista2)
