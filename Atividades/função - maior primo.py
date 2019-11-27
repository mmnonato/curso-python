def nprimo (n):
    controle = False
    p = 0
    i = 0

    while i <= n:
        i = i + 1
        if i > n:
            controle = True
        else:
            if n % i == 0:
                p = p + 1

    if p == 2:
        return "primo"

def maior_primo(n):
    s = 0
    k = 0
    
    while s < n:
        s = s + 1
        if nprimo(s) == "primo":
            k = s
    
    return k
		