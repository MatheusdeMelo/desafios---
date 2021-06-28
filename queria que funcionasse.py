import random
def mostrar(uma_lista, resposta1, resposta2, resposta3):
    aleatorizando = random.choice(uma_lista)
    resposta_certa = []
    resposta_certa.append(dic1['resposta1²'])
    pontos = 0
    if resposta2 in resposta_certa and uma_resposta == 'b':
        pontos += 1
        print('Você acertou')
        print(f'até agora essa é sua pontuação: {pontos}')
    else:
        print('Você errou')
        print(f'até agora essa é sua pontuação: {pontos}')
    total = 0
    total += pontos
    return total



dic1 = {'pergunta1': 'oq é utilizado para resolver as equações de segundo grau?: ', 'resposta1': 'formula de Richtter'
    , 'resposta1²': 'formula de Bhaskara', 'resposta1³': 'formula de Tesla'}
perguntas = []
perguntas.append(dic1['pergunta1'])
resposta = input('Vamos começar o jogo?: ')
antes_de_uma_resposta = input("""Escolha uma matéria:
a) Matemática
b) História
c) Português
d) Ciências""")
if antes_de_uma_resposta == 'a':
    uma_resposta = mostrar(perguntas)
while True:
    if resposta == 'sim':
        print('vamos simbora')
        mostrar(perguntas, dic1['resposta1'], dic1['resposta1²'], dic1['resposta1³'])
        outra_resposta = input('Quer continuar jogando?: ')
        if outra_resposta == 'não':
            break
print(f'Essa é sua pontuação final: {total}')