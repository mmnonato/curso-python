idade = int(input("Informe a idade: "))

if idade < 2:
    pessoa = "bebê"
elif idade < 4:
    pessoa = "criança"
elif idade < 13:
    pessoa = "garoto"
elif idade < 20:
    pessoa = "adolescente"
elif idade < 65:
    pessoa = "adulto"
elif idade >= 65:
    pessoa = "idoso"

print("Essa pessoa é um(a)", pessoa + ".")