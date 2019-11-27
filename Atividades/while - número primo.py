n = int(input("Digite um número inteiro: "))
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
    print("primo")
else:
    print("não primo")