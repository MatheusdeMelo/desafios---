temporada = {'nome':  input('digite o nome do jogador: ')}
partidas = int(input('digite o número de partidas: '))
numero_gols = []
contador_bala = 0
for c in range(partidas):
    numero_gols.append(int(input(f'qual foi o número de gols feito na °{c + 1} partida: ')))
for gols in numero_gols:
    contador_bala += gols
temporada['gols'] = contador_bala
temporada['numero de partidas'] = partidas
temporada['porcentagem'] = round(contador_bala / partidas, 2)
print(f'''Dados da temporada do {temporada['nome']}:
Ele jogou {temporada['numero de partidas']} partidas e nesse numero de partidas ele fez {temporada['gols']}
a média dele foi de {temporada['porcentagem']} gols por partida
''')

print(f'blah blah blah')
