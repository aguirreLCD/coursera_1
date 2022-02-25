import math


def delta(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    print(delta)
    return delta


def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    roots(a, b, c)


def roots(a, b, c):
    var_delta = delta(a, b, c)
    print(var_delta)

    if var_delta < 0:
        print("esta equação não possui raízes reais")
    else:
        root1 = (-b + math.sqrt(var_delta)) / (2 * a)
        root2 = (-b - math.sqrt(var_delta)) / (2 * a)
        print(root1, root2)

        if root1 == root2:
            print(f"Esta equação possui apenas uma raiz dupla {root1:.2f}")

        else:
            if root1 < root2:
                print(
                    f"as raízes da equação são {root1:.2f} e {root2:.2f}")
            else:
                print(f"as raízes da equação são {root2:.2f} e {root1:.2f}")


main()
