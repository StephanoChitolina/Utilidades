from time import sleep

print('''    O SISTEMA BINÁRIO, ou de base 2 é um sistema de numeração posicional em que todas as quantidades se 
representam com base em dois números, ou seja, zero e um (0 e 1).

    Os computadores digitais trabalham internamente com dois níveis de tensão, pelo que o seu sistema de numeração
natural é o sistema binário. Com efeito, num sistema simples como este é possível simplificar o cálculo, com o auxílio 
da lógica booliana. Em computação, chama-se um dígito binário (0 ou 1) de bit, que vem do inglês Binary Digit.
Um agrupamento de 8 bits corresponde a um byte (Binary Term).\n''')

sleep(10)
print('''    O SISTEMA OCTAL, é um sistema de numeração cuja base é 8, ou seja, utiliza 8 símbolos para a representação 
de quantidade. No ocidente, estes símbolos são os algarismos arábicos.

    O octal foi muito utilizado em informática como uma alternativa mais compacta ao binário na programação em linguagem
de máquina. Hoje, o sistema hexadecimal é mais utilizado como alternativa ao binário. Este sistema também é um sistema
posicional e a posição de seus algarismos determinada em relação à vírgula decimal. Caso isso não ocorra, supõe-se
implicitamente colocada à direita do número.\n''')

sleep(10)
print('''   O SISTEMA HEXADECIMAL, de numeração muito utilizado na programação de microprocessadores, em especial nos
equipamentos e máquinas de estudo e sistemas de desenvolvimento. Trata-se de um sistema de numeração posicional que
representa os números em base 16, sendo assim, utilizando 16 símbolos. Este sistema utiliza os símbolos
0, 1, 2, 3, 4, 5, 6, 7, 8 e 9 do sistema decimal, além das letras A, B, C, D, E e F.

    A nomenclatura "hexadecimal" é usada devido aos termos "hexa" que significa "6" e "deci" que representa "10",
portanto indicando a base 16. Cada número hexa significa quatro bits de dados binários. Um byte é criado por 8 bits e
é representado por dois dígitos hexa. Já um word possui 16 bits e pode ser representado por quatro dígitos hexa. Um
duplo word, dword, possui 32 bits e é representado por oito dígitos hexa. A grande vantagem de utilizar o sistema
hexadecimal torna-se clara à medida que os números vão se tornando maiores.
    Este sistema é muito utilizado para demonstrar números binários de uma forma mais compacta, visto ser muito mais
fácil converter hexadecimal em binários e vice-versa.\n''')

print('CONVERSÃO DE UM NÚMERO INTEIRO PARA: BINÁRIO, OCTAL OU HEXADECIMAL:')
print(('=-=' * 15))

numero = int(input('Digite um número inteiro: '))
opcao = ''
while opcao != 5:
    print('Escolha uma das bases para conversão:\n'
          '[ 1 ] converter para BINÁRIO\n'
          '[ 2 ] converter para OCTAL\n'
          '[ 3 ] converter para HEXADECIMAL\n'
          '[ 4 ] escolher outro número\n'
          '[ 5 ] encerrar programa')
    opcao = int(input('Digite a opção escolhida: '))
    sleep(1)
    print('~' * 54)
    if opcao == 1:
        binario = bin(numero)
        print(f'{numero} convertido para BINÁRIO é igual a {binario[2:]}')
        print('~' * 54)
        sleep(2)
    elif opcao == 2:
        octal = oct(numero)
        print(f'{numero} convertido para OCTAL é igual a {octal[2:]}')
        print('~' * 54)
        sleep(2)
    elif opcao == 3:
        hexadecimal = hex(numero)
        print(f'{numero} convertido para HEXADECIMAL é igual a {hexadecimal[2:]}')
        print('~' * 54)
        sleep(2)
    elif opcao == 4:
        numero = int(input('Digite um novo número inteiro: '))
        print('~' * 54)
        sleep(2)
    elif opcao == 5:
        print((' ' * 16), 'PROGRAMA ENCERRADO')
        print('~' * 54)
        sleep(2)
        break
    else:
        print('Opção inválida! Opções disponíveis: 1, 2, 3, 4 ou 5')
        print('~' * 54)








