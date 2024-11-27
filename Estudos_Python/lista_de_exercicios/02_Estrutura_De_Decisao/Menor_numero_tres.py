numero_de_entrada_um = int (input('Digite 1: '))
numero_de_entrada_dois = int (input ('Digite 2: '))
numero_de_entrada_tres = int (input ('Digite 3: '))

if numero_de_entrada_um < numero_de_entrada_dois and numero_de_entrada_um <numero_de_entrada_tres:
    print ('Número 01: '+str (numero_de_entrada_um))
elif numero_de_entrada_dois <numero_de_entrada_tres:
    print ('Número 02: '+ str (numero_de_entrada_dois))
else:
    print ('Número 03: ' + str (numero_de_entrada_tres))
    