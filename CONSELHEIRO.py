import random
from time import sleep

class conselheiro:
    def __init__(self):
        self.respostas = [
            'Com certeza, vai em frente!',
            'Não tenho certeza, acho que deve pensar melhor.',
            'Você não deveria fazer isso',
            'Essa é a hora certa!',
            'Vai mas não vai muito!',
            'PERIGO! Pare e Pense melhor!',
            'Nem sempre o caminho da razão é claro, pense de novo, acredito que você vai mudar de opinião',
            'Eu sabia que a primeira coisa que voc ia perguntar isa ser isso, a resposta é sim!!',
            'Olha Olha, to percebendo segundas intenções nesta sua pergunta, hum sei sei sei.',
            'As vezes você pergunta coisas das quais já sabe a resposta, Pensa de novo!',
            'Não podia perder a oportinidade de perguntar isso né? Mas a resposta é não.',
            'Adoro este tipo de pergunta! Vai fundo!',
            'Fora de questão nem ouse pensar nisso!',
            'Já vi que você é persistente nessas questões, vai lá então, vê no que vai dar!',
            'Ta ai uma coisa que você devia para de pensar.',
            'Pergunte ao seu coração, e vais envontrar a resposta verdadeira',
            'Peça este conselho para a pessoa que você mais ama e admira!',
            'Hahahahaha, capaz que tu não ia perguntar isso! Olha acho melhor espera um pouco.',
            'Se isso não prejudicar ninguém, que mal tem né?!',
            'Partiu!?',
            'Pelo ótica que estou vendo as coisas, não vejo problema.',
            'Pense: Isto é justo com todos os envolvidos?',
            'Coloca essa cabeça no lugar! E para de viajar!',
            'Olha isso parece ser uma coisa bem construtiva, aprovado!',
            'A principio acho melhor espera um pouco, mas não muito! kkkk',
            'Não se preocupa de não for agora, oportunidade não vai faltar.',
            'Primeira coisa: Se valoriza!, Segunda coisa: Ergue a cabeça e Terceira coisa: NÃO!',
            'Olha ta ai uma boa idéia!',
            'Eita! Já vi que isso ta te encomodando! Mas relaxa que na hora certa vai.',
            'Na minha visão, tem vezes que o melhor é esperar e observar.',
            'Claro e porque não, o que pode dar errado afinal?'
        ]


    def inicializar(self):
        input('Faça sua pergunta para que eu lhe aconselhe: ')
        print('Refletindo sobre sua pergunta...')
        sleep(2)
        print(random.choice(self.respostas))


    def continuar(self, decisao):
        while True:
            decisao.inicializar()
            continuar = input('Gostaria de receber mais de meus conselhos? [s/n] ').strip().lower()[0]
            if continuar == 's':
                continue
            elif continuar == 'n':
                break
            else:
                while continuar not in 'sn':
                    print('Resposta inválida! digites somente (s ou n)')
                    continuar = input('Gostaria de receber mais de meus conselhos? [s/n] ').strip().lower()[0]
                    if continuar == 'n':
                        break


aconselhador = conselheiro()
aconselhador.continuar(aconselhador)
print('Fim dos conselhos, volte quando precisar de mais!')