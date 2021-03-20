lista = []
while True:
    dicionario = {'nome': input('digite seu nome: '), 'idade': int(input('digite a sua idade: ')),
                  'sexo': input('M/F: ')}
    lista.append(dicionario)
    pergunta = input('quer continuar? ')
    if pergunta == 'não':
        break
velhinhos = []
media = 0
mulheres = []
for pessoas in lista:
    media += pessoas['idade']
for pessoas in lista:
    if pessoas['idade'] >= media / len(lista):
        velhinhos.append(pessoas['nome'])
    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
print(f'''Dados Gerais:
pessoas cadastradas: {lista}
acimas da média: {velhinhos}
mulheres: {mulheres}''')