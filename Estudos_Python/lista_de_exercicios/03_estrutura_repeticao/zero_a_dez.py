while True:
    try: #try-exeption serve para caso existam possiveis erros na entrada de valores
        nota_do_aluno = float (input ('Digite: '))
        #da pra colcar duas condições no mesmo if sem usar o "&&"
        if 10<= nota_do_aluno <=10:
            print ('Nota valida')
        else:
            print ('Nota invalida')
    except ValueError:
        print ('Coloque um carctere numerico')
            
       
        
