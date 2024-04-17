primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
terceiro = int(input('Terceiro número: '))

maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro


menor = primeiro
if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')