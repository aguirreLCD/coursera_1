def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    media = float((nota1 + nota2 + nota3 + nota4) / 4.00)

    print("A média aritmética é %.1f" % media)


main()
