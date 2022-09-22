import os

lembrete = list()
sair = False

while not sair:
    resposta = input('Fazer anotação? [s/n]').strip().lower()
    if resposta == 's':
        texto = input('Anotação: ')
        lembrete.append(texto)

    print('\n' + 'Anotações'.center(30, '='))
    # Layout do post-it
    for nota in lembrete:
        texto_tamanho = len(nota)
        lembrete_tamanho = texto_tamanho + 6
        print('-' * lembrete_tamanho)
        print(nota.center(lembrete_tamanho))
        print('-' * lembrete_tamanho)

    r = input('sair? [s/n]')
    if r == 's':
        sair = True
    os.system('cls' if os.name == 'nt' else 'clear')
