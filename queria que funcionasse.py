import random
def perguntar(pergunta, resposta1, resposta2, resposta3):
    outra_resposta = input(f"""{pergunta}
a) {resposta1}
b) {resposta2}
c) {resposta3}
Qual é a resposta?: """)
    pontos = 0
    if outra_resposta == 'b' and pergunta == dic1['pergunta1']:
        pontos += 1
    if outra_resposta == 'c' and pergunta == dic2['pergunta2']:
        pontos += 1

    return pontos




dic1 = {'pergunta1': 'oq é utilizado para resolver as equações de segundo grau?: ', 'resposta1': 'formula de Richtter'
    , 'resposta1²': 'formula de Bhaskara', 'resposta1³': 'formula de Tesla'}
dic2 = {'pergunta2': 'qual é o valor da equação: 2x -b + 20; sendo x = 8 e b = 12', 'resposta2': 36, 'resposta2²': 22,
        'resposta2³': 24}
dic3 = {'pergunta3': 'quais são os elementos do teorema de Pitágoras?: ', 'resposta3': 'catetos e hipotenusa',
        'resposta3²': 'canetos e hipércia', 'resposta3³': 'altura e largura'}
resposta = input('Vamos começar o jogo?: ')
if resposta == 'sim':
    while True:
        antes_de_uma_resposta = input("""Escolha uma matéria:
        a) Matemática
        b) História
        c) Português
        d) Ciências
        Qual é a sua escolha?: """)
        if antes_de_uma_resposta == 'a':
            print('Vamos de matemática então!')
            uma_resposta = perguntar(dic1['pergunta1'], dic1['resposta1'], dic1['resposta1²'], dic1['resposta1³'])
            uma_resposta1 = perguntar(dic2['pergunta2'], dic2['resposta2'], dic2['resposta2²'], dic2['resposta2³'])
            uma_resposta2 = perguntar(dic3['pergunta3'], dic3['resposta3'], dic3['resposta3²'], dic3['resposta3³'])
        ahhhhhh = input('Quer continuar a jogar ou ficar com os pontos que vc já ganhou?: ')
        if ahhhhhh == 'não':
            break
print(f'Os pontos que você conquistou: {pontos}')