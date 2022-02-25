def main():
    # user type a number
    number = int(input("Digite o número: "))
    # print(f"number {number}")

    # variable for a remainder of a division by 10 = last digit
    last_digit = number % 10
    # print(f"last {last_digit}")

    # variable for the other digits
    new_num = number // 10
    # print(f"new number {new_num}")

    # initialize a variable for crossing indicator
    digit_adjacent = False

    # counter
    i = 0
    #      1311        and   false
    while new_num > 0 and not digit_adjacent:
        new_last_digit = new_num % 10
        # print(f"new last  {new_last_digit}")
        # print(f"last while {last_digit}")
        # print(new_last_digit == last_digit)

        if (new_last_digit == last_digit):
            digit_adjacent = True

        else:
            i = i + 1

            last_digit = new_last_digit
            # print(f"while last {last_digit}")

            new_num = new_num // 10
            # print(f"while new num {new_num}")

    if digit_adjacent:
        print("sim")
    else:
        print("não")


main()
