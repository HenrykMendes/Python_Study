#Faça um programa que leia um nome de usuário e a sua senha e não aceite 
# a senha igual ao nome do usuário, mostrando 
# uma mensagem de erro e voltando a pedir as informações.

while True:

        usuario = input ("Nome:");
        senha = input ("Senha: ");
        
        if usuario == senha:
            print ("Senha e nome não podem ser os mesmo")
        else:
            print ("Cadastrado!");
