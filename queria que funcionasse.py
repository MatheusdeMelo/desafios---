import random
def perguntar(pergunta, resposta1, resposta2, resposta3):
    global os_pontos
    outra_resposta = input(f"""{pergunta}
a) {resposta1}
b) {resposta2}
c) {resposta3}
Qual é a resposta?: """)
    pontos = 0
    if antes_de_uma_resposta == 'a':
        if outra_resposta == 'b' and pergunta == mat1['pergunta1']:
            os_pontos += 1
        elif outra_resposta == 'c' and pergunta == mat2['pergunta2']:
            os_pontos += 1
        elif outra_resposta == 'a' and pergunta == mat3['pergunta3']:
            os_pontos += 1
        elif outra_resposta == 'a' and pergunta == mat4['pergunta4']:
            os_pontos += 1
        elif outra_resposta == 'c' and pergunta == mat5['pergunta5']:
            os_pontos += 1
    if antes_de_uma_resposta == 'b':
        if outra_resposta == 'a' and pergunta == hist1['pergunta1']:
            os_pontos += 1
        elif outra_resposta == 'b' and pergunta == hist2['pergunta2']:
            os_pontos += 1
        elif outra_resposta == 'c' and pergunta == hist3['pergunta3']:
            os_pontos += 1
        elif outra_resposta == 'b' and pergunta == hist4['pergunta4']:
            os_pontos += 1
        elif outra_resposta == 'a' and pergunta == hist5['pergunta5']:
            os_pontos += 1
    pontos = os_pontos
    print(pontos)
    return pontos




mat1 = {'pergunta1': 'oq é utilizado para resolver as equações de segundo grau?: ', 'resposta1': 'formula de Richtter'
    , 'resposta1²': 'formula de Bhaskara', 'resposta1³': 'formula de Tesla'}
mat2 = {'pergunta2': 'qual é o valor da equação: 2x -b + 20; sendo x = 8 e b = 12', 'resposta2': 36, 'resposta2²': 22,
        'resposta2³': 24}
mat3 = {'pergunta3': 'quais são os elementos do teorema de Pitágoras?: ', 'resposta3': 'catetos e hipotenusa',
        'resposta3²': 'canetos e hipércia', 'resposta3³': 'altura e largura'}
mat4 = {'pergunta4': 'qual é o número adquirido ao dividirmos o comprimento da circunferência com o diâmetro?: ',
        'resposta4': 'π', 'resposta4²': '2r', 'resposta4³': '3,33333333333333...'}
mat5 = {'pergunta5': 'que número é maior?: ', 'resposta5': -26, 'resposta5²': -120, 'resposta5³': -3}
hist1 = {'pergunta1': 'quem foi o primeiro ministro britânico que atuou na 2° guerra mundial?: ',
         'resposta1': 'Winston Churchill', 'resposta1²': 'Anthony Eden', 'resposta1³': 'George Bush'}
hist2 = {'pergunta2': 'quais desses países estavam do lado dos EUA na guerra fria?: ', 'resposta2': 'China',
         'resposta2²': 'Canada', 'resposta2³': 'Alemanha Oriental'}
hist3 = {'pergunta3': 'quais desses ditadores causaram mais mortes?: ', 'resposta3': 'Josef Stalin',
         'resposta3²': 'Hugo Chávez', 'resposta3³': 'Mao Tse-tsung'}
hist4 = {'pergunta4': 'qual é a maior base da sociedade ocidental?: ', 'resposta4': 'O marxicismo',
         'resposta4²': 'O cristianismo', 'resposta4³': 'O populismo'}
hist5 = {'pergunta5': 'quem foi a pessoa que comandou para a vitória, na maior parte do tempo, os aliados na guerra do Paraguai?:',
         'resposta5': 'Duque de Caixias', 'resposta5²': 'Tiradentes', 'resposta5³': 'Gastão de Orleans'}
os_pontos = 0
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
            mat_resposta = perguntar(mat1['pergunta1'], mat1['resposta1'], mat1['resposta1²'], mat1['resposta1³'])
            mat_resposta1 = perguntar(mat2['pergunta2'], mat2['resposta2'], mat2['resposta2²'], mat2['resposta2³'])
            mat_resposta2 = perguntar(mat3['pergunta3'], mat3['resposta3'], mat3['resposta3²'], mat3['resposta3³'])
            mat_resposta3 = perguntar(mat4['pergunta4'], mat4['resposta4'], mat4['resposta4²'], mat4['resposta4³'])
            mat_resposta4 = perguntar(mat5['pergunta5'], mat5['resposta5'], mat5['resposta5²'], mat5['resposta5³'])
        if antes_de_uma_resposta == 'b':
            print('Vamos de história então!')
            hist_resposta = perguntar(hist1['pergunta1'], hist1['resposta1'], hist1['resposta1²'], hist1['resposta1³'])
            hist_resposta1 = perguntar(hist2['pergunta2'], hist2['resposta2'], hist2['resposta2²'], hist2['resposta2³'])
            hist_resposta2 = perguntar(hist3['pergunta3'], hist3['resposta3'], hist3['resposta3²'], hist3['resposta3³'])
            hist_resposta3 = perguntar(hist4['pergunta4'], hist4['resposta4'], hist4['resposta4²'], hist4['resposta4³'])
            hist_resposta4 = perguntar(hist5['pergunta5'], hist5['resposta5'], hist5['resposta5²'], hist5['resposta5³'])
        ahhhhhh = input('Quer continuar a jogar ou ficar com os pontos que vc já ganhou?: ')
        if ahhhhhh == 'não':
            break
print(f'Os pontos que você conquistou: {hist_resposta4}; e esse é o valor que você acumulou: R${hist_resposta4*500}')