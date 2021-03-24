temporada = {}
lista = []
numerogols = []
gols = 0
while True:
    temporada = {'nome': input('digite o nome: '), 'partidas': int(input('quantas partidas ele jogou?: '))}
    for g in range(temporada['partidas']):
        gols += int(input(f'quantos gols ele fez na °{g + 1} partida: '))
        numerogols.append(gols)
    lista.append(temporada)
    pergunta = input('quer continuar S/N?: ')
    if pergunta == 'N':
        break
temporada['gols'] = numerogols
print(lista)