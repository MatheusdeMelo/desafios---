import random
def mostrar(uma_lista, resposta1, resposta2, resposta3):
    aleatorizando = random.choice(uma_lista)
    print(f"""{aleatorizando}
    
    a){resposta1}
    b){resposta2}
    c){resposta3}
    """)
    uma_resposta = input('Qual é a resposta?: ')
    pontos = 0
    if uma_resposta == 'b':
        pontos += 1
        print('Você acertou')
        print(f'até agora essa é sua pontuação: {pontos}')



dic1 = {'pergunta1': 'oq é utilizado para resolver as equações de segundo grau?: ', 'resposta1': 'formula de Richtter'
    , 'resposta1²': 'formula de Bhaskara', 'resposta1³': 'formula de Tesla'}
perguntas = []
perguntas.append(dic1['pergunta1'])
resposta = input('Vamos começar o jogo?: ')
if resposta == 'sim':
    print('simbora')
    mostrar(perguntas, dic1['resposta1'], dic1['resposta1²'], dic1['resposta1³'])