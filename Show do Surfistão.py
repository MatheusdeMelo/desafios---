def coloque(dic, name, coisa):
    dic[name] = coisa


def listar(um, dois, tres, quatro, cinco):
    global resultado
    global lista
    lista = []
    lista.append(um)
    lista.append(dois)
    lista.append(tres)
    lista.append(quatro)
    lista.append(cinco)
    resultado = str(input(random.choice(lista)))
    if resultado == '6':
        lista.remove(um)
    if resultado == 'formula de Bhaskara':
        lista.remove(dois)
    if resultado == '48':
        lista.remove(tres)
    if resultado == '2001':
        lista.remove(quatro)
    if resultado == '45':
        lista.remove(cinco)






def conferir(a):
   respostas = []
   respostas.append(dict1['resp certa'])
   respostas.append(dict2['resp certa'])
   respostas.append(dict3['resp certa'])
   respostas.append(dict4['resp certa'])
   respostas.append(dict5['resp certa'])
   if resultado != respostas[1]:
    if int(resultado) in respostas:
        print('você acertou!!')
    else:
        print('você errou!!')
   if resultado == respostas[1]:
       if resultado in respostas:
           print('você acertou!!')
       else:
           print('você errou!!')


import random
resultado = ''
lista = []
dict1 = {'pergunta': 'raiz quadrada de 36: ', 'resp certa': 6, 'resp errada1': 18, 'resp errada2': 3}
dict2 = {'pergunta': 'qual é a regra utilizada pra resolver equações de 2°: ', 'resp certa': 'formula de Bhaskara','resp errada1': 'formula de Newton', 'resp errada2': 'teorema de Pitágoras'}
dict3 = {'pergunta': 'reposta de 22 + 3 x (2 x 5) - 4: ', 'resp certa': 48, 'resp errada1': 246, 'resp errada2': 72}
dict4 = {'pergunta': 'se Jesus morreu aos 33 anos, em 2034 vai fazer quantos anos que ele morreu?: ', 'resp certa': 2001, 'resp errada1': 2002, 'resp errada2': 2003}
dict5 = {'pergunta': 'se em cada 500 ml de café é colocado 3 cubos de açucar, em uma garrafa de 7,5 litros quantos cubos serão colocados?: ', 'resp certa': 45, 'resp errada1': 40, 'resp errada2': 15}
matematica = {}
coloque(matematica, '1°', dict1)
coloque(matematica, '2°', dict2)
coloque(matematica, '3°', dict3)
coloque(matematica, '4°', dict4)
coloque(matematica, '5°', dict5)
#lista = [matematica, geografia, historia, curiosidades, ciências]
for c in range(5):
    listar(matematica['1°']['pergunta'], matematica['2°']['pergunta'], matematica['3°']['pergunta'], matematica['4°']['pergunta'], matematica['5°']['pergunta'])
    conferir(resultado)
    print(resultado)
    print(lista)