def main():
    total_alunos = int(input("Digite a quantidade de alunos: "))
    i = 0

    recuperacao = 0
    reprovados = 0
    aprovados = 0
    desempenho_bom = 0

    while i <= total_alunos:
        nota = float(input("Digite a nota: "))

        if (nota >= 3.0) and (nota < 5.0):
            recuperacao = recuperacao + 1
        if nota < 3.0:
            reprovados = reprovados + 1
        if nota > 5.0:
            aprovados = aprovados + 1
        if nota > 8.0:
            desempenho_bom = desempenho_bom + 1

        i = i + 1

    print(f"Total de alunos = {total_alunos}")
    print(f"Número de alunos reprovados = {reprovados}")
    print(f"Número de alunos de recuperação = {recuperacao}")
    print(f"Número de alunos aprovados = {aprovados}")
    print(f"Número de alunos com desempenho muito bom = {desempenho_bom}")


main()
