n = int(input("Digite o número: ")) 
x = 1 # variável que vai diminuir de n na fórmula fatorial
nf = n # valor inicial do fatorial
verifica = False # indicador de passagem

while not verifica and x < n: # enquanto verifica for verdadeiro e o x menor que n, fazer os comandos abaixo
    nf = nf * (n - x) # fórmula fatorial
    if x >= n: # se o x for maior ou igual a n, considere verifica como verdadeiro
        verifica = True
    else: # caso contrário, execute a expressão abaixo
        x = x + 1
print(nf) # quando o while tiver uma de suas expressões falsas, o programa deve imprimir o resultado de nf