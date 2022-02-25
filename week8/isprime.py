def isPrime(x):
    factor = 2
    if x == 2:
        return True

    while (x % factor != 0) and (factor <= x/2):
        factor = factor + 1
    if (x % factor == 0):
        return False
    else:
        return True


limit = int(input("Max limit: "))

n = 2
while n < limit:
    if isPrime(n):
        print(n, end=', ')
    n = n + 1

list_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
               41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print()
print(f"len: ", len(list_primes))
