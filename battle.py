import pygame
from enum import Enum

# Definição dos estados das telas
Tela = Enum('Tela', 'INICIAL MAGOS ARENA BATALHA')
estado_tela = Tela.INICIAL

mago_escolhido = None
arena_batalha = None
magias1 = []

pygame.init()

def telainicial():
    largura, altura = 800, 500
    tela1 = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("TELA INICIAL")
    imagemfundo1 = pygame.image.load("img/FUNDO BATALHA.png")#Define o fundo da imagem inicial
    botaostart = pygame.image.load("img/start.png")     #imagem do botão start da tela inicial
    botao_rect = botaostart.get_rect()
    botao_rect.centerx = largura // 2
    botao_rect.centery = altura // 2 + 50

    while estado_tela == Tela.INICIAL:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(event.pos):
                    estado_tela = Tela.MAGOS

        tela1.blit(imagemfundo1, (0, 0))
        tela1.blit(botaostart, botao_rect)
        pygame.display.update()


def telamagos():
    global mago_escolhido, estado_tela
    
    largura, altura = 800, 500
    tela3 = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("TELA MAGOS")#nome da tela
    imagemfundo3 = pygame.image.load("img/ESCOLHAOMAGO.png")

    botaomagofogo = pygame.image.load("img/mago_fogo.jpg")
    botao_rect = botaomagofogo.get_rect()#rect do mago do fogo
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

    while estado_tela == Tela.MAGOS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(event.pos):
                    mago_escolhido = 'Fogo'
                    magias1 = ['Chamas Sombrias', 'Chamas Espirais Profundas', 'Estrela Incandescente']
                    estado_tela = Tela.ARENA

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect2.collidepoint(event.pos):
                    mago_escolhido = 'Agua'
                    magias1 = ['Projétil de Água Benta', 'Fúria da Serpente do Mar','Rugido do Dragão do Mar']
                    estado_tela = Tela.ARENA
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect3.collidepoint(event.pos):
                    mago_escolhido = 'Terra'
                    magias1 = ['Obstrução de Solo','Mãe-Terra Dividida','Solo Ascendente']
                    estado_tela = Tela.ARENA
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect4.collidepoint(event.pos):
                    mago_escolhido = 'Ar'
                    magias1 = ['Vento Cortante', 'Sopro do Dragão', 'Dança dos Ventos']
                    estado_tela = Tela.ARENA

        tela3.blit(imagemfundo3, (0, 0))
        tela3.blit(botaomagofogo, botao_rect)
        tela3.blit(botaomagoagua, botao_rect2)
        tela3.blit(botaomagoterra, botao_rect3)
        tela3.blit(botaomagoar, botao_rect4)
        pygame.display.update()

def carregar_imagem_mago(mago_escolhido):
    if mago_escolhido == 'Fogo':
        return pygame.image.load("img/mago_fogo.jpg")
    elif mago_escolhido == 'Agua':
        return pygame.image.load("img/mago_agua.jpg")
    elif mago_escolhido == 'Terra':
        return pygame.image.load("img/mago_terra.jpg")
    elif mago_escolhido == 'Ar':
        return pygame.image.load("img/mago_ar.png")
    else:
        # Tratar caso em que o mago escolhido não é válido
        raise ValueError("Mago escolhido inválido")
    

def desenhar_magias(tela, magias):
    x = 170
    y = 500 // 2 + 100
    espacamento = 40
    largura = 320
    altura = 50
    cor_texto = (255, 255, 255)
    fonte = pygame.font.Font(None, 30)

    # Carregar a imagem do botão
    imagem_botao = pygame.image.load("img/botao.png")
    imagem_botao = pygame.transform.scale(imagem_botao, (largura, altura))

    for magia in magias:
        # Desenhar a imagem do botão
        tela.blit(imagem_botao, (x, y))

        # Renderizar o texto da magia
        texto = fonte.render(magia, True, cor_texto)

        # Centralizar o texto no botão
        texto_retangulo = texto.get_rect(center=(x + largura // 2, y + altura // 2))

        # Desenhar o texto no botão
        tela.blit(texto, texto_retangulo)

        y += espacamento

    
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

    while estado_tela == Tela.ARENA:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arenafogo_rect.collidepoint(event.pos):
                    arena_batalha = pygame.image.load("img/TELAFUNDOFOGO.png")
                    estado_tela = Tela.BATALHA
                if arenaagua_rect2.collidepoint(event.pos):
                    arena_batalha = pygame.image.load("img/TELAFUNDOAGUA.png")
                    estado_tela = Tela.BATALHA
                if arenaterra_rect3.collidepoint(event.pos):
                    arena_batalha = pygame.image.load("img/FUNDOARENATERRA.png")
                    estado_tela = Tela.BATALHA
                if arenaar_rect4.collidepoint(event.pos):
                    arena_batalha = pygame.image.load("img/TELAFUNDOAR.png")
                    estado_tela = Tela.BATALHA
    tela4.blit(imagemfundo4, (0, 0))
    tela4.blit(arenamagofogo, arenafogo_rect)
    tela4.blit(arenamagoagua, arenaagua_rect2)
    tela4.blit(arenamagoterra, arenaterra_rect3)
    tela4.blit(arenamagoar, arenaar_rect4)
    pygame.display.update()

def batalha(arena):
    largura, altura = 800, 500
    tela5 = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("ARENA BATALHA") # nome da tela
    # Variáveis para controlar o movimento do mago
    mago_posicao_y = ((altura // 2) + 50)  # Posição inicial do mago
    mago_subindo = True  # Define se o mago está subindo ou descendo

    # Verificar o tipo de mago escolhido
    fonte = pygame.font.Font(None, 30)

    while estado_tela == Tela.BATALHA:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        tela5.blit(arena, (0, 0))  # Desenha a imagem da arena na tela

        # Atualiza a posição vertical do mago
        if mago_subindo:
            mago_posicao_y -= 1
            if mago_posicao_y <= ((altura // 2) - 50):  # Define a altura máxima do movimento de subida
                mago_subindo = False
        else:
            mago_posicao_y += 1
            if mago_posicao_y >= ((altura // 2) + 50):  # Define a altura máxima do movimento de descida
                mago_subindo = True

        tela5.blit(carregar_imagem_mago(mago_escolhido), (0, mago_posicao_y))  # Desenha o mago na posição atual

        if mago_escolhido:
            desenhar_magias(tela5, magias1)

        pygame.display.update()
        pygame.time.delay(10)  # Atraso de 10 milissegundos entre os quadros da animação

