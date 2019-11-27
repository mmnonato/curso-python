# Este programa pede um número ao usuário e faz a soma dos números que o compõe. Por exemplo, caso o usuário forneça o número 123, o resultado da soma será 6, pois 1 + 2 + 3 = 6.

x = input("Digite um número: ") # Aqui o usuário informa o número
x_int = int(x) # O número é convertido de string para inteiro
y = x_int%10 # Aqui está o cálculo da variável inicial, que resulta no primeiro número à direita de x

while x_int > 0: # Enquanto x_int for menor do que 0, efetuar os cálculos abaixo
    x_int=x_int//10 # Atualiza o valor de x_int para pegar o segundo número à direito de x
    y=y+x_int%10 # Aqui é feita a soma do primeiro, segundo e n números de um número qualquer
print(y) # Escreve na tela o resultado da soma.
         