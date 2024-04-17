insert_1 = float(input('Digite o primeiro numero: '))
insert_2 = float(input('Digite o segundo numero: '))

dividir = float(insert_1 + insert_2)
soma = dividir / 2

if(soma < 3):
    print('O aluno não conseguiu ser aprovado no ano letivo.')
    print('Resultado do aluno: {}'.format(soma))
elif(soma < 5):
    print('Você está de recuperação.')
    print('Resultado do aluno: {}'.format(soma).split(2, None))  
elif(soma > 6):
    print('O aluno está aprovado.')
    print('Resultado do aluno: {}'.format(soma))
else:
    print('Não foi possivel validar a nota do aluno.')        