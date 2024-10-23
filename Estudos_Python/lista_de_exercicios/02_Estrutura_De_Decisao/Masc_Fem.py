#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str (input('Qual seu sexo entre M e F: '))
#python: if - elif - else
#java: if - else if - else
if sexo == 'M':
    print ('Masculino')
elif sexo == 'F':
    print ('feminino')
else:
    print ('Gambiarra')