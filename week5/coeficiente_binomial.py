# Os Coeficientes ou Números Binomiais
# são formas algébricas de representar um valor.
# Ele é genericamente expressado por “n” sobre “p”,
# dentro de um parêntesis.
# Esse valor pode ser calculado desenvolvendo-se uma fórmula com fatorial,
# semelhante a da análise combinatória.

# É como se fosse uma fração com numerador (n) e denominador (p).
# Porém, não usamos o traço entre eles, justamente para diferenciar.
# O coeficiente binomial não equivale a uma simples divisão.

# os números binomiais são uma ferramenta
# que acelerou os avanços na matemática e na engenharia,
# porque facilitaram o cálculo de produtos notáveis
# (fatoração de polinômios).

# regrinhas de produtos notáveis:

# (n+p)0 = 1
# (n+p)1 = (n+p)
# (n+p)2 = n² + 2np + p²
# (n+p)3 = n³ + 3n²p + 3np³ + p³

# No Ensino Fundamental,
# nós só aprendemos a resolver binômios
# com potências para os expoentes menores ou iguais a 3.

# Porém, os binômios de Newton(sim, o cientista)
#  servem justamente para as situações em que precisamos resolver binômios
# elevados a expoentes maiores ou iguais a 4.

# Concluímos que o coeficiente binomial
# é importante para o que vem depois da matemática básica e, graças a ele,
# os físicos, químicos e matemáticos puderam evoluir nas ciências.

# quando n = p o resultado é sempre 1;
# quando p = 0 o resultado é sempre 1;
# quando p = 1 o reseultado é sempre n;

# Dois coeficientes binomiais serão do tipo complementares se
# seus numeradores forem iguais
# e a soma de seus denominadores for igual ao numerador.

# Os coeficientes binomiais podem ser organizados, em ordem crescente,
# em um formato de triângulo retângulo.
# A esse fenômeno chamamos de Triângulo de Pascal ou Tartaglia.
# Organizá-los dessa forma nos permite observar
# uma série de propriedades internas,
# que podem ajudar na hora de resolver questões de progressão numérica.


def main():

    def fatorial(n):
        fatorial = 1

        while (n > 1):
            fatorial = fatorial * n
            n = n - 1
        return fatorial

    print(fatorial(5))

    def test_fatorial():

        if fatorial(0) == 1:
            print("works ok on 0")
        else:
            print("do not work on 0")

        if fatorial(1) == 1:
            print("works ok on 1")
        else:
            print("do not work on 1")

        if fatorial(2) == 2:
            print("works ok on 2")
        else:
            print("do not work on 2")

        if fatorial(5) == 120:
            print("works ok on 5")
        else:
            print("do not work on 5")

    test_fatorial()

    def num_binomial(n, k):
        return fatorial(n) // (fatorial(k) * fatorial(n-k))
        # return fatorial(n) / (fatorial(k) * fatorial(n-k))

    print(num_binomial(5, 3))
    print(num_binomial(20, 10))


main()
