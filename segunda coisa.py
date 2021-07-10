def dio(nome, pergunta, resposta1, resposta2, resposta3):
    global contador
    contador += 1
    nome = {f'perg{contador}': pergunta, f'resp{contador}': resposta1, f'resp1{contador}': resposta2, f'resp2{contador}': resposta3}
    return nome
def perguntar(dicionário):
    global pontuação
    outra_resposta = input(f"""{dicionário[f'perg{contador}']}
a) {dicionário[f'resp{contador}']}
b) {dicionário[f'resp1{contador}']}
c) {dicionário[f'resp2{contador}']}
Qual é a resposta?: """)
    if outra_resposta == 'a' and {dicionário[f'resp{contador}']}:
        print('você acertou!')
        pontuação += 1
    total = pontuação
    print(pontuação)
    return pontuação




contador = 0
pontuação = 0
rod1 = dio('mat1', 'quais são os elementos do teorema de Pitágoras?: ', 'catetos e hipotenusa', 'canetos e hipércia',
           'altura e largura')
resposta_certa = []
resposta_certa.append(rod1[f'resp{contador}'])
perguntar(rod1)
perguntar(rod1)
print(rod1)
print(resposta_certa)