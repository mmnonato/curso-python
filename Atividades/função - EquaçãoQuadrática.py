import math

def delta (a, b, c):
	return b ** 2 - 4 * a * c

def x1 (b, a):
	return (- b + math.sqrt(d)) / (2 * a)

def x2 (b, a):
	return (- b - math.sqrt(d)) / (2 * a)


a = float(input("Informe a letra A: "))
b = float(input("Informe a letra B: "))
c = float(input("Informa a letra C: "))

d = delta(a, b, c)

if d < 0:
	print("esta equação não possui raízes reais")
else:
	x1 = x1(b, a)
	x2 = x2(b, a)
if d == 0:
	print("a raiz desta equação é", x1)
elif d > 0:
	if x1 < x2:
		print("as raízes da equação são", x1, "e", x2)
	else:
		print("as raízes da equação são", x2, "e", x1)