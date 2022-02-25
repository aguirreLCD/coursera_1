def main():
    repeticao = int(input("Digite a quantidade de notas: "))

    i = 0
    soma = 0

    while i < repeticao:
        nota = int(input("Digite a nota: "))
        soma = nota + soma
        i = i + 1

    print("soma das notas: ", soma)

    media = soma / repeticao

    print("media das notas: %.1f" % media)


main()
