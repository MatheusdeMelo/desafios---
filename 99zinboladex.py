def maior(numero):
    grande = 0
    for numeros in numero:
        if numeros > grande:
            grande = numeros
    print(f"""Dados gerais:
    os números digitados foram: {numero}
    o maior número foi: {grande}
    """)


lista = []
while True:
   númerais = int(input('digite um número: '))
   lista.append(númerais)
   resposta = input('quer digitar outro número?: ')
   if resposta == 'não':
       break
maior(lista)