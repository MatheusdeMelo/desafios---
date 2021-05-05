def coloque(dic, name, coisa):
    dic[name] = coisa
import random
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
print(matematica)
amor = input('qual??')