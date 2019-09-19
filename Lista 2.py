a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if a > (b + c) or b > (a + c) or c > (a + b):
    print('Não é triângulo')
elif a == b != c or b == c != a or a == c != b:
    print('É isósceles')
elif a == b == c:
    print('É equilátero')
else:
    print('É escaleno')


ano = int(input('Ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('É bissexto!')
else:
    print('Não é bissexto!')

'''from calendar import isleap
ano = int(input('Ano: '))

if isleap(ano) == True:
    print('É bissexto')
else:
    print('Não é bissexto')'''

peso = int(input('Peso: '))
valor = 4
excesso = peso - 50
if peso > 50:
    multa = valor * excesso
else:
    multa = 0
    excesso = 0

print(f'Excesso: {excesso}Kg')
print(f'Multa: R${multa:.2f}')

n1 = float(input('N1: '))
n2 = float(input('N2: '))
n3 = float(input('N3: '))

if n1 == n2 == n3:
    print('Digite números diferentes!')
else:
    if n1 >= n2 and n1 >= n3:
        maior = n1
    elif n2 >= n1 and n2 >= n3:
        maior = n2
    elif n3 >= n1 and n3 >= n2:
        maior = n3
    print(f'O maior deles é {maior}')

n1 = float(input('N1: '))
n2 = float(input('N2: '))
n3 = float(input('N3: '))

if n1 == n2 == n3:
    print('Digite 3 números diferentes')
else:
    if n1 >= n2 and n1 >= n3:
        ma = n1
    if n2 >= n1 and n2 >= n3:
        ma = n2
    if n3 >= n1 and n3 >= n2:
        ma = n3
    if n1 <= n2 and n1 <= n3:
        me = n1
    if n2 <= n1 and n2 <= n3:
        me = n2
    if n3 <= n1 and n3 <= n2:
        me = n3
    print(f'Maior: {ma}')
    print(f'Menor: {me}')

ganho = float(input('Ganho por hora: '))
horas = int(input('Horas trabalhadas no mês: '))
bruto = ganho * horas
IR = bruto * 0.11
INSS = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - IR - INSS - sind
print(f'''Salário bruto: R${bruto:.2f}
Imposto de Renda: R${IR:.2f}
INSS: R${INSS:.2f}
Sindicato: R${sind:.2f}
Salário líquido: R${liquido:.2f}''')

area = float(input('Área a ser pintada (m²): '))
'''1 litro pinta 3m², 1 lata (18litros) pinta 54m²'''

if area % 54 == 0:
    qtd = area / 54
else:
    qtd = area // 54 + 1
preço = qtd * 80
print(f'Quantidade de latas: {int(qtd)}')
print(f'Preço total: R${preço:.2f}')
