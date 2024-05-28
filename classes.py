import pygame
import random




mage_player = None

class Mago: #classe responsável por armazenar a energia, se ta vivo ou morto e a classe do mago
    def __init__(self, classe_mago, nome):
        self.nome  = nome
        self.vida = 500
        self.vida_maxima = 500
        self.energia = 300
        self.energia_maxima = 300
        self.vivo = True
        self.classe = classe_mago
    
    def elemento():
        pass

class Magia:
    def __init__(self, nome, poder, custo_energia):
        self.nome = nome
        self.poder = poder
        self.custo_energia = custo_energia
        self.rect = None

def criar_magias(classe):#resposável por criar as instancias de Magia do mago
    magias_classe = []
    if classe == 'Fogo':
        magias_classe.append(Magia('Chamas Sombrias', 140, 40))
        magias_classe.append(Magia('Chamas Espirais Profundas', 40, 20))
        magias_classe.append(Magia('Estrela Incandescente', 20, 10))

    elif classe == 'Agua':
        magias_classe.append(Magia('Projétil de Água Benta', 70, 35))
        magias_classe.append(Magia('Fúria da Serpente do Mar', 40, 20))
        magias_classe.append(Magia('Rugido do Dragão do Mar', 20, 10))

    elif classe == 'Terra':
        magias_classe.append(Magia('Obstrução de Solo', 70, 35))
        magias_classe.append(Magia('Mãe-Terra Dividida', 40, 20))
        magias_classe.append(Magia('Solo Ascendente', 20, 10))

    elif classe == 'Ar':
        magias_classe.append(Magia('Vento Cortante', 70, 35))
        magias_classe.append(Magia('Sopro do Dragão', 40, 20))
        magias_classe.append(Magia('Dança dos Ventos', 20, 10))

    return magias_classe



pygame.init()

def telainicial():
    largura, altura = 800, 500
    tela1 = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("TELA INICIAL")
    imagemfundo1 = pygame.image.load("img/FUNDO BATALHA.png")#Define o fundo da imagem inicial
    botaostart = pygame.image.load("img/botao.png")     #imagem do botão start da tela inicial
    botao_rect = botaostart.get_rect()

    botaocreditos = pygame.image.load("img/botao.png")
    botaocreditos_rect = botaocreditos.get_rect()
    botaocreditos_rect.centerx = largura // 2
    botaocreditos_rect.centery = altura // 2 + 130
    botao_rect.centerx = largura // 2
    botao_rect.centery = altura // 2 + 50

    botaosobre = pygame.image.load("img/botao.png")
    botaosobre_rect = botaosobre.get_rect()
    botaosobre_rect.centerx = largura // 2
    botaosobre_rect.centery = altura // 2 + 210

    fonte = pygame.font.Font(None, 40)
    fonte.set_bold(True)
    texto1 = fonte.render("START", True, (255, 255, 255))
    texto2 = fonte.render("CRÉDITOS", True, (255, 255, 255))
    texto3 = fonte.render("SOBRE", True, (255, 255, 255))
    
    texto1_rect = texto1.get_rect(center=botao_rect.center)
    texto2_rect = texto2.get_rect(center=botaocreditos_rect.center)#SERVE PARA POSICIONAR O TEXTO NO CENTRO DO BOTÃO
    texto3_rect = texto3.get_rect(center=botaosobre_rect.center)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(event.pos):
                    telamagos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botaocreditos_rect.collidepoint(event.pos):
                    tela_creditos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botaosobre_rect.collidepoint(event.pos):
                    tela_sobre()

        tela1.blit(imagemfundo1, (0, 0))
        tela1.blit(botaostart, botao_rect)
        tela1.blit(botaocreditos, botaocreditos_rect )
        tela1.blit(botaosobre, botaosobre_rect )
        tela1.blit(texto1, texto1_rect)
        tela1.blit(texto2, texto2_rect)
        tela1.blit(texto3, texto3_rect)
        pygame.display.update()
        






def tela_creditos():
    largura, altura = 800, 500
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("TELA INICIAL")
    imagemcredito = pygame.image.load("img/CREDITOS.png")#Define o fundo da imagem inicial
    botao = pygame.image.load("img/botao.png")
    botao = pygame.transform.scale(botao, (120, 40))
    botao_rect = botao.get_rect()
    botao_rect.left = 0
    botao_rect.bottom = altura
    fonte = pygame.font.Font(None, 30)  
    texto = fonte.render("VOLTAR", True, (255, 255, 255))  
    texto_rect = texto.get_rect(center=botao_rect.center) #SERVE PARA POSICIONAR O TEXTO NO CENTRO DO BOTÃO, MÓ TRAMPO
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(event.pos):
                    telainicial()

        tela.blit(imagemcredito, (0,0) )
        tela.blit(botao, botao_rect)
        tela.blit(texto, texto_rect)  # DESENHA O TEXTO LÁ NO CENTRO DO BOTÃO, POR ISSO A VARIÁVEL
        
        pygame.display.update()

def tela_sobre():
    largura, altura = 800, 500
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("TELA INFO")
    imagemcredito = pygame.image.load("img/SOBRE.png")#Define o fundo da imagem inicial
    botao = pygame.image.load("img/botao.png")
    botao = pygame.transform.scale(botao, (120, 40))
    botao_rect = botao.get_rect()
    botao_rect.left = 0
    botao_rect.bottom = altura
    fonte = pygame.font.Font(None, 30)  
    texto = fonte.render("VOLTAR", True, (255, 255, 255))  
    texto_rect = texto.get_rect(center=botao_rect.center) #SERVE PARA POSICIONAR O TEXTO NO CENTRO DO BOTÃO, MÓ TRAMPO
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(event.pos):
                    telainicial()

        tela.blit(imagemcredito, (0,0) )
        tela.blit(botao, botao_rect)
        tela.blit(texto, texto_rect)  # DESENHA O TEXTO LÁ NO CENTRO DO BOTÃO, POR ISSO A VARIÁVEL
        
        pygame.display.update()



def telamagos():
    global escolha

    largura, altura = 800, 500
    tela3 = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("TELA MAGOS")
    imagemfundo3 = pygame.image.load("img/ESCOLHAOMAGO.png")

    botaomagofogo = pygame.image.load("img/mago_fogo.jpg")
    botao_rect = botaomagofogo.get_rect()
    botao_rect.centerx = 118
    botao_rect.centery = altura // 2 + 100

    botaomagoagua = pygame.image.load("img/mago_agua.jpg")
    botao_rect2 = botaomagoagua.get_rect()
    botao_rect2.centerx = 308
    botao_rect2.centery = altura // 2 + 100

    botaomagoterra = pygame.image.load("img/mago_terra.jpg")
    botao_rect3 = botaomagoterra.get_rect()
    botao_rect3.centerx = 498
    botao_rect3.centery = altura // 2 + 100

    botaomagoar = pygame.image.load("img/mago_ar.png")
    botao_rect4 = botaomagoar.get_rect()
    botao_rect4.centerx = 688
    botao_rect4.centery = altura // 2 + 100

    botao_voltar = pygame.image.load("img/botao.png")
    botao_voltar = pygame.transform.scale(botao_voltar, (120, 40))
    botao_voltar_rect = botao_voltar.get_rect()
    botao_voltar_rect.left = 10
    botao_voltar_rect.top = 10
    fonte = pygame.font.Font(None, 30)
    texto_voltar = fonte.render("VOLTAR", True, (255, 255, 255))
    texto_voltar_rect = texto_voltar.get_rect(center=botao_voltar_rect.center)

    while True:
        global magias1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(event.pos):
                    escolha = 'Fogo'
                    telaescolhaarena()
                if botao_rect2.collidepoint(event.pos):
                    escolha = 'Agua'
                    telaescolhaarena()
                if botao_rect3.collidepoint(event.pos):
                    escolha = 'Terra'
                    telaescolhaarena()
                if botao_rect4.collidepoint(event.pos):
                    escolha = 'Ar'
                    telaescolhaarena()
                if botao_voltar_rect.collidepoint(event.pos):
                    telainicial()

        tela3.blit(imagemfundo3, (0, 0))
        tela3.blit(botaomagofogo, botao_rect)
        tela3.blit(botaomagoagua, botao_rect2)
        tela3.blit(botaomagoterra, botao_rect3)
        tela3.blit(botaomagoar, botao_rect4)
        tela3.blit(botao_voltar, botao_voltar_rect)
        tela3.blit(texto_voltar, texto_voltar_rect)
        pygame.display.update()


        

def telaescolhaarena():
    largura, altura = 800, 500
    tela4 = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("TELA ESCOLHA ARENA")
    imagemfundo4 = pygame.image.load("img/TELAESCOLHAARENA.png")

    arenamagofogo = pygame.image.load("img/BOTAOFOGOMOLDURA.png")
    arenafogo_rect = arenamagofogo.get_rect()
    arenafogo_rect.centerx = 118
    arenafogo_rect.centery = altura // 2 - 20

    arenamagoagua = pygame.image.load("img/BOTAOAGUAMOLDURA.png")
    arenaagua_rect2 = arenamagoagua.get_rect()
    arenaagua_rect2.centerx = 280
    arenaagua_rect2.centery = altura // 2 + 160

    arenamagoterra = pygame.image.load("img/BOTAOTERRAMOLDURA.png")
    arenaterra_rect3 = arenamagoterra.get_rect()
    arenaterra_rect3.centerx = 520
    arenaterra_rect3.centery = altura // 2 + 160

    arenamagoar = pygame.image.load("img/BOTAOARMOLDURA.png")
    arenaar_rect4 = arenamagoar.get_rect()
    arenaar_rect4.centerx = 688
    arenaar_rect4.centery = altura // 2 - 20

    botao_voltar = pygame.image.load("img/botao.png")
    botao_voltar = pygame.transform.scale(botao_voltar, (120, 40))
    botao_voltar_rect = botao_voltar.get_rect()
    botao_voltar_rect.left = 10
    botao_voltar_rect.top = 10
    fonte = pygame.font.Font(None, 30)
    texto_voltar = fonte.render("VOLTAR", True, (255, 255, 255))
    texto_voltar_rect = texto_voltar.get_rect(center=botao_voltar_rect.center)

    while True:
        global arena_batalha
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arenafogo_rect.collidepoint(event.pos):
                    arena_batalha = pygame.image.load("img/TELAFUNDOFOGO.png")
                    batalha(arena_batalha)
                if arenaagua_rect2.collidepoint(event.pos):
                    arena_batalha = pygame.image.load("img/TELAFUNDOAGUA.png")
                    batalha(arena_batalha)
                if arenaterra_rect3.collidepoint(event.pos):
                    arena_batalha = pygame.image.load("img/FUNDOARENATERRA.png")
                    batalha(arena_batalha)
                if arenaar_rect4.collidepoint(event.pos):
                    arena_batalha = pygame.image.load("img/TELAFUNDOAR.png")
                    batalha(arena_batalha)
                if botao_voltar_rect.collidepoint(event.pos):
                    telamagos()

        tela4.blit(imagemfundo4, (0, 0))
        tela4.blit(arenamagofogo, arenafogo_rect)
        tela4.blit(arenamagoagua, arenaagua_rect2)
        tela4.blit(arenamagoterra, arenaterra_rect3)
        tela4.blit(arenamagoar, arenaar_rect4)
        tela4.blit(botao_voltar, botao_voltar_rect)
        tela4.blit(texto_voltar, texto_voltar_rect)
        pygame.display.update()





def carregar_imagem_mago(mago_escolhido):
    if mago_escolhido == 'Fogo':
        return pygame.image.load("img/magofogo.png")
    elif mago_escolhido == 'Agua':
        return pygame.image.load("img/magoagua.png")
    elif mago_escolhido == 'Terra':
        return pygame.image.load("img/magoterra.png")
    elif mago_escolhido == 'Ar':
        return pygame.image.load("img/magoar.png")
    else:
        pass


def desenhar_magias(tela, magias):
    x = 200
    y = 500 // 2 + 100
    espacamento = 40
    largura = 320
    altura = 50
    cor_texto = (255, 255, 255)
    fonte = pygame.font.Font(None, 30)

    for magia in magias:
        # Carregar a imagem do botão
        imagem_botao = pygame.image.load("img/botao.png")
        imagem_botao = pygame.transform.scale(imagem_botao, (largura, altura))

        # Desenhar a imagem do botão
        tela.blit(imagem_botao, (x, y))

        # Renderizar o texto da magia
        texto = fonte.render(magia.nome, True, cor_texto)  # Acessar o nome da magia usando magia.nome

        # Centralizar o texto no botão
        texto_retangulo = texto.get_rect(center=(x + largura // 2, y + altura // 2))

        # Desenhar o texto no botão
        tela.blit(texto, texto_retangulo)

        # Definir a área retangular do botão
        magia.rect = pygame.Rect(x, y, largura, altura)

        y += espacamento

def desenhar_vida_mana(tela, mago, x, y, largura_total, altura, espessura_borda):
    # Calcula a largura da barra de vida com base no valor atual da vida
    largura_vida = int((mago.vida / mago.vida_maxima) * (largura_total - espessura_borda * 2))

    # Calcula a largura da barra de mana com base no valor atual da mana
    largura_mana = int((mago.energia / mago.energia_maxima) * (largura_total - espessura_borda * 2))

    # Desenha a barra de vida vazia
    pygame.draw.rect(tela, (255, 255, 255), (x, y, largura_total, altura))

    # Desenha a borda da barra de vida
    pygame.draw.rect(tela, (0, 0, 0), (x, y, largura_total, altura), espessura_borda)

    # Desenha a barra de vida preenchida
    cor_vida = (0, 255, 0)  # Cor verde para indicar vida alta
    if mago.vida < mago.vida_maxima / 2:
        cor_vida = (255, 255, 0)  # Cor amarela para indicar vida média
    if mago.vida < mago.vida_maxima / 4:
        cor_vida = (255, 0, 0)  # Cor vermelha para indicar vida baixa
    pygame.draw.rect(tela, cor_vida, (x + espessura_borda, y + espessura_borda, largura_vida, altura - espessura_borda * 2))

    # Desenha a barra de mana vazia
    pygame.draw.rect(tela, (255, 255, 255), (x, y + altura + 10, largura_total, altura))

    # Desenha a borda da barra de mana
    pygame.draw.rect(tela, (0, 0, 0), (x, y + altura + 10, largura_total, altura), espessura_borda)

    # Desenha a barra de mana preenchida
    pygame.draw.rect(tela, (0, 0, 255), (x + espessura_borda, y + altura + 10 + espessura_borda, largura_mana, altura - espessura_borda * 2))

    # Exibe o valor da vida na barra de vida
    fonte = pygame.font.Font(None, 24)
    texto_vida = fonte.render(f"Vida: {mago.vida}/{mago.vida_maxima}", True, (255, 255, 255))
    tela.blit(texto_vida, (x, y - 20))

    # Exibe o valor da mana na barra de mana
    texto_mana = fonte.render(f"Mana: {mago.energia}/{mago.energia_maxima}", True, (255, 255, 255))
    tela.blit(texto_mana, (x, y + altura + 10 - 20))







def gerar_mago_inimigo(): 
    #Def responsável por pegar aleatóriamente uma classe para o mago_inimigo e criar uma instancia Mago e Magia
    global mago_inimigo, magias_inimigo, classe_inimigo
    classes = ['Fogo', 'Agua', 'Terra', 'Ar']
    classe_inimigo = random.choice(classes)#pega uma das 4 classes para o mago inimigo
    mago_inimigo = Mago(classe_inimigo, "Mago_inimigo")
    magias_inimigo = criar_magias(classe_inimigo)#criando e armazenando as magias do mago inimigo
    
    return mago_inimigo

def defesa(mago):
    if mago.nome =="player":
        return random.random() < 0.3 #SÓ 30% de chance de defesa
    else:
        return random.random() < 0.6# 60% para a IA

def atacar(mago, magia, tela):
    dano = magia.poder
    if defesa(mago):
        print(f"{mago.nome} se defendeu!")
        dano = magia.poder*0.5

    if dano >= mago.vida:
        mago.vida = 0
    else:
        mago.vida -= dano
        
    if mago.vida <= 0:
        mago.vivo = False
        print(f"{mago.nome} morreu")
        telainicial()

    if mago.energia <= 0:
        mago.vivo = False
        print(f"{mago.nome} morreu")
    return dano





def mostrar_dano(tela, danos):
    fonte = pygame.font.Font(None, 50)
    cor = (255, 0, 0, 255)
    danos_atualizados = []

    for dano in danos:
        valor, posicao_x, posicao_y, tempo = dano
        if pygame.time.get_ticks() - tempo < 1400:  # Exibir o dano por 1,4seg
            texto = fonte.render(f"-{valor} de HP", True, cor)
            tela.blit(texto, (posicao_x, 30))
            danos_atualizados.append(dano)

    return danos_atualizados


def batalha(arena):
    largura, altura = 800, 500
    tela5 = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("ARENA BATALHA")  # nome da tela
    mage_player = Mago(escolha, "player")
    magias_player = criar_magias(escolha)
    gerar_mago_inimigo()
    print(mago_inimigo.classe, mago_inimigo.energia)
    turno_mago_inimigo = False
    ultimo_turno = pygame.time.get_ticks()
    intervalo_turnos = 500

    for magia in magias_player:
        print(f"Nome: {magia.nome}")
    print(mage_player.vivo)
    print(mage_player.classe)

    # Variáveis para controlar o movimento do mago
    mago_posicao_y = ((altura // 2) - 70)  # Posição inicial do mago
    mago_subindo = True  # Define se o mago está subindo ou descendo
    barra_mana_y = mago_posicao_y - 40

    # Verificar o tipo de mago escolhido
    fonte = pygame.font.Font(None, 30)

    danos_jogador = []  # Lista para armazenar os danos causados pelo jogador
    danos_inimigo = []  # Lista para armazenar os danos causados pelo mago inimigo

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                tempo_atual = pygame.time.get_ticks()
                if tempo_atual - ultimo_turno >= intervalo_turnos:
                    if mage_player.vivo:
                        for magia in magias_player:
                            if magia.rect.collidepoint(event.pos):
                                print(f"Você usou: {magia.nome}\nCusto de mana: {magia.custo_energia}")
                                danoplayer = atacar(mago_inimigo, magia, tela5)
                                danos_jogador.append((danoplayer, 560, 300, pygame.time.get_ticks()))  # Adiciona o dano à lista
                                mage_player.energia -= magia.custo_energia

                                ultimo_turno = tempo_atual
                                turno_mago_inimigo = True
                                break

        if turno_mago_inimigo and mago_inimigo.vivo:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - ultimo_turno >= intervalo_turnos:
                magia_inimigo = random.choice(magias_inimigo)
                print(f"O Mago inimigo usou: {magia_inimigo.nome}\nCusto de mana: {magia_inimigo.custo_energia}")
                danoinimigo = atacar(mage_player, magia_inimigo, tela5)
                danos_inimigo.append((danoinimigo, 20, 300, pygame.time.get_ticks()))  # Adiciona o dano à lista
                mago_inimigo.energia -= magia_inimigo.custo_energia

                turno_mago_inimigo = False
                ultimo_turno = tempo_atual



        tela5.blit(arena, (0, 0))  # Desenha a imagem da arena na tela

        # Atualiza a posição vertical do mago
        if mago_subindo:
            mago_posicao_y -= 2
            if mago_posicao_y <= ((altura // 2) - 70):  # Define a altura máxima do movimento de subida
                mago_subindo = False
        else:
            mago_posicao_y += 2
            if mago_posicao_y >= ((altura // 2) + 20):  # Define a altura máxima do movimento de descida
                mago_subindo = True

        tela5.blit(carregar_imagem_mago(escolha), (-50, mago_posicao_y))  # Desenha o mago na posição atual
        tela5.blit(pygame.transform.flip(carregar_imagem_mago(classe_inimigo), True, False), (560, mago_posicao_y))  # Desenha o mago inimigo, o pygame.transform.flip é para inverter a imagem

        if escolha:
            desenhar_magias(tela5, magias_player)

        desenhar_vida_mana(tela5, mage_player, 20, mago_posicao_y - 40, 200, 20, 2)  # Barra de mana do personagem principal
        desenhar_vida_mana(tela5, mago_inimigo, tela5.get_width() - 20 - 200, mago_posicao_y - 40, 200, 20, 2)

        # Atualiza a exibição dos danos
        danos_jogador = mostrar_dano(tela5, danos_jogador)
        danos_inimigo = mostrar_dano(tela5, danos_inimigo)

        pygame.display.update()


telainicial()