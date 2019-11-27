k = 1
while k >= 0:
    k = int(input("Digite um número: "))
    if k < 0:
        print("Programa encerrado!")
    else:
        k_fat = 1
        cont = 1
        while cont < k:
            cont += 1       # o mesmo que cont = cont + 1
            k_fat *= cont   # o mesmo que k_fat = k_fat * cont
        print(k_fat)