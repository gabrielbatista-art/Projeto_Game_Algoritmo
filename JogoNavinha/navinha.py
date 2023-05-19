import sys,pygame #Importa os módulos referentes ao sistema do computador e pygame
from random import randint
import utilitarios
from Jogador import Jogador as player #Importa o jogador como player
from Inimigo import Inimigo as enemy #Importa o inimigo como enemy
from Tiro import Tiro
# from StartGame import start_screen
from defscore import desenhar_pontos

def jogoNavinha():
    pygame.init() #Inicializa os módulos do pygame

    #VARIÁVEIS GERAIS ---------------------------------------------------------------------
    #Tela
    larguraTela, alturaTela = utilitarios.resolucaoX, utilitarios.resolucaoY #Define a resolução do jogo
    tela = pygame.display.set_mode((larguraTela, alturaTela)) #Define a janela onde o jogo irá rodar.
    pygame.display.set_caption(utilitarios.tituloGame) #Define o título da janela.

    #Gameplay
    Clock = pygame.time.Clock()
    fps = 60 #Define a quantidade de quadros por segundo que o jogo roda

    pontos : int = 0


    #ENTIDADES ----------------------------------------------------------------------------
    #Fundo
    imagemFundo = pygame.image.load("Sprites/Fundo.png")
    imagemFundo = pygame.transform.scale(imagemFundo, (larguraTela, alturaTela)) #Ajusta a imagem de fundo para o tamanho da tela

    #Player
    naveJogador = pygame.image.load("Sprites/Player/player1.png") #Sprite player
    velocidadePlayer = 10

    #Inimigos
    navesInimigos = ["Sprites/Inimigo_Olhao.png", "Sprites/Inimigo_Caveirinha.png"]
    naveInimigo1 = pygame.image.load(navesInimigos[randint(0, 1)]) #Sprite Inimigo
    velocidadeInimigo = 5

    #Tiro
    tiroSprite = pygame.image.load("Sprites/Tiro.png")
    ultimoTiro = pygame.time.get_ticks() #Essa variável guarda o momento em que o ultimo tiro foi lançado
    cadencia = 200 #É a cadência de tiro em milissegundos
    velocidadeTiro = 15

    fogo = pygame.image.load("Sprites/turbina.gif")

    #INSTANCIAR ENTIDADES ------------------------------------------------------------------
    todasSprites = pygame.sprite.Group() #Inicia o grupo onde vão todas as sprites
    inimigos = pygame.sprite.Group() #Inicia o grupo para armazenar inimigos
    lasers = pygame.sprite.Group()

    #JOGADOR
    jogador = player(naveJogador, velocidade = velocidadePlayer, vida = 3, tela = (larguraTela, alturaTela)) #Instancia o jogador
    todasSprites.add(jogador) #Adiciona o jogador as grupo de todas as sprites



    #INIMIGOS
    for c in range(5):
        naveInimigo1 = pygame.image.load(navesInimigos[randint(0, 1)]) #Sprite Inimigo
        inimigo = enemy(naveInimigo1, velocidade = velocidadeInimigo, tela = (larguraTela, alturaTela)) #Instancia o inimigo, a gente coloca um for pra instanciar vários dps
        todasSprites.add(inimigo) #Adiciona o inimigo ao grupo de todas as sprites
        inimigos.add(inimigo) #Adiciona o inimigo ao grupo dos inimigos p conferir a colisão c o player depois

    # start_screen(imagemFundo, tela)

    while True:
        Clock.tick(fps) #Define a quantidade de quadros em que o jogo roda
        tela.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(pontos)
                pygame.quit()
                sys.exit()

        todasSprites.draw(tela)
        todasSprites.update() #Esse método atualiza todos os objetos dentro do grupo

        #Verifica o momento em que o tiro foi lançado
        tiroMomento = pygame.time.get_ticks()

        tecla = pygame.key.get_pressed() #Observa as teclas que são apertadas a cada frame
        if tecla[pygame.K_SPACE] and tiroMomento - ultimoTiro > cadencia:
            laser = Tiro(tiroSprite, velocidadeTiro, 10, (larguraTela, alturaTela))
            laser.rect.midtop = jogador.rect.midtop
            laser.rect.bottom = jogador.rect.top
            todasSprites.add(laser)
            lasers.add(laser)
            ultimoTiro = tiroMomento
        if tecla[pygame.K_p]:
            break

        colisaoTiro = pygame.sprite.groupcollide(inimigos, lasers, False, False)
        colisaoLaser = pygame.sprite.groupcollide(lasers, inimigos, False, False)
        if colisaoTiro:
            if colisaoLaser:
                lasers.remove(colisaoLaser)
                todasSprites.remove(colisaoLaser)
            inimigos.remove(colisaoTiro)
            todasSprites.remove(colisaoTiro)
            pontos += 1

        colisao = pygame.sprite.spritecollide(jogador, inimigos, False) #Confere se há colisão entre o player e os inimigos e retorna True ou False
        if colisao: #Se retornar true o jogo breka
            inimigos.remove(colisao)
            todasSprites.remove(colisao)

        tela.blit(imagemFundo, (0,0))
        # tela.blit(fogo, (jogador.rect.x + 55, jogador.rect.y + 118))
        todasSprites.draw(tela) #Esse método desenha todas as sprites dentro do grupo "todasSprites" na tela


        pygame.display.update() #Atualiza a tela do pygame
