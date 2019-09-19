nota = float(input('Insira uma nota entre 0 e 10: '))

while nota > 10 or nota < 0:
    print('Apenas entre 0 e 10!')
    nota = float(input('Nota: '))
print('Obrigado!')


user = str(input('Nome de usuário: '))
senha = str(input('Senha: '))

while user == senha:
    print('Erro: Usuário e senha não podem ser iguais!')
    user = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))
print('Obrigado!')


A = 80000
B = 200000
anos = 0

while A < B:
    A = A + A * 0.03
    B = B + B * 0.015
    anos = anos + 1
print(f'A população "A" vai passar a população "B" em {anos} anos')


n = int(input('Digite um número para saber sua sequência de Fibonacci: '))
f1 = 1
f2 = 1
x = 2

if n == 1 or n == 2:
    print(f'F{n} = {f1}')
while x != n:
    f1 = f1 + f2
    x = x + 1
    if x == n:
        print(f'F{n} = {f1}')
    if x != n:
        f2 = f1 + f2
        x = x + 1
        if x == n:
            print(f'F{n} = {f2}')



print('Digite dois números inteiros para saber seu máximo divisor comum')
n1 = int(input('N1: '))
n2 = int(input('N2: '))
r = n1 % n2
mdc1 = n1
mdc2 = n2

while r != 0:
    (mdc1, mdc2) = (mdc2, r)
    r = mdc1 % mdc2

print(f'O máximo divisor comum entre {n1} e {n2} é {mdc2}')
