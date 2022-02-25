
import re


def main():

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
        # print(sentenca)
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

        print("lista de sentencas", lista_sentencas)
        print("tamanho lista de sentencas:", tamanho_lista_sentencas)

        print("lista de frases", lista_frases)
        print("tamanho lista de frases:", tamanho_lista_frases)

        print("lista de palavras", lista_palavras)
        print("tamanho lista de palavras:", tamanho_lista_palavras)

        palavras_diferentes = n_palavras_diferentes(lista_palavras)
        print("num total palavras diferentes", palavras_diferentes)

        palavras_unicas = n_palavras_unicas(lista_palavras)
        print("num total palavras unicas", palavras_unicas)

        quantidade_de_letras = []
        for palavra in lista_palavras:
            quantidade_de_letras.extend(palavra)

        total_quantidade_de_letras = len(
            quantidade_de_letras)
        print("lista quantidade de letras",
              quantidade_de_letras)
        print("soma quantidade de letras",
              total_quantidade_de_letras)

        quantidade_caracteres = []
        for frase in lista_frases:
            quantidade_caracteres.extend(frase)

        total_quantidade_de_caracteres = len(quantidade_caracteres)
        print("lista quantidade caracteres",
              quantidade_caracteres)
        print("soma quantidade caracteres",
              total_quantidade_de_caracteres)

        quantidade_caracteres_cada_frase = []
        for caractere in frase:
            quantidade_caracteres_cada_frase.extend(caractere)

        print("qtd carac cada frase", quantidade_caracteres_cada_frase)
        print(len(quantidade_caracteres_cada_frase))

        # # wal_b
        # quantidade de letras
        tamanho_medio_de_palavra = total_quantidade_de_letras / tamanho_lista_palavras
        wal_b = tamanho_medio_de_palavra
        print("wal_b", wal_b)

        # # ttr_b
        relacao_type_token = palavras_diferentes / tamanho_lista_palavras
        ttr_b = relacao_type_token
        # print("ttr_b", relacao_type_token)
        print("ttr_b", ttr_b)

        # # hlr_b
        razao_hapax_legomana = palavras_unicas / tamanho_lista_palavras
        # print("hlr_b", razao_hapax_legomana)
        hlr_b = razao_hapax_legomana
        print("hlr_b", hlr_b)

        # # sal_b
        tamanho_medio_de_sentenca = total_quantidade_de_caracteres / tamanho_lista_sentencas
        sal_b = tamanho_medio_de_sentenca
        print("sal_b", sal_b)

        # # sac_b
        complexidade_de_sentenca = tamanho_lista_frases / tamanho_lista_sentencas
        # print("sac_b", complexidade_de_sentenca)
        sac_b = complexidade_de_sentenca
        print("sac_b", sac_b)

        # # pal_b
        tamanho_medio_de_frase = total_quantidade_de_caracteres / tamanho_lista_frases
        pal_b = tamanho_medio_de_frase
        print("pal_b", pal_b)

        # calcular os 6 traços linguisticos
        # assinatura_b = [wal_b, ttr_b, hlr_b, sal_b, sac_b, pal_b]
        as_b = [wal_b, ttr_b, hlr_b, sal_b, sac_b, pal_b]
        return as_b

    calcula_assinatura(
        texto="Testando texto, carecteres processo, transforma string. Testando texto.")


main()
