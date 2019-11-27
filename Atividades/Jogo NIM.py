def computador_escolhe_jogada (n, m):
    y = 0
    controle = False
    while y <= m or (not controle):
        if n == m:
            y = m
            return y
        if n < m:
            y = n
            return y
        if n % (m + 1) == 0:
            y = m
            controle = True
            return y 
        else:
            while (not controle):
                if n % (m + 1) == 0:
                    return y
                    controle = True
                else:
                    n = n - 1
                    y = y + 1
            else:
                if n == m:
                    y = m
                return y

def usuario_escolhe_jogada (n, m):
    x = 0
    terminou = False
    while (not terminou):
        x = int(input("Quantas peças você vai tirar? "))
        if x > 0 and x <= n and x <= m:
            return x
            terminou = True
        else:
            x > m or x <= 0 or x > n
            print("Oops! Jogada inválida! Tente de novo.")

def partida (): 
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    c = 0
    v = 0
    verifica = False
    if n % (m + 1) == 0:
        print("Você começa!")
        while (not verifica):
            if n == 0: 
                verifica = True
            else:
                x = usuario_escolhe_jogada(n, m)
                print("Você tirou ", x, "peça(s).")
                n = n - x
                print("Agora resta(m) ", n, "peça(s) no tabuleiro.")
                if n == 0:
                    print("Fim do jogo! Você ganhou!")
                    return False
                else:
                    y = computador_escolhe_jogada(n, m)
                    print("O computador tirou ", y, "peça(s).")
                    n = n - y
                    print("Agora resta(m) ", n, "peça(s) no tabuleiro.")
                    if n == 0:
                        print("Fim do jogo! O computador ganhou!")
                        return True
    else:
        print("Computador começa!")
        while (not verifica):
            if n == 0: 
                verifica = True
            else:
                y = computador_escolhe_jogada(n, m)
                print("O computador tirou ", y, "peça(s).")
                n = n - y
                print("Agora resta(m) ", n, "peça(s) no tabuleiro.")
                if n == 0:
                    print("Fim do jogo! O computador ganhou!")
                    return True
                else:
                    x = usuario_escolhe_jogada(n, m)
                    print("Você tirou ", x, "peça(s).")
                    n = n - x
                    print("Agora resta(m) ", n, "peça(s) no tabuleiro.")
                    if n == 0:
                        print("Fim do jogo! Você ganhou!")
                        return False

def campeonato ():
    c = 0
    v = 0
    print("**** Rodada 1 ****")
    rd1 = partida()
    if rd1 == True:
        c = c + 1
    else:
        v = v + 1
    print("**** Rodada 2 ****")
    rd2 = partida()
    if rd2 == True:
        c = c + 1
    else:
        v = v + 1
    print("**** Rodada 3 ****")
    rd3 = partida()
    if rd3 == True:
        c = c + 1
    else:
        v = v + 1
    print("**** Final do campeonato! ****")
    print("Placar: Você ", v, "X", c, "Computador")

def jogo ():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    j = int(input())
    if j == 1:
        partida()
    else:
        campeonato()

jogo()
