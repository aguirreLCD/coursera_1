def main():
    inteiro = int(input("Digite um número inteiro: "))

    divisao_inteira = inteiro // 10
    divisao_resto = divisao_inteira % 10

    digito_dezena = divisao_resto

    print(f"O dígito das dezenas é {digito_dezena}")


main()
