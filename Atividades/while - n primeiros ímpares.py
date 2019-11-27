n = int(input("Digite o valor de n: "))
i = 0 
x = 0  

verifica = False

while not verifica:
	i = i + 1
	if i % 2 != 0:
		print(i)
	else:
		x = x + 1
		if x == n: 
			verifica = True