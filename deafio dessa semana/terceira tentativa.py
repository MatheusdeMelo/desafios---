temporada = {}
lista = []
gols = 0
contador = 0
while True:
    temporada = {'nome': input('digite o nome: '), 'partidas': int(input('quantas partidas ele jogou?: ')), 'gols': []}
    for g in range(temporada['partidas']):
        gols += int(input(f'quantos gols ele fez na °{g + 1} partida: '))
    temporada['gols'].append(gols)
    lista.append(temporada)
    pergunta = input('quer continuar S/N?: ')
    contador += 1
    if pergunta == 'N':
        break
temporada['média'] = round(contador / temporada['partidas'], 2)
for c in range(contador):
    print(f"""Dados da Temporada:
nome: {temporada['nome'][c]}
partidas jogadas: {temporada['partidas'][c]}
gols: {temporada['gols']} com uma porcentagem de {temporada['média'][c]}
""")