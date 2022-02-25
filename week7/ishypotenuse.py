def is_hypotenuse(c):

    # c = ishopotenuse to check
    # a, b = cathetus, catheti
    # commonly known as leg
    leg_a = 1
    leg_b = 2

    isHypotenuse = False

    while leg_b <= c and not isHypotenuse:
        while leg_a <= c:
            # execute the square root function implied
            # by the Pythagorean theorem
            # c = √a² + b² √ √
            if c == (leg_a ** 2 + leg_b ** 2)**(1/2):
                print("%d^2 + %d^2 = %d^2" % (leg_a, leg_b, c))

                isHypotenuse = True

                return c, isHypotenuse
            else:
                isHypotenuse = False
            leg_a = leg_a + 1

        leg_a = 1
        leg_b = leg_b + 1
        isHypotenuse = False


def sum_hypotenuse(c):
    count = 0
    sum = 0
    hypotenusa_to_sum = 0

    while c >= 1:
        if is_hypotenuse(c):
            hypotenusa_to_sum = c
            print(hypotenusa_to_sum, "is hypotenuse")
            print()
            sum = sum + hypotenusa_to_sum
        count = count + 1
        c = c - 1

    print(sum)
    return sum


sum_hypotenuse(25)

# is_hypotenuse(25)

# 24 ^ 2 + 7 ^ 2 = 25 ^ 2
# 25
# 16^2 + 12 ^ 2 = 20 ^ 2
# 20
# 15 ^ 2 + 8 ^ 2 = 17 ^ 2
# 17
# 12 ^ 2 + 9 ^ 2 = 15 ^ 2
# 15
# 12 ^ 2 + 5 ^ 2 = 13 ^ 2
# 13
# 8 ^ 2 + 6 ^ 2 = 10 ^ 2
# 10
# 4 ^ 2 + 3 ^ 2 = 5 ^ 2
# 5
# 105
