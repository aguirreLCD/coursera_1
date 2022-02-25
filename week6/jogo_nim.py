def inicia_jogo():
    print('')
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('')
    print('1 - para jogar uma partida isolada')

    partidaOuCampeonato = int(input("2 - para jogar um campeonato "))

    if partidaOuCampeonato == 1:
        print('')
        print("Voce escolheu uma partida!")
        partida()
    if partidaOuCampeonato == 2:
        print('')
        print("Voce escolheu um campeonato!")
        campeonato()


def campeonato():
    indexPartida = 1

    placar_pc_campeonato = 0

    while indexPartida < 4:
        print("")
        print(f"**** Rodada ", indexPartida, " ****")
        print("")
        [m, n, placar_pc1] = partida()
        placar_pc_campeonato = placar_pc_campeonato + placar_pc1
        indexPartida += 1

    print("")
    print('**** Final do campeonato! ****')
    print("")
    print('Placar: Você ', 0, ' X', placar_pc_campeonato, ' Computador')
    print("")


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if m > n:
        while m > n:
            m = int(input("Limite de peças por jogada? "))
    placar_pc = int(0)

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
            if user_play == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou", user_play, "peças.")
            n = n - user_play

            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.")
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")

            usuarioJogando = False
        else:
            print()
            pc_play = computador_escolhe_jogada(n, m)
            if pc_play == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", pc_play, "peças.")
            n = n - pc_play

            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.")
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")

            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                placar_pc = int(1)

            else:
                usuarioJogando = True

    return n, m, placar_pc


def usuario_escolhe_jogada(n, m):
    print()
    jogadaDoUsuario = int(input("Quantas peças você vai tirar? "))

    if (jogadaDoUsuario > m) or (jogadaDoUsuario <= 0) or (jogadaDoUsuario > n):
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        jogadaDoUsuario = int(input("Quantas peças você vai tirar? "))
        print("")
    n = jogadaDoUsuario
    return n


def computador_escolhe_jogada(n, m):
    jogadaPc = 1

    while jogadaPc <= m and (n-jogadaPc) % (m+1) != 0:
        jogadaPc = jogadaPc + 1

    if jogadaPc > m:
        n = jogadaPc-1
    else:
        n = jogadaPc

    return n


inicia_jogo()
