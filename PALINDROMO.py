
print('''PALÍNDROMO - O que é uma palavra ou frase palíndromo?
    Palíndromo, do grego palin (novo) e dromo (percurso), é toda palavra ou frase que pode ser lida de trás pra frente
e que, independente da direção, mantém o seu sentido. Também chamadas de anacíclicas, elas devem ser lidas
considerando-se apenas as letras.

-> Alguns exemplos de Palíndromo:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
A CARA RAJADA DA JARARACA
ADIAS A DATA DA SAIDA
A MAE TE AMA
A GRAMA E AMARGA
AME O POEMA
ATE O POETA
E ASSIM A MISSA E
O CEU SUECO
O MITO E OTIMO
OI RATO OTARIO
SECO DE RAIVA COLOCO NO COLO CAVIAR E DOCES\n''')

print('Vamos verificar se uma frase é um Palindromo.')
while True:
    print('=-=' * 20)
    frase = input('Digite uma frase: [sem acentos] ').strip().upper().replace(' ', '')
    frase_invertida = frase[::-1]
    print(f'O inverso de {frase} é {frase_invertida}')
    if frase == frase_invertida:
        print('Portanto temos um Palíndromo.')
    else:
        print('A frase digitada não é um Palíndromo!')
    print('=-=' * 20)
    continuar = input('Gostaria de ver se outra frase é um Palimdromo? [S/N] ').strip().upper()[0]
    while continuar not in 'NS':
        print('Ops!! Opção inválida! Digite somente [S/N] ', end=' ')
        continuar = input('Gostaria de ver se outra frase é um Plaíndromo? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 10, '  FIM DO PROGRAMA ', '=-' * 10)





















