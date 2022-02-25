# print('Bem-vindo ao jogo do NIM! Escolha:')
# print('')
# print('1 - para jogar uma partida isolada')
# partidaOuCampeonato = int(input('2 - para jogar um campeonato '))
# if partidaOuCampeonato == 1:
#     partida()
# if partidaOuCampeonato == 2:
#     campeonato()
# print('')
# print('**** Final do campeonato! ****')
# print('')


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m+1) == 0:
        print()
        print("Você começa!")
        usuarioJogando = True
    else:
        print()
        print("Computador começa!")
        usuarioJogando = False

    while n > 0:
        if usuarioJogando:
            print()
            user_play = usuario_escolhe_jogada(n, m)
            print("Você tirou", user_play, "peças.")
            n = n - user_play
            print("Agora restam", n, "peças no tabuleiro.")
            usuarioJogando = False
        else:
            print()
            pc_play = computador_escolhe_jogada(n, m)
            print("O computador tirou", pc_play, "peças.")
            n = n - pc_play
            print("Agora restam", n, "peças no tabuleiro.")
            usuarioJogando = True

    print(n, m)
    return n, m


def usuario_escolhe_jogada(n, m):
    print()
    jogadaDoUsuario = int(input("Quantas peças você vai tirar?"))

    if jogadaDoUsuario > m:
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        jogadaDoUsuario = int(input("Quantas peças você vai tirar?"))

    n = jogadaDoUsuario
    return n


def computador_escolhe_jogada(n, m):
    print(f"n, m, def pc", n, m)

    # print(n % (m + 1))

    # pc_tira = n % (m + 1)
    # print(pc_tira)

    # cont = 0
    if n % (m+1) != 0:

        # if n % (m+1) < m
        #######################################################
        # while n % (m+1) != 0
        # nNaMesa = n
        # m=m-1
        #   if n % (m+1) == 0
        #       if nNaMesa-n % (m+1) == 0
        #           jogadaDoComputador = n
        #       else
        #       #tryAgainMeuFilho
        #######################################################
        jogadaDoComputador = n - (n - (m-1))
        print(jogadaDoComputador)

        # if jogadaDoComputador == 0:
        #     jogadaDoComputador = jogadaDoComputador + 1
    else:
        # print(n)
        # print(jogadaDoComputador)
        if n < m:
            # jogadaDoComputador = n - (m-1)
            jogadaDoComputador = n
            print(jogadaDoComputador)
        else:
            jogadaDoComputador = m
            print(jogadaDoComputador)

    n = jogadaDoComputador
    return n

    # jogadaDoComputador =
    # while m > cont:
    #     n = n - m
    #     if n % (m + 1) == 0:
    #         return m
    #     else:
    #         n = n + m
    #         m = m - 1
    #         cont = cont + 1

    # return m

    # while (n % (m+1) != 0) and (m > 0):
    #     if n % (m+1) == 0:
    #         jogadaDoComputador = n - (m-1)
    #         print(jogadaDoComputador)
    #         # if jogadaDoComputador == 0:
    #         #     jogadaDoComputador = jogadaDoComputador + 1
    #     else:
    #         if n < m:
    #             # jogadaDoComputador = n - (m-1)
    #             jogadaDoComputador = n
    #             # print(jogadaDoComputador)
    #         else:
    #             jogadaDoComputador = m
    #             # print(jogadaDoComputador)

    #     n = jogadaDoComputador
    #     return n


partida()
