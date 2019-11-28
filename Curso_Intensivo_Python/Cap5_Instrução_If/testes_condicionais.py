# Este programa pede ao usuário que forneça a idade e, em seguida, informa o valor da entrada.

age = int(input('Qual sua idade? '))

if age < 4:
    preço = 0
elif age < 18:
    preço = 5
elif age < 65:
    preço = 10
elif age >= 65:   # A partir daqui somente pessoas com 65 anos ou mais pagará $5.
    preço = 5     
#else:            # O bloco else poderia ser substituído por elif age >= 65, sem prejuízo.
    #preço = 5    

print("Sua entrada custa $" + str(preço) + ".")