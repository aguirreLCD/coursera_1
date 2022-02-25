import math


def main():
    x1 = int(input("Digite a coordenada x para o ponto 1: "))
    y1 = int(input("Digite a coordenada y para o ponto 1: "))

    x2 = int(input("Digite a coordenada x para o ponto 2: "))
    y2 = int(input("Digite a coordenada y para o ponto 2: "))

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # print(distance)

    if distance >= 10:
        print("longe")
    else:
        print("perto")


main()
