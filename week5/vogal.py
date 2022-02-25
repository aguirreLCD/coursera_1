from curses.ascii import isalpha


def main():

    def vogal(a):
        caractere = str(a).upper()
        vogal = False
        consoante = False
        print(caractere)

        if caractere.isalpha():
            if caractere in "AEIOU":
                vogal = True
                print(vogal)
                return(vogal)
            else:
                print(consoante)
                return(consoante)
        else:
            print("por favor insira um caractere válido")

    vogal("a")
    vogal("b")
    vogal("E")
    vogal("D")
    vogal("C")
    vogal("A")
    vogal("E")
    # vogal(a=2)
    # vogal(3)


main()
