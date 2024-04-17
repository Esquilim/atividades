l1 = float(input('Digite o tamanho do primeiro lado do triangulo '))
l2 = float(input('Digite o tamanho do segundo lado do triangulo '))
l3 = float(input('Digite o tamanho do terceiro lado do triangulo '))

if l1 + l2 > l3 or l1 + l3 > l2 or l2 + l3 > l1:
    if l1 == l2 and l2 == l3:
         print(' os lados formam um triangulo equilatero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('os lados formam um triangulo isosceles')
    else:
        print('os lados formam um triangulo escaleno')
else:
    print('os lados não formam um triangulo')