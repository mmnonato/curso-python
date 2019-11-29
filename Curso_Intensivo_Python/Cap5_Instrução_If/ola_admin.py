usuarios = ["marcos", "paulo", "admin", "pedro", "silvia"]

if usuarios: # verifica se a lista tem pelo menos um item e, se tiver, faz o comando, senão dá a msg do else.
    for usuario in usuarios:
        if usuario == "admin":
            print("Olá admin, gostaria de ver um relatório de status?")
        else:
            print("Olá " + usuario + ", obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar alguns usuários!")

