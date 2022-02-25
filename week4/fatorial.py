def main():
    n = int(input("Digite o valor de n: "))
    fatorial = n

    if n == 0:
        fatorial = 1
        print(f"{fatorial}")

    else:
        fatorial = n
        while n > 1:
            fatorial = fatorial * (n-1)
            n = n - 1

        print(f"{fatorial}")


main()
