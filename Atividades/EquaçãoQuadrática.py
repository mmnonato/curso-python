# Relembrando, esse programa vai receber como entrada três valores, o a, b e c, que são as constantes ali da equação de segundo grau e daí você vai usando a fórmula de Bhaskara, imprimir as raízes, sendo que tem três casos se delta é menor que zero você vai dizer que não tem raízes reais, se delta igual a zero você vai dizer que tem uma raiz real que é tal, se delta for maior que zero, você vai dizer que tem duasraízes reais que são: tal e tal.

import math
a = float(input("Informe a letra A: "))
b = float(input("Informe a letra B: "))
c = float(input("Informa a letra C: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
	print("esta equação não possui raízes reais")

else:
	x1 = (- b + math.sqrt(delta)) / (2 * a)
	x2 = (- b - math.sqrt(delta)) / (2 * a)
	if delta == 0:
		print("a raiz desta equação é", x1)
	if delta > 0:
		if x1 < x2:
			print("as raízes da equação são", x1, "e", x2)
		else:
			print("as raízes da equação são", x2, "e", x1)