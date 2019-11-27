# Este programa pede ao usuário que forneça a idade e, em seguida, informa o valor da entrada.

age = int(input('Qual sua idade? '))

if age < 4:
    preço = 0
elif age < 18:
    preço = 5
else:
    preço = 10

print("Sua entrada custa $" + str(preço) + ".")