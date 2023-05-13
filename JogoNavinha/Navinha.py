import sys,pygame #Importa os módulos referentes ao sistema do computador e pygame
from Jogador import Jogador as player #Importa o jogador como player
from Inimigo import Inimigo as enemy #Importa o inimigo como enemy
from Tiro import Tiro

pygame.init() #Inicializa os módulos do pygame

#VARIÁVEIS GERAIS ---------------------------------------------------------------------
#Tela
larguraTela, alturaTela = 480, 720 #Define a resolução do jogo
tela = pygame.display.set_mode((larguraTela, alturaTela)) #Define a janela onde o jogo irá rodar.
pygame.display.set_caption("Python space shooter") #Define o título da janela.

#Gameplay
Clock = pygame.time.Clock()
fps = 60 #Define a quantidade de quadros por segundo que o jogo roda


#ENTIDADES ----------------------------------------------------------------------------
#Fundo
imagemFundo = pygame.image.load("JogoNavinha/Sprites/Fundo.png")
imagemFundo = pygame.transform.scale(imagemFundo, (larguraTela, alturaTela)) #Ajusta a imagem de fundo para o tamanho da tela

#Player
naveJogador = pygame.image.load("JogoNavinha/Sprites/Player.png") #Sprite player
velocidadePlayer = 10

#Inimigos
naveInimigo1 = pygame.image.load("JogoNavinha/Sprites/Inimigo_Olhao.png") #Sprite Inimigo
velocidadeInimigo = 5

#Tiro
tiroSprite = pygame.image.load("JogoNavinha/Sprites/Tiro.png")
velocidadeTiro = 10

#INSTANCIAR ENTIDADES ------------------------------------------------------------------
todasSprites = pygame.sprite.Group() #Inicia o grupo onde vão todas as sprites
inimigos = pygame.sprite.Group() #Inicia o grupo para armazenar inimigos
lasers = pygame.sprite.Group()

#JOGADOR
jogador = player(naveJogador, velocidade = velocidadePlayer, vida = 3, tela = (larguraTela, alturaTela)) #Instancia o jogador
todasSprites.add(jogador) #Adiciona o jogador as grupo de todas as sprites



#INIMIGOS
for c in range(5):
    inimigo = enemy(naveInimigo1, velocidade = velocidadeInimigo, tela = (larguraTela, alturaTela)) #Instancia o inimigo, a gente coloca um for pra instanciar vários dps
    todasSprites.add(inimigo) #Adiciona o inimigo ao grupo de todas as sprites
    inimigos.add(inimigo) #Adiciona o inimigo ao grupo dos inimigos p conferir a colisão c o player depois



while True:
    Clock.tick(fps) #Define a quantidade de quadros em que o jogo roda
    tela.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    todasSprites.update() #Esse método atualiza todos os objetos dentro do grupo

    tecla = pygame.key.get_pressed() #Observa as teclas que são apertadas a cada frame
    if tecla[pygame.K_SPACE]:
        laser = Tiro(tiroSprite, velocidadeTiro, 10, (larguraTela, alturaTela))
        laser.rect.left = jogador.rect.left
        laser.rect.bottom = jogador.rect.top
        todasSprites.add(laser)
        lasers.add(laser)

    colisaoTiro = pygame.sprite.groupcollide(inimigos, lasers, False, False)
    if colisaoTiro:
        inimigos.remove(colisaoTiro)
        todasSprites.remove(colisaoTiro)

    colisao = pygame.sprite.spritecollide(jogador, inimigos, False) #Confere se há colisão entre o player e os inimigos e retorna True ou False
    if colisao: #Se retornar true o jogo breka
        inimigos.remove(colisao)
        todasSprites.remove(colisao)

    tela.blit(imagemFundo, (0,0))
    todasSprites.draw(tela) #Esse método desenha todas as sprites dentro do grupo "todasSprites" na tela


    pygame.display.update() #Atualiza a tela do pygame
