def cadastro(name, raça, peso):
    cadastrado = []
    cadastrado.append(name)
    cadastrado.append(raça)
    cadastrado.append(peso)
    return cadastrado





sistema = {}
cachorros = []
cats = []
print('Bom dia! Seja bem vindo ao Surf Petshop')
resposta = input('Posso lhe ajudar?: ')
while resposta != 'Não':
    cadastrar = input('Já tem cadastro?: ')
    c = 0
    if cadastrar == 'Não':
        c += 1
        outra_perg = input('É um gato ou um cachorro?: ')
        if outra_perg == 'Cachorro':
            p1 = cadastro(input('Qual é o nome dele?: '), input('Qual a raça dele?: '), input('Qual é o peso dele?: '))
            print('Cadastro feito!')
            cachorros.append(p1)
        if outra_perg == 'Gato':
            p2 = cadastro(input('Qual é o nome dele?: '), input('Qual é a cor dele?: '), input('Qual é o peso dele?: '))
            print('Cadastro feito!')
            cats.append(p2)
        quest = input('Mais alguma coisa?: ')
        if quest == 'Não':
            break
    if cadastrar == 'Sim':
        perg = input('Qual é o nome dele?: ')
        print(cachorros)
        if perg in p1 or perg in p2:
            print('Ok! pode deixa-lo conosco')
            break
        else:
            print('Não há nenhum agendamento, cadastre-o de novo!')
            break
sistema['cachorros'] = cachorros
sistema['gatos'] = cats
print(sistema)