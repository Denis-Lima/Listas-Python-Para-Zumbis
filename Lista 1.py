n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
soma = n1 + n2
print (soma)



metros = float(input('Digite um valor em metros para converter em milímetros: '))
milímetros = metros * 1000
print (f'{metros} metros é igual a {milímetros} milímetros')



d = int(input('Informe um valor em dias: '))
h = int(input('Informe um valor em horas (inteiras): '))
m = int(input('Informe um valor em minutos: '))
s = int(input('Informe um valor em segundos: '))
dh = d * 24
horas = dh + h
hm = horas * 60
minutos = hm + m
ms = minutos * 60
segundos = ms + s
print (f'Todos os valores convertidos para segundos somam {segundos} segundos')



salário = float(input('Qual o seu salário?\n:'))
porcentagem = float(input('Qual é a porcentagem de aumento que receberá?(Apenas números)\n:'))
aumento = salário  * porcentagem/100
novo = salário + aumento
print (f'Você receberá um aumento de R${aumento:.2f} e seu novo salário é de R${novo:.2f}!')


preço = float(input('Qual o preço do produto?\n:'))
porcentagem = float(input('Qual o desconto do produto?(Apenas números)\n:'))
desconto = preço * porcentagem/100
pagar = preço - desconto
print(f'O desconto foi de R${desconto:.2f} e o preço a pagar ficou em R${pagar:.2f}')


dist = float(input('Qual a distância da viagem?(Em km)\n:'))
vel = float(input('Qual a velocidade média esperada para a viagem?(Em Km/H)\n:'))
horas = dist // vel
minutos = (dist % vel)/ vel * 60
print (f"A sua viagem irá durar aproximadamente {horas:.0f}h e {minutos:.0f}'")


C = float(input('Digite uma temperatura em Celsius para conversão: '))
F = 9*C/5 + 32
print (f'{C}ºC são {F}ºF')


F = float(input('Digite uma temperatura em Fahrenheit para conversão: '))
C = (F-32)*5/9
print (f'{F}ºF são {C}ºC')


km = float(input('Quantos quilômetros foram percorridos?\n:'))
d = float(input('Por quantos dias o carro foi alugado?\n:'))
p1 = 60 * d
p2 = 0.15 * km
preço = p1 + p2
print (f'O preço a pagar é de {preço:.2f} reais.')


cigarros = int(input('Quantos cigarros você fuma por dia?\n:'))
anos = int(input('Por quantos anos você têm fumado?\n'))
ad = anos * 365
qtd = cigarros * ad
minutos = 10 * qtd
redução = minutos / 60 / 24
print (f'Sua vida foi reduzida em {redução:.2f} dias por fumar')


digitos = 2 ** 1000000
contar = len(str(digitos))
print (f'2 elevado a 1 milhão tem {contar} dígitos!')
