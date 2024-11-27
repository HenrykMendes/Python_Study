

entrada_numero = int(input ("Digite 1: "));
entrada_numero_dois = int (input('Digite 2: '));
entrada_numero_tres = int (input ('Digite 3: '));


todos_numero = [entrada_numero, entrada_numero_dois, entrada_numero_tres]

todos_numero.sort(reverse=True)

for num in todos_numero:
    print (num)