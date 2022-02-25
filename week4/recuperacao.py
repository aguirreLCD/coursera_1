# Dados um número inteiro n > 0 e as notas finais de n alunos,
# determinar quantos alunos ficaram de recuperação.
# Um aluno está de recuperação se sua nota final
# está entre 3.0 e 5.0 (exclusive) A nota máxima é 10.0.


def main():
    number_students = int(input("Digite o total de estudantes: "))
    i = 0
    recuperacao = 0

    while i < number_students:
        grade = int(input("Digite a nota do estudante: "))
        if grade <= 3.0 or grade <= 5.0:
            recuperacao = recuperacao + 1
            i = i + 1
        else:
            i = i + 1

    print(f"recuperacao {recuperacao}")


main()
