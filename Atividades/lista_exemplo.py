# Esse programa imprime os elementos de uma lista (array ou vetor) em sua ordem inversa.

flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1