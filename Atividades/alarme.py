h = input("Informe a hora atual: ")
a = input("Informe o número de horas a esperar antes de tocar o alarme: ")
t = int(h)+(int(a)%12)
print("O alarme irá tocar às", t, "horas")