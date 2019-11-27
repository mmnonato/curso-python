def remove_repetidos (lista): # Esta função remove os números repetidos de uma lista.
    lista2 = [] 
    for num in lista:
        if num in lista2:
            len(lista)
        else:
            lista2.append(num)
    lista2.sort()
    return lista2