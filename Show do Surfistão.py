def coloque(dic, name, coisa):
    dic[name] = coisa


def listar(um, dois, tres, quatro, cinco):
    global resultado
    global uma_lista
    lista = []
    lista.append(um)
    lista.append(dois)
    lista.append(tres)
    lista.append(quatro)
    lista.append(cinco)
    contador = 0
    contador += 1
    while contador != 1:
        uma_lista.append(lista)
        contador += 1
    print(uma_lista)
    print(lista)
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
    return lista
    return uma_lista







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
chave = ''
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
uma_lista = []
for c in range(5):
    print(uma_lista)
    outra_lista = listar(matematica['1°']['pergunta'], matematica['2°']['pergunta'], matematica['3°']['pergunta'], matematica['4°']['pergunta'], matematica['5°']['pergunta'])
    conferir(resultado)
    if resultado == 6:
        outra_lista.pop(0)
    if resultado == 'formula de Bhaskara':
        outra_lista.pop(1)
    if resultado == 48:
        outra_lista.pop(2)
    if resultado == 2001:
        outra_lista.pop(3)
    if resultado == 45:
        outra_lista.pop(4)