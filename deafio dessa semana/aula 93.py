dados_centrais = {'nome': input('Qual é seu nome?: '),'partidas': int(input('Quantas partidas vc jogou?: '))}
print(type(dados_centrais['partidas']))
golssssssssssssssss = []
total_de_gols = []
for c in range(dados_centrais['partidas']):
    golssssssssssssssss.append(int(input(f'na sua {c + 1}° vc fez quantos gols?: ')))
    dados_centrais['gols'] = golssssssssssssssss
for gols in dados_centrais['gols']:
    total_de_gols += gols
print(total_de_gols)