largura = int(input("digite a largura: "))
altura = int(input("digite o altura: "))
linha = 1
coluna = 1

while linha <= altura:
    if linha == 1 or linha == altura:
        while coluna <= largura:
            print("#", end = "")
            coluna = coluna + 1
        linha = linha + 1
        print()
        coluna = 1
    else:
        while linha < altura:
            while coluna <= largura:
                if coluna == 1 or coluna == largura:
                    print("#", end = "")
                    coluna = coluna + 1
                else:
                    print(" ", end = "")
                    coluna = coluna + 1
            linha = linha + 1
            print()
            coluna = 1