
primeira_compra = float(input ('Digite01: '));
segunda_compra = float(input ('Digite02: '));
terceira_compra = float(input('Digite03: '));

if primeira_compra > segunda_compra and primeira_compra > terceira_compra:
    print ("Caixa de ovo: R$"+str(primeira_compra))
elif segunda_compra > terceira_compra:
    print ('Salame: R$'+str(segunda_compra))
else:
    print ('Carne do sol: R$'+str(terceira_compra))