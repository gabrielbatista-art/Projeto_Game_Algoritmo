import pygame
from pygame.locals import *
from pygame import mixer
from sys import exit
from random import randint
from random import Random

pygame.init()
# mixer.init()

# som_do_missil = mixer.music.load('')
# som_da_explosao = pygame.mixer.Sound('')

resolucao : tuple = (480, 640)

janela = pygame.display.set_mode(resolucao)
pygame.display.set_caption('Jogo da Nave')


clock = pygame.time.Clock() #Para definir o fps que o jogo vai rodar


imagemdefundo = pygame.image.load('spacebggame.png')
navedojogador = pygame.image.load('sprite_nave_pequena.png')
navedojogador2 = pygame.transform.rotate(navedojogador, 90)
nave_inimiga = pygame.image.load('nave_inimiga_pequena.png')


#Gerenciador de sprites
centroJogadorX, centroJogadorY = navedojogador.get_width() / 2, navedojogador.get_height() / 2
direitaJogador = navedojogador.get_width()
baixoJogador = navedojogador.get_height()


#Posição da nave do jogador
posicao_x_do_jogador = resolucao[0] / 2 - centroJogadorX
posicao_y_do_jogador = resolucao[1] / 2 - centroJogadorY
velocidade_da_nave_jogador = 10

balas : list = [] #Lista para armazenar as posições das balas atiradas
velBala = 1 #Velocidade do movimento da bala

tiro = False

while True:
    clock.tick(60) #Define o fps que o jogo vai rodar

    for events in pygame.event.get(): #Para fechar o jogo
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if events.type == KEYDOWN:
            if events.key == K_SPACE:
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
    #Pressiona a tecla de tiro
        # bala = pygame.draw.circle(janela, (0, 255, 0), (posicao_x_do_jogador + 45, posicao_y_do_jogador), 10)


    #Barreira para A nava do jogador não sair da tela
    if posicao_x_do_jogador <= 0:
        posicao_x_do_jogador = 0
    elif posicao_x_do_jogador >= resolucao[0] - centroJogadorX * 2:
        posicao_x_do_jogador = resolucao[0] - centroJogadorX * 2

    if posicao_y_do_jogador <= 0:
        posicao_y_do_jogador = 0
    elif posicao_y_do_jogador >= resolucao[1] - centroJogadorY * 2:
        posicao_y_do_jogador = resolucao[1] - centroJogadorY * 2

    
    
    janela.blit(imagemdefundo, (0,0))
    janela.blit(navedojogador, (posicao_x_do_jogador,posicao_y_do_jogador))
    janela.blit(nave_inimiga, (400,50))


    for bala in balas: #Itera pela lista "balas" e cria uma bala para cada elemento(bala) que existir lá
        if bala[1] >= 0: #Confere se o valor de "y" da bala ainda está dentro da janela
            print(bala[1])
            pygame.draw.circle(janela, (0, 255, 0), (bala[0], bala[1]), 10)
            bala[1] -= velBala
        else: #Se o valor de "y" excedeu a janela ele deleta o elemento da lista de acordo com seu índice
            balas.pop(balas.index(bala))


    print(balas)


    pygame.display.update()
    