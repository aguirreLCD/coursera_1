def main():
    squareSide = int(
        input("Digite o valor correspondente ao lado de um quadrado: "))

    perímetro = squareSide * 4
    area = squareSide ** 2

    print("perímetro: %d - área: %d " % (perímetro, area))


main()
