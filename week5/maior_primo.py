

def maior_primo(x):

    def primo(x):
        n = 2
        prime = True

        if x < n:
            prime = False

        while (n < x) and prime:
            if (x % 2 == 0) or (x % n == 0):
                prime = False
            else:
                prime = True
            n = n + 1
        return prime
    while not primo(x):
        x = x - 1
    print(x)
    return x


# maior_primo(7)
maior_primo(100)
