import random
def perguntar(uma_lista, resposta1, resposta2, resposta3):
    aleatorizando = random.choice(uma_lista)
    uma_lista.remove(aleatorizando)
    outra_resposta = input(f"""{aleatorizando}
a) {resposta1}
b) {resposta2}
c) {resposta3}
Qual é a resposta?: """)
    pontos = 0
    if outra_resposta == 'b' and aleatorizando == dic1['pergunta1']:
        pontos += 1
    if outra_resposta == 'c' and aleatorizando == dic2['pergunta2']:
        pontos += 1
    return uma_lista
    return pontos




dic1 = {'pergunta1': 'oq é utilizado para resolver as equações de segundo grau?: ', 'resposta1': 'formula de Richtter'
    , 'resposta1²': 'formula de Bhaskara', 'resposta1³': 'formula de Tesla'}
dic2 = {'pergunta2': 'qual é o valor da equação: 2x -b + 20; sendo x = 8 e b = 12', 'resposta2': 36, 'resposta2²': 22,
        'resposta2³': 24}
perguntas = []
perguntas.append(dic1['pergunta1'])
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
            uma_resposta = perguntar(perguntas, dic1['resposta1'], dic1['resposta1²'], dic1['resposta1³'])
            uma_resposta1 = perguntar(perguntas, dic2['resposta2'], dic2['resposta2²'], dic2['resposta2³'])
