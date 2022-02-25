def main():
    n = int(input("Digite o valor de n: "))

    i = 0

    n = n * 2

    while i <= n:
        if i % 2 != 0:
            print(i)
        i = i + 1


main()
