def main():
    name = input("Digite o nome do cliente: ")
    expirationDay = input("Digite o dia de vencimento: ")
    expirationMonth = input("Digite o mês de vencimento: ")
    invoice = input("Digite o valor da fatura: ")

    print(
        f"Olá, {name}\nA sua fatura com vencimento em {expirationDay} de {expirationMonth} no valor de R$ {invoice} está fechada.")


main()
