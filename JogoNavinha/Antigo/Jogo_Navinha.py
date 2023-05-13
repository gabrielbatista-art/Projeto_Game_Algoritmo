import pygame
from pygame.locals import *
from pygame import mixer
from sys import exit
from random import randint

pygame.init()
# mixer.init()

# som_do_missil = mixer.music.load('')
# som_da_explosao = pygame.mixer.Sound('')

resolucaoX, resolucaoY = 480, 640

janela = pygame.display.set_mode((resolucaoX, resolucaoY))
pygame.display.set_caption('Jogo da Nave')


clock = pygame.time.Clock() #Para definir o fps que o jogo vai rodar


imagemdefundo = pygame.image.load('spacebggame.png')
imagemdefundo = pygame.transform.rotate(imagemdefundo, 90)
imagemdefundo = pygame.transform.scale(imagemdefundo, (resolucaoX, resolucaoY))

navedojogador = pygame.image.load('sprite_nave_pequena.png')
rectJogador = navedojogador.get_rect()

naveInimiga = pygame.image.load('nave_inimiga_pequena.png')
rectInimigo = naveInimiga.get_rect()

#Grupos
# player = pygame.sprite.Group()
# player.add(rectJogador)


score = 0
font = pygame.font.SysFont("arial", 20, True, False) #Fonte do texto do jogo


#Gerenciador de sprites
#Player
centroJogadorX, centroJogadorY = navedojogador.get_width() / 2, navedojogador.get_height() / 2
direitaJogador = navedojogador.get_width()
baixoJogador = navedojogador.get_height()
rectJogador = navedojogador.get_rect()

#Inimigo
centroInimigoX, centroInimigoY = naveInimiga.get_width() / 2, naveInimiga.get_height() / 2
direitaInimigo = naveInimiga.get_width()
baixoInimigo = naveInimiga.get_height()
rectInimigo = naveInimiga.get_rect()


#Nave do jogador
posicao_x_do_jogador = resolucaoX / 2 - centroJogadorX
posicao_y_do_jogador = resolucaoY / 2 - centroJogadorY

velocidade_da_nave_jogador = 10

balas : list = [] #Lista para armazenar as posições das balas atiradas
velBala = 10 #Velocidade do movimento da bala

tiro = False

#Nave do inimigo
posicaoInimigo : list = []
naves : list = []

velocidadeNaveInimigo = 3

nasceInimigoFrequencia = 30
nasceInimigo = 24
podeNascerInimigo = False
pygame.time.set_timer(nasceInimigo, nasceInimigoFrequencia, 0)


while True:
    clock.tick(60) #Define o fps que o jogo vai rodar
    janela.fill((0, 0, 0))

    mensagem : str = f"Pontos: {score}"
    texto_formatado = font.render(mensagem, True, (255, 255, 255))

    for events in pygame.event.get(): #Para fechar o jogo
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if events.type == KEYDOWN:
            if events.key == K_SPACE: #Detecta o botão de tiro
                balas.append([posicao_x_do_jogador + 45, posicao_y_do_jogador])


    #Movimentação da nave do jogador
    teclas = pygame.key.get_pressed()
    #Se pressionar setinha para cima
    if teclas[pygame.K_UP]:
        posicao_y_do_jogador -= velocidade_da_nave_jogador
    #Se pressionar setinha para baixo
    if teclas[pygame.K_DOWN]:
        posicao_y_do_jogador += velocidade_da_nave_jogador
    #Se pressionar setinha para esquerda
    if teclas[pygame.K_LEFT]:
        posicao_x_do_jogador -= velocidade_da_nave_jogador
    #Se pressionar setinha para direita
    if teclas[pygame.K_RIGHT]:
        posicao_x_do_jogador += velocidade_da_nave_jogador


    #Barreira para A nava do jogador não sair da tela
    if posicao_x_do_jogador <= 0: #Confere se a posição X do jogador é menor que 0
        posicao_x_do_jogador = 0 #Caso seja ele faz com que o valor de X do jogador volte a ser 0
    elif posicao_x_do_jogador >= resolucaoX - centroJogadorX * 2: #Confere se a posição X do jogador é maior que a resolução X da tela
        posicao_x_do_jogador = resolucaoX - centroJogadorX * 2 #Caso seja ele faz com que a posição X do jogador seja

    if posicao_y_do_jogador <= 0:
        posicao_y_do_jogador = 0
    elif posicao_y_do_jogador >= resolucaoY - centroJogadorY * 2:
        posicao_y_do_jogador = resolucaoY - centroJogadorY * 2

    
    janela.blit(imagemdefundo, (0,0))

    janela.blit(navedojogador, (posicao_x_do_jogador,posicao_y_do_jogador))

    #SPAWNER DE INIMIGOS
    if pygame.event.get(nasceInimigo): #Observa se o timer do nascimento dos inimigos já resetou
        podeNascerInimigo = True

    if podeNascerInimigo:
        posicaoInimigoX = randint(0, resolucaoX)
        posicaoInimigoY = 0 - centroInimigoY
        posicaoInimigo.append([posicaoInimigoX, posicaoInimigoY])
        podeNascerInimigo = False

    #Movimento Inimigo
    for inimigo in posicaoInimigo: #Para cada posição de inimigo na lista ele desenha um inimigo na tela
        if inimigo[1] < resolucaoY:
            janela.blit(naveInimiga, (inimigo[0], inimigo[1]))
            inimigo[1] += velocidadeNaveInimigo
            print(inimigo[1])
            for bala in balas:
                if bala[1] <= (inimigo[1] + baixoInimigo) and bala[1] >= (inimigo[1] - baixoInimigo) and bala[0] <= (inimigo[0] + direitaInimigo) and bala[0] >= (inimigo[0] - direitaInimigo):
                    posicaoInimigo.pop(posicaoInimigo.index(inimigo))
                    score += 1
        else:
            posicaoInimigo.pop(posicaoInimigo.index(inimigo))


    #Movimento e spawn de balas
    for bala in balas: #Itera pela lista "balas" e cria uma bala para cada elemento(bala) que existir lá
        if bala[1] >= 0: #Confere se o valor de "y" da bala ainda está dentro da janela
            tiro = pygame.draw.circle(janela, (0, 255, 0), (bala[0], bala[1]), 10)
            bala[1] -= velBala
        else: #Se o valor de "y" excedeu a janela ele deleta o elemento da lista de acordo com seu índice
            balas.pop(balas.index(bala))
        
    #Detector colisão bala
    


    janela.blit(texto_formatado, (10, 40))
    pygame.display.update()
    