import re


def main():

    assinatura = le_assinatura()
    textos = le_textos()
    numero_do_texto = avalia_textos(textos, assinatura)


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo 
    e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    # [4.51, 0.693, 0.55, 70.82, 1.82, 38.5]
    # print([wal, ttr, hlr, sal, sac, pal])
    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados 
    e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +
                  " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")
    # print(textos)
    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto
     e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    # print(sentencas)
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca
    e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase
    e devolve uma lista das palavras dentro da frase'''
    # print(frase.split())
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras
     e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    # print(unicas)
    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras
     e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    # print(len(freq))
    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR.
    Essa funcao recebe duas assinaturas de texto
    e deve devolver o grau de similaridade nas assinaturas.'''

    list_diferenca = []
    i = 0
    for traco in as_a:
        diferenca = as_a[i] - as_b[i]
        # print(diferenca)

        diferencaAbs = abs(diferenca)
        # print(diferencaAbs)

        list_diferenca.append(diferencaAbs)
        i = i + 1

    # print(list_diferenca)

    soma = 0
    i = 0
    for item in list_diferenca:
        soma = soma + list_diferenca[i]
        i = i + 1

    # print(soma)

    # Sab
    grau_de_similaridade = soma / 6

    # print(grau_de_similaridade)

    return grau_de_similaridade


def calcula_assinatura(texto):
    '''IMPLEMENTAR.
        Essa funcao recebe um texto
        e deve devolver a assinatura do texto.'''

    lista_sentencas = []
    lista_frases = []
    lista_palavras = []

    for sentenca in separa_sentencas(texto):
        lista_sentencas.append(sentenca)

        for frase in separa_frases(sentenca):
            lista_frases.append(frase)

            for palavra in separa_palavras(frase):
                lista_palavras.append(palavra)

    tamanho_lista_sentencas = len(lista_sentencas)
    tamanho_lista_frases = len(lista_frases)
    tamanho_lista_palavras = len(lista_palavras)

    # print("lista de sentencas", lista_sentencas)
    # print("tamanho lista de sentencas:", tamanho_lista_sentencas)

    # print("lista de frases", lista_frases)
    # print("tamanho lista de frases:", tamanho_lista_frases)

    # print("lista de palavras", lista_palavras)
    # print("tamanho lista de palavras:", tamanho_lista_palavras)

    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    # print("num total palavras diferentes", palavras_diferentes)

    palavras_unicas = n_palavras_unicas(lista_palavras)
    # print("num total palavras unicas", palavras_unicas)

    quantidade_de_letras = []
    for palavra in lista_palavras:
        quantidade_de_letras.extend(palavra)

    total_quantidade_de_letras = len(
        quantidade_de_letras)
    # print("lista quantidade de letras",
    #       quantidade_de_letras)
    # print("soma quantidade de letras",
    #       total_quantidade_de_letras)

    quantidade_caracteres = []
    for frase in lista_frases:
        quantidade_caracteres.extend(frase)

    total_quantidade_de_caracteres = len(quantidade_caracteres)
    # print("lista quantidade caracteres",
    #       quantidade_caracteres)
    # print("soma quantidade caracteres",
    #       total_quantidade_de_caracteres)

    quantidade_caracteres_sentenca = []
    for sentenca in lista_sentencas:
        quantidade_caracteres_sentenca.extend(sentenca)

    # print(quantidade_caracteres_sentenca)
    total_qtd_caracteres_sentenca = len(quantidade_caracteres_sentenca)

    # quantidade_caracteres_cada_frase = []
    # for caractere in frase:
    #     quantidade_caracteres_cada_frase.extend(caractere)

    # print("qtd carac cada frase", quantidade_caracteres_cada_frase)
    # print(len(quantidade_caracteres_cada_frase))

    # # wal_b
    # quantidade de letras
    tamanho_medio_de_palavra = total_quantidade_de_letras / tamanho_lista_palavras
    wal_b = tamanho_medio_de_palavra
    # print("wal_b", wal_b)

    # # ttr_b
    relacao_type_token = palavras_diferentes / tamanho_lista_palavras
    ttr_b = relacao_type_token
    # print("ttr_b", relacao_type_token)
    # print("ttr_b", ttr_b)

    # # hlr_b
    razao_hapax_legomana = palavras_unicas / tamanho_lista_palavras
    # print("hlr_b", razao_hapax_legomana)
    hlr_b = razao_hapax_legomana
    # print("hlr_b", hlr_b)

    # # sal_b
    tamanho_medio_de_sentenca = total_qtd_caracteres_sentenca / tamanho_lista_sentencas
    sal_b = tamanho_medio_de_sentenca
    # print("sal_b", sal_b)

    # # sac_b
    complexidade_de_sentenca = tamanho_lista_frases / tamanho_lista_sentencas
    # print("sac_b", complexidade_de_sentenca)
    sac_b = complexidade_de_sentenca
    # print("sac_b", sac_b)

    # # pal_b
    tamanho_medio_de_frase = total_quantidade_de_caracteres / tamanho_lista_frases
    pal_b = tamanho_medio_de_frase
    # print("pal_b", pal_b)

    # calcular os 6 traços linguisticos
    # assinatura_b = [wal_b, ttr_b, hlr_b, sal_b, sac_b, pal_b]
    as_b = [wal_b, ttr_b, hlr_b, sal_b, sac_b, pal_b]
    return as_b


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR.
    Essa funcao recebe uma lista de textos e uma assinatura ass_cp
    e deve devolver o numero (1 a n) do texto
    com maior probabilidade de ter sido infectado por COH-PIAH.'''

    lista = []
    for texto in textos:
        as_b = calcula_assinatura(texto)
        #  return as_b
        grau_similaridade = compara_assinatura(ass_cp, as_b)
        # return grau_de_similaridade
        lista.append(grau_similaridade)

    # print("lista de graus", lista)

    # count = 0
    # for index in range(len(lista)):
    #     print("index", index)
    #     print(lista[index])
    #     print(lista[index+1])

    # guarda_menor_valor = lista[0]
    # guarda_index_menor_valor = 0

    # for index in range(len(lista) - 1):
    #     if lista[index + 1] < guarda_menor_valor:
    #         # print("menor valor é o da frente, na comparação index+1",
    #         #       lista[index + 1], "index:", index + 1)
    #         guarda_menor_valor = lista[index + 1]
    #         guarda_index_menor_valor = index + 1
    # # print("menor valor:", guarda_menor_valor,
    # #       "index:", guarda_index_menor_valor)
    # print()
    # print("O autor do texto", guarda_index_menor_valor +
    #       1, "está infectado com COH-PIAH")

    # while index < len(lista_de_graus_similaridade) - 1:
    #     if valor[index] >= valor[index]:
    #         print(valor)

    #     count = count + 1

    # while lista_de_graus_similaridade:
    #     print(lista_de_graus_similaridade[0])

    print("O autor do texto", lista.index(
        min(lista)) + 1, "está infectado com COH-PIAH")

    return lista.index(min(lista)) + 1

    # return guarda_index_menor_valor + 1


main()
