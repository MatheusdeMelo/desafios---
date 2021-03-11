dados = {}
nome = []
sexo = []
idade = []
contador = 0
pergunta = ''
while True:
    nome.append(input('digite seu nome: '))
    sexo.append(input('M/F: '))
    idade.append(int(input('digite sua idade: ')))
    pergunta = input('mais alguem?: ')
    if pergunta == 'não':
        break
    contador += 1
dados['pessoa'] = nome, idade
print(dados['pessoa'])
mediaaa = 0
for idades in idade:
    mediaaa += idades
dados['média'] = round(mediaaa / contador, 2)
velhos = []
for nomes in dados['pessoa']:
    print(nome)
    print(idades)
print(dados)