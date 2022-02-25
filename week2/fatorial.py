def main():
    n = int(input("Digite o valor de n: "))
    fatorial = 1
    i = 2

    while i <= n:
        fatorial = fatorial * i
        i = i + 1

    print("O fatorial de %d é = " % n)


main()
