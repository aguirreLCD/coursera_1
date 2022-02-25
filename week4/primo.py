def main():
    x = int(input("Digite um número inteiro: "))

    n = 2

    prime = True

    if x < n:
        prime = False

    while (x > n) and prime:
        check = x % n
        print(check)
        if (x % 2 == 0) or (check == 0):
            prime = False
        else:
            prime = True
        n = n + 1

    if prime:
        print("primo")
    else:
        print("não primo")


main()
