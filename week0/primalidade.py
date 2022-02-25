def main():
    number = int(input("Digite um número inteiro: "))
    count = 1
    prime = False

    # while number > count:
    #     if number % count == 0:
    #         count = count + 1
    #         print("prime")
    #     else:
    #         print("not prime")

    # if number > 1:
    #     print(f"number {number}")

    #     if number % number == 0:
    #         print(f"number {number}")

    #         if number // number == 1:
    #             print(f"number {number}")

    #             print("primo")

    #         else:
    #             print("nao primo")

    # while count <= number:
    #     condition1 = number % 2
    #     print(condition1)

    #     if condition1 == 0:
    #         condition2 = number % number
    #         print(condition2)

    #     if condition2 == 0:
    #         print("nao primo")

    # count = count + 1

    while count < number:
        # count = count + 1
        if number % count == 0 and number % number == 0:
            prime = True
        else:
            prime = False

        count = count + 1

    if prime:
        print("prime")
    else:
        print("not prime")

#  um número (number)  é primo se
# n = 2
# while n <= number - 1:
#  check = x % n
    # if check != 0:
    # primo = True
    #  n = n + 1
#  para todo número N entre 2 e number – 1,
#  o resto da divisão entre X e N é diferente de 0

#

    # while count <= number:
    #     if number % count == 0:
    #         prime = False
    #         # print("nao primo")
    #     count = count + 1
    #     # count = count + 1

    #     # else:
    #     # prime = True
    #     # print("primo")

    # if prime:
    #     print("primo")
    # else:
    #     print("não primo")

    # n = 2
    # while n <= number - 1:
    # check = x % n
    # if check != 0:
    #     primo = True
    #     n = n + 1


main()


# basta que o número dado de entrada
# if number % (n > 1) and number % (n < number) == 0
# seja divisível por qualquer número maior que 1
# e menor que ele mesmo,
# que podemos dizer que ele não é primo.
