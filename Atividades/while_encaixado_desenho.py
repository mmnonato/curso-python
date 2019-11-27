largura = int(input("digite a largura: "))
altura = int(input("digite o altura: "))
linha = 1
coluna = 1

while linha <= altura:
    while coluna <= largura:
        print("#", end = "")
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1