import math


def main():

    a = float(input("enter the value of a: "))
    b = float(input("enter the value of b: "))
    c = float(input("enter the value of c: "))

    delta = b ** 2 - 4 * a * c
    # print(delta)

    if delta < 0:
        print("esta equação não possui raízes reais")

    else:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        # print(root1, root2)

        if delta == 0:
            print(f"a raíz desta equação é {root1:.2f}")

        else:
            if root1 < root2:
                print(f"as raízes da equação são {root1:.2f} e {root2:.2f}")
            else:
                print(f"as raízes da equação são {root2:.2f} e {root1:.2f}")


main()
