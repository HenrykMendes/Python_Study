

entrada_numero = int(input ("Digite 1: "));
entrada_numero_dois = int (input('Digite 2: '));
entrada_numero_tres = int (input ('Digite 3: '));

if entrada_numero > entrada_numero_dois and entrada_numero >entrada_numero_tres:
    print ("Maior 1: "+str (entrada_numero))
elif entrada_numero_dois > entrada_numero_tres:
    print ('Maior 2: '+str (entrada_numero_dois))
else:
    print ('Maior 3: '+str (entrada_numero_tres))
