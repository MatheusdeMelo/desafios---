def contador(inicio, fim, passo):
    tam = (fim - beg) + 1
    pedaço = []
    for c in range(tam):
        pedaço.append(beg+c)
    if passo <= 1:
        print(pedaço[inicio - 1:fim])
    else:
        print(pedaço[inicio - 1:fim:passo])


beg = int(input('qual será o inicio?: '))
end = int(input('qual será o fim?: '))
pas = int(input('qual será o passo?: '))
contador(beg, end, pas)