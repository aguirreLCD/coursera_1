# for i in range(20):
#     print(i)

# for i in range(10, 20):
#     print(i)

# for i in range(0, 10, 3):
#     print(i)


# pares = range(0, 40, 2)

# for i in pares:
#     print(i)


# numbers = range(100, 0, -5)

# for x in numbers:
#     print(x)


list_primes = [2, 3, 5, 7, 11, 13]

for i in range(len(list_primes)):
    list_primes[i] = list_primes[i] ** 3


print(list_primes)
# [8, 27, 125, 343, 1331, 2197]
