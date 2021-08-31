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
    if antes_de_uma_resposta == 'c':
        if outra_resposta == 'c' and pergunta == port1['pergunta1']:
            os_pontos += 1
        elif outra_resposta == 'a' and pergunta == port2['pergunta2']:
            os_pontos += 1
        elif outra_resposta == 'b' and pergunta == port3['pergunta3']:
            os_pontos += 1
        elif outra_resposta == 'c' and pergunta == port4['pergunta4']:
            os_pontos += 1
        elif outra_resposta == 'c' and pergunta == port5['pergunta5']:
            os_pontos += 1
    if antes_de_uma_resposta == 'd':
        if outra_resposta == 'b' and pergunta == cie1['pergunta1']:
                os_pontos += 1
        elif outra_resposta == 'b' and pergunta == cie2['pergunta2']:
                os_pontos += 1
        elif outra_resposta == 'c' and pergunta == cie3['pergunta3']:
                os_pontos += 1
        elif outra_resposta == 'a' and pergunta == cie4['pergunta4']:
                os_pontos += 1
        elif outra_resposta == 'c' and pergunta == cie5['pergunta5']:
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
port1 = {'pergunta1': 'quais desses se encaixam nos adjuntos adnominais?: ', 'resposta1': 'substantivo',
         'resposta1²': 'verbos', 'resposta1³': 'adjetivo'}
port2 = {'pergunta2': 'na frase: Maria vai jogar võlei hoje. O termo "Maria" se encaixa em?: ', 'resposta2': 'sujeito',
         'resposta2²': 'predicado verbal', 'resposta2³': 'predicado nominal'}
port3 = {'pergunta3': 'o "é" se encaixa em qual alternativa?: ', 'resposta3': 'verbo transitivo',
         'resposta3²': 'verbo de ligação', 'resposta3³': 'advérbio'}
port4 = {'pergunta4': 'qual dessas alternativas tem um substantivo composto?: ',
         'resposta4': 'João vai a igreja amanhã', 'resposta4²': 'Uma tsunami aconteceu no Japão em 2011',
         'resposta4³': 'Eu e ela vamos hoje'}
port5 = {'pergunta5': 'para a frase: "Augusto vai ____ hoje?". Qual seria a resposta certa?: ', 'resposta5': 'viaja',
         'resposta5²': 'viajando', 'resposta5³': 'viajar'}
cie1 = {'pergunta1': 'Qual dessas alternativas não é o nome de uma árvore?:', 'resposta1': 'Pata de Vaca',
        'resposta1²': 'Cabeça de Jegue', 'resposta1³': 'Ipê-branco'}
cie2 = {'pergunta2': 'O que não está errado?:', 'resposta2': 'Os mamíferos tem sangue frio',
        'resposta2²': 'Os mamíferos são os animais que mamam', 'resposta2³': 'Os mamíferos incluem as cobras'}
cie3 = {'pergunta3': 'Quais desses nomes cíentificos não esxistem?:' , 'resposta3' : 'Sphyrna lewini',
        'resposta3²': 'Gorilla gorilla gorilla', 'resposta3³': 'Baleia baleia baleia'}
cie4 = {'pergunta4': 'Qual desses materias tem uma maior densidade (g/cm³)?:', 'resposta4': 'Cobre',
        'resposta4²': 'Diamante', 'resposta4³': 'Madeira'}
cie5 = {'pergunta5': 'Qual desses animais possuem a mordida mais forte?:', 'resposta5': 'Tubarão',
        'resposta5²': 'Crocodilo', 'resposta5³': 'T-rex'}
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
        if antes_de_uma_resposta == 'c':
            print('Vamos de português então!')
            port_resposta = perguntar(port1['pergunta1'], port1['resposta1'], port1['resposta1²'], port1['resposta1³'])
            port_resposta1 = perguntar(port2['pergunta2'], port2['resposta2'], port2['resposta2²'], port2['resposta2³'])
            port_resposta2 = perguntar(port3['pergunta3'], port3['resposta3'], port3['resposta3²'], port3['resposta3³'])
            port_resposta3 = perguntar(port4['pergunta4'], port4['resposta4'], port4['resposta4²'], port4['resposta4³'])
            port_resposta4 = perguntar(port5['pergunta5'], port5['resposta5'], port5['resposta5²'], port5['resposta5³'])
        if antes_de_uma_resposta == 'd':
            print('Vamos de ciência então!')
            cie_resposta = perguntar(cie1['pergunta1'], cie1['resposta1'], cie1['resposta1²'], cie1['resposta1³'])
            cie_resposta1 = perguntar(cie2['pergunta2'], cie2['resposta2'], cie2['resposta2²'], cie2['resposta2³'])
            cie_resposta2 = perguntar(cie3['pergunta3'], cie3['resposta3'], cie3['resposta3²'], cie3['resposta3³'])
            cie_resposta3 = perguntar(cie4['pergunta4'], cie4['resposta4'], cie4['resposta4²'], cie4['resposta4³'])
            cie_resposta4 = perguntar(cie5['pergunta5'], cie5['resposta5'], cie5['resposta5²'], cie5['resposta5³'])
        ahhhhhh = input('Quer continuar a jogar ou ficar com os pontos que vc já ganhou?: ')
        if ahhhhhh == 'não':
            break
print(f'Os pontos que você conquistou: {cie_resposta4}; e esse é o valor que você acumulou: R${cie_resposta4*500}')