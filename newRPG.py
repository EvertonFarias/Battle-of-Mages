#Grupo 01
#Batalha dos Magos
#Pedro Vinicius
#Gustavo Santos
#Kleverton Filipe
#Weslly Vitor
#Everton de Farias
import time
import sys
import random


##################################
#Classes:

class Magia:
    def __init__(self, magia, poder, custo_energia):
        self.magia = magia
        self.poder = poder
        self.custo_energia = custo_energia


class Mago:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.magias = []
        self.vivo = True
    
    def __str__(self):
        return self.nome
   
        



    def Defender(self, magias, mago_inimigo):
        poder_recebido = magias.poder / 2
        if poder_recebido > self.energia:
            poder_recebido = self.energia
        self.energia -= poder_recebido
        print(35*"-")
        print(f"{mago_inimigo} se defende da magia, perdendo {poder_recebido} pontos de energia.")
        print(f'{mago_inimigo} Tem agora {self.energia} de energia')
        print(35*"-")

        if self.energia <= 0:
            self.vivo = False
            print(f"{mago_inimigo} fica sem energia e morre!")


    
    def Atacar(self, magias, mago_alvo, classe):
        defender = random.randint(1, 10)
        if self.energia >= magias.custo_energia:
            print('qual habilidade deseja usar: ')
            self.magias_disponiveis(magias, classe)
            escolha = int(input('> '))
            while escolha <0 or escolha >2:
                escolha = int(input(f"Informe as habilidades com os números '0, 1 e 2' \n>:"))
            valor = self.magias[escolha]
            print(f'O Mago {self.nome} Usou A Magia {valor}')
            if defender >= 6:
                self.Defender(magias, mago_alvo)
                print(f'O mago {self.nome} tem agora {self.energia}')
            elif defender <=5:
                print(35*"-")
                print("Você não conseguiu se defender")
                print(35*"-")
        else:
            print(f'Voce Nao tem Energia o Suficiente para Usar Magias')


    def Aprender(self, magias,classe):
        self.magias.extend(magias)
        print_lento(f'{self.nome} Se tornou um Mago da Classe {classe}')
    

    def magias_disponiveis(self, magia, classe):
        print_lento(f'---------Mago {self.nome}---------\n'
            f'         classe {classe}\n'
            '------------------------\n'
            f'|   0 -  {self.magias[0]}\n'
            f'|    Custo - {magia.custo_energia} / Poder {magia.poder}\n\n'
            f'|    {self.magias[1]}\n'
            f'|   1 - Custo - {magia.custo_energia} / Poder {magia.poder}\n\n'
            f'|     {self.magias[2]}\n'
            f'|   2 - Custo - {magia.custo_energia} / Poder {magia.poder}\n\n'
            '------------------------', atraso=0.001)
    
    def HomeScreen(self):
        options = input("> ")
        if options.lower() == ("1"):
            print('Jogando')
        elif options.lower() == ("2"):
            sys.exit()

        while options.lower() not in ['1', '2']:
            print("Escolha uma opcao valida.")
            options = input("> ")
            if options.lower() == ("1"):
                print('Jogando')
            elif options.lower() == ("2"):
                sys.exit()



class Arena:
    def __init__(self, nome):
        self.nome = nome
    
    def Duelo(self, mago1, mago2): 
        print_lento(f"{mago1.nome} e {mago2.nome} entram na arena!", atraso=0.009)
        while mago1.vivo and mago2.vivo:
            mago1.Atacar(magia1, mago2, classe1)
            if mago2.vivo:
                mago2.Atacar(magia2, mago1, classe2)
        if mago1.vivo:
            print_lento(f"{mago1.nome} é o vencedor do Duelo!")
            self.vencedor = mago1
            return mago1
        else:
            print_lento(f"{mago2.nome} é o vencedor do Duelo!")
            self.vencedor = mago2
            return mago2

class Torneio:
    def __init__(self, nome_torneio, arena):
        self.nome_torneio = nome_torneio
        self.arena = arena
        self.magos_inscritos = []
        self.vencedor = None
    
    def inscrever_mago(self, *magos):
        for mago in magos:
            if mago not in self.magos_inscritos:
                self.magos_inscritos.append(mago)
                print_lento(f'{mago.nome} foi inscrito no torneio.')
            else:
                print_lento(f'{mago.nome} já está inscrito no torneio.')

    def Iniciar(self):
        print_lento(f'O torneio {self.nome_torneio} foi iniciado!')
        vencedores = list(self.magos_inscritos)  # Copia a lista de magos inscritos
        while len(vencedores) > 1:
            novos_vencedores = []
            for i in range(0, len(vencedores), 2):  # Itera de 2 em 2
                mago1 = vencedores[i]
                mago2 = vencedores[i + 1] if i + 1 < len(vencedores) else None
                if mago2:  # Se houver um segundo mago, faz o duelo
                    vencedor = self.arena.Duelo(mago1, mago2)
                    print_lento(f'O mago vencedor do duelo foi: {vencedor.nome}\n', atraso=0.07)
                    novos_vencedores.append(vencedor)
                else:  # Se for um número ímpar de magos, passa o último mago para a próxima rodada
                    novos_vencedores.append(mago1)
            vencedores = list(novos_vencedores)  # Atualiza a lista de vencedores para a próxima rodada
        if vencedores:
            self.vencedor = vencedores[0]  # O último vencedor é o vencedor do torneio
            print_lento(f'O mago vencedor do torneio {self.nome_torneio} foi: {self.vencedor.nome}\n')
        else:
            print_lento('Nenhum mago vencedor encontrado. O torneio não pode ser concluido')

###Def sleep
def print_lento(mensagem, atraso=0.04):
    for letra in mensagem:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    print()
################################################################################################
################################################################################################
################################### parte do input: ############################################
mag1 = input('Digite o nome do mago:\n>')

while mag1 == '':
    mag1 = input('Por Favor Digite o nome do mago:\n>')

print_lento('   ---Classes---\n   Mago da Terra\n   Mago da Agua \n   Mago do Fogo', atraso=0.01 )
classe1 = input('Digite a Classe que deseja ser:\n>')
if classe1.lower() in ["terra", "mago da terra"]:
    magias1 = ['Obstrução de Solo','Mãe-Terra Dividida','Solo Ascendente']
elif classe1.lower() in ("agua", "mago da agua"):
    magias1 = ['Projétil de Água Benta', 'Fúria da Serpente do Mar','Rugido do Dragão do Mar']
elif classe1.lower() in ("fogo", "mago do fogo"):
    magias1 = ['Bola de Fogo Mágica de Explosão Máxima', 'Chamas Espirais Profundas', 'Encarnação do Fogo do Inferno']

while classe1.lower() not in ['terra', 'agua', 'fogo','mago da terra', 'mago da agua', 'mago do fogo']:
    print("Escolha uma opcao valida.")
    classe1 = input("> ")
if classe1.lower() in ("terra", "Mago da Terra"):
    magias1 = ['Obstrução de Solo','Mãe-Terra Dividida','Solo Ascendente']
elif classe1.lower() in ("agua"):
    magias1 = ['Projétil de Água Benta', 'Fúria da Serpente do Mar','Rugido do Dragão do Mar']
elif classe1.lower() in ("fogo"):
    magias1 = ['Bola de Fogo Mágica de Explosão Máxima', 'Chamas Espirais Profundas', 'Encarnação do Fogo do Inferno']


mag2 = input('Digite o nome do outro mago:\n>')
while mag2 == '':
    mag2 = input('Por Favor Digite o nome do outro mago:\n>')
while mag2 == mag1:
    mag2 = input('Esse Mago Ja existe, Por favor Digite Outro nome:\n>')
    

print_lento('   ---Classes---\n   Mago da Terra\n   Mago da Agua \n   Mago do Fogo', atraso=0.01 )
classe2 = input('Digite a Classe que deseja ser:\n>')
if classe2.lower() in ("terra", "mago da terra"):
    magias2 = ['Obstrução de Solo','Mãe-Terra Dividida','Solo Ascendente']
elif classe2.lower() in ("agua", "mago da agua"):
    magias2 = ['Projétil de Água Benta', 'Fúria da Serpente do Mar','Rugido do Dragão do Mar']
elif classe2.lower() in ("fogo", "mago do fogo"):
    magias2 = ['Bola de Fogo Mágica de Explosão Máxima', 'Chamas Espirais Profundas', 'Encarnação do Fogo do Inferno']

while classe2.lower() not in ['terra', 'agua', 'fogo','mago da terra', 'mago da agua', 'mago do fogo']:
    print("Escolha uma opcao valida.")
    classe2 = input("> ")
if classe2.lower() in ("terra", "mago da terra"):
    magias2 = ['Obstrução de Solo','Mãe-Terra Dividida','Solo Ascendente']
elif classe2.lower() in ("agua", "mago da agua"):
    magias2 = ['Projétil de Água Benta', 'Fúria da Serpente do Mar','Rugido do Dragão do Mar']
elif classe2.lower() in ("fogo", "mago do fogo"):
    magias2 = ['Bola de Fogo Mágica de Explosão Máxima', 'Chamas Espirais Profundas', 'Encarnação do Fogo do Inferno']



#começando
mago1 = Mago(mag1)
magia1 = Magia(magias1, 20, 10)
mago2 = Mago(mag2)
magia2 = Magia(magias2, 20, 10)
mago1.Aprender(magias1, classe1)
mago2.Aprender(magias2, classe2)
torneio = Torneio("torneio do poder", Arena("fogo"))
torneio.inscrever_mago(mago2, mago1)
Torneio.Iniciar(torneio)


