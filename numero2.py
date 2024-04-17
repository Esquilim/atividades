primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
terceiro = int(input('Terceiro número: '))


maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

print(f'O maior número é: {maior}')