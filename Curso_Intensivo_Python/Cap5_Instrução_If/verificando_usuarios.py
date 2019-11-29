usuarios_atuais = ["pedro", "paulo", "josé", "antonio", "maria"]
novos_usuarios = ["joão", "Paulo", "marcos", "tiago", "MARIA"]

for novo_usuario in novos_usuarios:
    if novo_usuario.lower() in usuarios_atuais: # Para que a comparação não falhe, todos os nomes foram convertidos para letra minúscula (.lower()).
        print("O nome de usuário " + novo_usuario + " já está sendo utilizado, por favor, forneça outro nome.")
    else:
        print("O nome de usuário " + novo_usuario + " está disponível!")




