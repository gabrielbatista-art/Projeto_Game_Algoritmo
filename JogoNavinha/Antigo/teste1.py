import pygame
import random

pygame.init()

x = 1280
y = 720
#Definições de tela
teladojogo = pygame.display.set_mode((x,y))
pygame.display.set_caption('MVP DA NAVE')

imagemdefundo = pygame.image.load('spacebggame.png')
imagemdefundo = pygame.transform.scale(imagemdefundo, (x,y))

#definições inimigo
alienigena = pygame.image.load('nave_inimiga_pequena.png')
alienigena = pygame.transform.scale(alienigena ,(50,50))
alienigena = pygame.transform.rotate(alienigena, -90)

#definições jogador
jogador1 = pygame.image.load('sprite_nave_pequena.png')
jogador1 = pygame.transform.scale(jogador1, (50,50))
jogador1 = pygame.transform.rotate(jogador1, -90)

#definição missil
missil = pygame.image.load('missil_pequeno.png')
missil = pygame.transform.scale(missil, (25,25))
missil = pygame.transform.rotate(missil, -90)

#posição inimigo
posicao_alienigena_x = 500
posicao_alienigena_y = 360

#possição jogador
posicao_jogador1_x = 200
posicao_jogador1_y = 300

velocidade_x_missil = 0
posicao_x_missil = 200
posicao_y_missil = 300

pontos = 10

triggered = False
rodando = True

corpojogador1 = jogador1.get_rect()
corpoalienigena = alienigena.get_rect()
corpo_missil = missil.get_rect()

#funções
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respawn_missil():
    triggered = False
    respawn_missil_x = posicao_jogador1_x
    respawn_missil_y = posicao_jogador1_y
    velocidade_x_missil = 0
    return[respawn_missil_x, respawn_missil_y, triggered, velocidade_x_missil]

def colisao():
    global pontos
    if corpojogador1.colliderect(corpoalienigena) or corpoalienigena.x == 60:
        pontos -= 1
        return True
    elif corpo_missil.colliderect(corpoalienigena):
        pontos += 1
        return True
    else:
        return False


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    teladojogo.blit(imagemdefundo, (0,0))
    relativo_x = x % imagemdefundo.get_rect().width
    if relativo_x < 1280:
        teladojogo.blit(imagemdefundo, (relativo_x,0))
    #sprites na tela
    teladojogo.blit(alienigena,(posicao_alienigena_x,posicao_alienigena_y))
    teladojogo.blit(missil,(posicao_x_missil,posicao_y_missil))
    teladojogo.blit(jogador1, (posicao_jogador1_x, posicao_jogador1_y))
    #teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and posicao_jogador1_y > 1:
        posicao_jogador1_y -= 1
        posicao_y_missil -= 1
    if tecla[pygame.K_DOWN] and posicao_jogador1_y < 665:
        posicao_jogador1_y += 1
        if not triggered:
            posicao_y_missil += 1
    if tecla[pygame.K_SPACE]:
        triggered = True
        velocidade_x_missil = 2

    #respawn
    if posicao_alienigena_x == 50 or colisao():
        posicao_alienigena_x = respawn()[0]
        posicao_alienigena_y = respawn()[1]
    if posicao_x_missil == 1300:
        posicao_x_missil,posicao_y_missil,triggered,velocidade_x_missil = respawn_missil()
    #posição rect
    corpojogador1.y = posicao_jogador1_y
    corpojogador1.x = posicao_jogador1_x
    
    corpo_missil.x = posicao_alienigena_x
    corpo_missil.y = posicao_alienigena_y
    
    corpoalienigena.x = posicao_alienigena_x
    corpoalienigena.y = posicao_alienigena_y

    #movimentação da tela
    x += 15
    #movimentação 
    posicao_alienigena_x -= 1
    posicao_x_missil += velocidade_x_missil
    pygame.draw.rect(teladojogo,(255,0,0), corpojogador1, 4)
    pygame.draw.rect(teladojogo,(255,0,0),corpo_missil, 4)
    pygame.draw.rect(teladojogo,(255,0,0),corpoalienigena,4)
    print(pontos)
    pygame.display.update()
