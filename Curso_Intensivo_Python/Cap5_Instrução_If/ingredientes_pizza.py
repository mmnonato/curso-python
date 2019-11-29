ingredientes_disponiveis = ["cogumelo", "azeitona", "pimentão", "pepperoni", "abacaxi", "queijo extra"]
ingredientes_solicitados = ["cogumelo", "batata frita", "queijo extra"]

for ingrediente_solicitado in ingredientes_solicitados:
    if ingrediente_solicitado in ingredientes_disponiveis:
        print("Adicionando " + ingrediente_solicitado + ".")
    else:
        print("Desculpe, nós não temos " + ingrediente_solicitado + ".")

print("\nAcabei de fazer sua pizza!")