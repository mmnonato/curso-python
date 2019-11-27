def fatorial (y):
	yf = 1
	cont = 1
	while cont < y:
		cont = cont + 1     
		yf = yf * cont  
	return yf


n = int(input("Digite o valor de n: "))
p = int(input("Digite o valor de p: "))

cb = fatorial(n) / (fatorial(p) * fatorial(n - p))

print(cb)
