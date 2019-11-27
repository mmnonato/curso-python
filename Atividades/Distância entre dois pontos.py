import math

x1 = int(input("Informe x1: "))
x2 = int(input("Informe x2: "))
y1 = int(input("Informe y1: "))
y2 = int(input("Informe y2: "))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if d >= 10:
	print("longe")
else:
	print("perto")