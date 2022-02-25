largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

linha = 1
coluna = 1

while linha <= altura:
    while coluna <= largura:
        if largura == 1 or largura == coluna or coluna == 1 or altura == 1 or altura == linha or linha == 1:
            print("#", end="")
        else:
            print(" ", end="")
        coluna = coluna + 1

    linha = linha + 1
    print(end="\n")
    coluna = 1
