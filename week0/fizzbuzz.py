def main():

    n = int(input("Digite o valor de n: "))

    Fizz = False
    Buzz = False
    FizzBuzz = False

    if (n % 3 == 0) and (n % 5 != 0):
        Fizz = True
        print(Fizz)
        print(' "Fizz" ')
    elif (n % 5 == 0) and (n % 3 != 0):
        Buzz = True
        print(Buzz)
        print(' "Buzz" ')
    elif (n % 3 == 0) and (n % 5 == 0):
        print(FizzBuzz)
        FizzBuzz = True
        print(' "FizzBuzz" ')
    else:
        print(n)


main()


# def fizzbuzz(n):

#     Fizz = False
#     Buzz = False
#     FizzBuzz = False

#     if (n % 3 == 0) and (n % 5 != 0):
#         Fizz = True
#         # print(Fizz)
#         # print("Fizz")

#         return (' "Fizz" ')
#     elif (n % 5 == 0) and (n % 3 != 0):
#         Buzz = True
#         # print(Buzz)
#         # print("Buzz")

#         return (' "Buzz" ')
#     elif (n % 3 == 0) and (n % 5 == 0):
#         FizzBuzz = True
#         # print(FizzBuzz)
#         # print("FizzBuzz")
#         # print(' "FizzBuzz" ')

#         return (' "FizzBuzz" ')
#     else:
#         # print(n)
#         return (n)


# fizzbuzz(15)
