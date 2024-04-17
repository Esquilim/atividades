import math

print('Equação do 2º grau da forma: ax² + bx + c')
a = float(input('Coeficiente a: '))

if a == 0:
    print('Se a=0, não é uma equação do segundo grau. Tchau!')
else:
    b = float(input('Coeficiente b: '))
    c = float(input('Coeficiente c: '))

    delta = b * b - 4 * a * c

    if delta < 0:
        print('Delta menor que 0. A equação não possui raízes reais. Tchau!')
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'Delta=0, a equação possui apenas uma raiz real: {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'A equação possui duas raízes reais: {raiz1} e {raiz2}')