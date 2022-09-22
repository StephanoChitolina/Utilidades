from time import sleep
print('*-*' * 40)
print('''                                                 -=- I.M.C -=-
    IMC é a sigla para Índice de Massa Corporal,que é um cálculo que serve para avaliar se a pessoa está dentro do seu
peso ideal em relação à altura. Assim, de acordo com o valor do resultado de IMC, a pessoa pode saber se está dentro do
peso ideal, acima ou abaixo do peso desejado.

    Estar dentro do peso certo é importante porque estar acima ou abaixo desse peso pode influenciar bastante a saúde,
aumentando o risco de doenças, sendo assim, é comum os médicos, enfermeiros e nutricionistas avaliem o IMC da pessoa
nas consultas de rotina para verificar a possibilidade de doenças que a pessoa pode estar pré-disposta.
''')
sleep(6)

print('*-*' * 40)
print(' ' * 38, 'CALCULO DO INDICE DE MASSA CORPORAL')

continuar = True
while continuar == True:
    print('*-*' * 40)
    peso = float(input('Digite seu peso: (Kg) '))
    altura = float(input(f'Qual altura será informada para o peso de {peso}Kg? (m) '))
    imc = peso / (altura ** 2)
    print('CALCULANDO...')
    sleep(3)
    print('O resultado do I.M.C. para o peso {}Kg e altura de {}m é de {:.2f} Kg/m2\n'.format(peso, altura, imc))
    sleep(2)
    print('''>>> SIGNIFICADO DO RESULTADO DO I.M.C.:
    Cada resultado do IMC deve ser avaliado por um profissional de saúde. No entanto,de acordo com seu I.M.C,'será 
    apresentado uma pré-disposição a algum tipo de complicação, caso seu I.M.C estiver fora do ideal.(parâmetros de 
    acordo com a Organização Mundial da Saúde.)\n''')
    print('*-*' * 40)
    sleep(2)
    if imc <= 16.9:
        imc = 'MUITO ABAIXO DO PESO IDEAL'
        print(f'I.M.C Está {imc}, pode gerar:\nQueda de cabelo, infertilidade, ausência menstrual'
              f'\nFadiga, stress, ansiedade')
    elif 16.9 < imc < 18.4:
        imc = 'ABAIXO DO PESO'
        print(f'I.M.C Está {imc}, pode gerar:\nFadiga, stress, ansiedade')
    elif 18.4 < imc < 24.9:
        imc = 'PESO IDEIAL'
        print(f'I.M.C Está no {imc}:\nMenor risco de doenças cardíacas e vasculares, Parabéns!')
    elif 24.9 < imc < 29.9:
        imc = 'ACIMA DO PESO'
        print(f'I.M.C Está {imc}, pode gerar:\nFadiga, má circulação, varizes')
    elif 29.9 < imc < 34.9:
        imc = 'OBESIDADE GRAU I'
        print(f'I.M.C Está em {imc}, pode gerar:\nFadiga, má circulação, varizes'
              f'\nDiabetes, angina, infarto, aterosclerose')
    elif 34.9 < imc < 40:
        imc = 'OBESIDADE GRAU II'
        print(f'I.M.C Está em {imc}, pode gerar:\nFadiga, má circulação, varizes'
              f'\nDiabetes, angina, infarto, aterosclerose\nApneia do sono, falta de ar')
    elif imc >= 40:
        imc = 'OBESIDADE GRAU III'
        print(f'I.M.C Está em {imc}, pode gerar:\nFadiga, má circulação, varizes\nDiabetes, angina, infarto, aterosclerose'
              f'\nApneia do sono, falta de ar\nRefluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC')
    print('*-*' * 40)
    if imc == 'MUITO ABAIXO DO PESO IDEAL' or imc == 'ABAIXO DO PESO':
        sleep(2)
        print('''DICA:
        Se o resultado do IMC estiver abaixo do ideal, o que se deve fazer é aumentar a ingestão de alimentos ricos em 
    vitaminas e minerais de boa qualidade, mas sem cair no erro de comer alimentos processados e ricos em gordura trans.
    Pizzas, frituras, cachorro quente e hambúrguer não são os melhores alimentos para quem precisa aumentar o peso de 
    forma saudável, porque este tipo de gordura pode se acumular no interior das artérias, aumentando o risco de doença 
    cardíaca.''')
    if imc == 'PESO IDEIAL!':
        sleep(2)
        print('''A IMPORTÂNCIA DE ESTAR NO PESO IDEAL:
        É importante estar dentro do peso ideal porque o peso certo está intimamente ligado ao estado de saúde da 
    pessoa. Ter um pequeno acumulo de gordura no corpo é importante para que hajam reservas de energia para quando a 
    pessoa ficar doente ter tempo para se recuperar. No entanto, o excesso de gordura se acumula no fígado, na cintura 
    e também dentro das artérias dificultando a passagem do sangue, e isso aumenta o risco de doenças cardíacas.Por 
    isso, estar dentro do peso ideal é importante para aumentar a saúde, prevenindo doenças cardiovasculares e aumentar 
    a qualidade de vida. Assim, quem está abaixo do peso deve aumentar o volume muscular para aumentar de peso de forma 
    saudável e quem está acima do peso, deve queimar gordura para ganhar saúde.''')
    if imc == 'ACIMA DO PESO' or imc == 'OBESIDADE GRAU I' or imc == 'OBESIDADE GRAU II' or imc == 'OBESIDADE GRAU III':
        sleep(2)
        print('''DICA:
        Se o resultado do IMC estiver acima do ideal e a pessoa não for muito musculosa, nem atleta, pode indicar que é 
    preciso emagrecer, eliminando o acúmulo de gordura, que contribui para o peso alto. Para isso deve-se comer somente 
    alimentos ricos em vitaminas e minerais, tendo o cuidado de diminuir o consumo de alimentos industrializados e ricos 
    em gordura, como massa folheada, bolos, biscoitos recheados e salgadinhos, por exemplo.Para que os resultados sejam 
    alcançados ainda mais rápido é aconselhado fazer exercícios para aumentar o gasto calórico e aumentar o metabolismo. 
    Recorrer a chás e suplementos naturais pode ser um estímulo para ajudar a emagrecer de forma mais rápida e saudável, 
    sem ter que passar fome. Alguns exemplos são o chá de hibisco ou o chá de gengibre com canela, mas um nutricionista 
    poderá indicar outros que sejam mais adequados às necessidades de cada pessoa''')
    sleep(5)
    print()
    resposta_usuario = input('Gostaria de verificar outro I.M.C? [S/N] '.strip())
    print()
    while resposta_usuario not in 'Ss':
        if resposta_usuario in 'Nn':
            continuar = False
            print('*-*' * 40)
            print(' ' * 46, 'FIM DO PROGRAMA')
            break
        else:
            print('Digite uma resposta válida, apenas [S/N]! ', end=' ')
            resposta_usuario = input('Gostaria de verificar outro I.M.C? [S/N] '.strip())
            print()
