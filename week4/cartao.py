def main():
    my_card = int(input("Digite o número do cartão: "))

    card_read = 1

    find_my_card = False

    while card_read != 0 and not find_my_card:
        card_read = int(input("Digite o número do próximo cartão: "))
        if card_read == my_card:
            find_my_card = True

    if find_my_card:
        print("My card was found.")
    else:
        print("My card was not found.")


main()
