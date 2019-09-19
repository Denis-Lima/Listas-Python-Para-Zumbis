from random import randint
lista = []
for n in range(10):
    lista.append(randint(1, 100))
maior = lista[0]
menor = lista[0]
for a in range(10):
    if maior <= lista[a]:
        maior = lista[a]
    if menor >= lista[a]:
        menor = lista[a]
        
print(f'''Lista: {lista}
maior: {maior}
menor: {menor}''')


from random import randint
lista = []
for n in range(20):
    lista.append(randint(1, 100))
par = []
impar = []

for a in range(20):
    if lista[a] % 2 == 0:
        par.append(lista[a])
    if lista[a] % 2 != 0:
        impar.append(lista[a])
print(f'''Lista: {lista}
Par: {par}
Impar: {impar}''')


from random import randint
vetor1, vetor2, vetor3 = [], [], []
for n in range(10):
    vetor1.append(randint(1, 100))
    vetor2.append(randint(1, 100))
for a in range(10):
    vetor3.append(vetor1[a])
    vetor3.append(vetor2[a])
print(f'''Vetor 1: {vetor1}
Vetor 2: {vetor2}
Vetor 3: {vetor3}''')


texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone.
Our community is based on mutual respect, tolerance, and
encouragement, and we are working to help each other live up to
these principles. We want our community to be more diverse:
whoever you are, and whatever your background, we welcome you.'''
texto = texto.lower()
texto = texto.replace(',', ' ').replace('.', ' ').replace(':', ' ')
texto = texto.split()
lista = []
for x in range(len(texto) - 1):
    if texto[x][0] in 'python' or texto[x][-1] in 'python':   
        lista.append(texto[x])
print (f'Lista de palavras que tenham "python" no início ou fim: {lista}')


texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone.
Our community is based on mutual respect, tolerance, and
encouragement, and we are working to help each other live up to
these principles. We want our community to be more diverse:
whoever you are, and whatever your background, we welcome you.'''
texto = texto.lower()
texto = texto.replace(',', ' ').replace('.', ' ').replace(':', ' ')
texto = texto.split()
lista = []
def pyt(palavra):
  for letra in palavra:
    if letra in 'python':
      return True
  return False
for x in texto:
    if pyt(x) and len(x) > 4:
        lista.append(x)
print(f'Lista de palavras com mais de 4 letras que tenham "python": {lista}')
print(len(lista), 'palavras no total')
