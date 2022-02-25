largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

cont = 1

while cont <= altura:
    while cont <= largura:
        print("#", end="")
        cont = cont + 1
    cont = 1
    altura = altura - 1
    print(end="\n")
