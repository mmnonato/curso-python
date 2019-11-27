num = int(input("Digite um número: ")) # O usuário informa o número
ant = num % 10 # Variável define o primeiro número à direita
num = num // 10 # Reduz o número original para que seja possível "captar" o segundo número à direita
i = 0 # contador de repetição

verifica = False # indicador de passagem é falso, pois ainda não sabemos dos números adjacentes

while num > 0 and not verifica: 
	prox = num % 10 # Variável define o primeiro número à direita
	if prox == ant: # comparação
		verifica = True # se verdade, "verifica" passa a ter novo valor
	else:
		i = i + 1 # contador
	ant = prox # atribui o valor de prox a ant
	num = num // 10 # reduz mais uma vez o valor de num para que seja possível "captar" o segundo número à direita
if verifica:
	print("sim") # quando verifica for True dentro do while imprime na tela sim
else:
	print("não") # quando o num for menor do que 0 (por não encontrar números adjacentes), a condição do while deixa de ser verdadeira e então imprime na tela não