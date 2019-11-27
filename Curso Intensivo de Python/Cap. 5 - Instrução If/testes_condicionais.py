age = int(input('Qual sua idade? '))

if age < 4:
    preço = 0
elif age < 18:
    preço = 5
else:
    preço = 10

print("Sua entrada custa $" + str(preço) + ".")