def fizzbuzz(n):

    Fizz = False
    Buzz = False
    FizzBuzz = False

    if (n % 3 == 0) and (n % 5 != 0):
        Fizz = True
        return ("Fizz")
    elif (n % 5 == 0) and (n % 3 != 0):
        Buzz = True
        return ("Buzz")
    elif (n % 3 == 0) and (n % 5 == 0):
        FizzBuzz = True
        return ("FizzBuzz")
    else:
        return (n)
