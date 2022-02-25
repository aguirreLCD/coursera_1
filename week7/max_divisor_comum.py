# Dados um número inteiro n > 0
# e uma sequência com n números inteiros maiores do que zero,
# determinar o máximo divisor comum entre eles.

# # Por exemplo, para a sequência
# 3    42    105
# o seu programa deve escrever o número 3.


def main():
    # read sequence
    n = int(input("Type the lenght of the sequence (>0): "))

    greatest_commom_divisor_currenty = int(input("Type first number: "))

    # counter for number already readed
    count = 1

    while count < n:
        num = int(input("Type %d number: " % (count + 1)))
        count = count + 1
        greatest_commom_divisor_currenty = greatest_commom_divisor(
            greatest_commom_divisor_currenty, num)

    print("The greatest commom divisor is ",
          greatest_commom_divisor_currenty)


def greatest_commom_divisor(a, b):
    # (int, int) => int
    # receive 2 integers + = a,b
    # return greatest_commom_divisor

    greatest_commom_divisor = a

    while (a % greatest_commom_divisor != 0) or (b % greatest_commom_divisor != 0):
        greatest_commom_divisor -= 1

    return greatest_commom_divisor


main()
