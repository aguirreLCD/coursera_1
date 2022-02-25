import re


def main():

    def calcula_assinatura(texto):
        lista_sentencas = []
        for sentenca in separa_sentencas(texto):
            lista_sentencas.append(sentenca)
        print("lista de sentencas", lista_sentencas)

        lista_frases = []
        for frase in separa_frases(sentenca):
            lista_frases.append(frase)
        # print("lista de frases", lista_frases)

        lista_palavras = []
        for palavra in separa_palavras(frase):
            lista_palavras.append(palavra)
        print("lista de palavras", lista_palavras)

    def separa_sentencas(texto):
        '''A funcao recebe um texto
        e devolve uma lista das sentencas dentro do texto'''
        sentencas = re.split(r'[.!?]+', texto)
        if sentencas[-1] == '':
            del sentencas[-1]
        # print("2", sentencas)
        return sentencas

    def separa_frases(sentenca):
        # print(sentenca)
        return re.split(r'[,:;]+', sentenca)

    def separa_palavras(frase):
        # print(frase.split())
        return frase.split()

    calcula_assinatura(
        texto="testando texto, carecteres processo, transforma string")


main()
