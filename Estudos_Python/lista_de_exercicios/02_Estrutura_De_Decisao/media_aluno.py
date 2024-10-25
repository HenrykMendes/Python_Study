#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota = int (input('Nota 01: '))
nota_2 = int (input('Nota 02: '))
media_ponderada = int (input('Média: '))
nota_final = (nota + nota_2) /2

if nota_final > media_ponderada:
    print (f"Parabéns! Sua nota foi de {nota_final} em nossa média {media_ponderada}")
elif nota_final == 10:
    print('Parabéns! Sua nota foi perfeita!')
else:
    print ('Reprovado')