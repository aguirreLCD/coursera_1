import math


def main():

    def bhaskara(a, b, c):
        delta = (b ** 2) - (4 * a * c)
        print(delta)

        if delta < 0:
            print("esta equação não possui raízes reais")
        else:
            root1 = (-b + math.sqrt(delta)) / (2 * a)
            root2 = (-b - math.sqrt(delta)) / (2 * a)
            print(root1, root2)

            if root1 == root2:
                return print(f"Esta equação possui apenas uma raiz dupla {root1:.2f}")

            else:
                if root1 < root2:
                    return print(
                        f"as raízes da equação são {root1:.2f} e {root2:.2f}")
                else:
                    return print(f"as raízes da equação são {root2:.2f} e {root1:.2f}")

    bhaskara(10, 25, 10)


main()
