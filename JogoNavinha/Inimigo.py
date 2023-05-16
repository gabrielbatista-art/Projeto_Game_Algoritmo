from random import randint
import pygame

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, naveInimigoSprite, velocidade : int, tela : tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = naveInimigoSprite
        self.rect = self.image.get_rect()
        self.rect.topleft = randint(0, tela[0]), 0 #Ajusta a posição do inimigo na tela
        self.tela = (tela[0], tela[1]) #Largura tela, Altura tela
        # self.velocidade = velocidade
        self.velocidade = randint(1, velocidade)

    def update(self):
        self.rect.y += self.velocidade #A nave só se move p baixo

        #Mantém a nave dentro da tela no eixo X
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.tela[0]:
            self.rect.right = self.tela[0]
        #Mantém a nave dentro da tela no eixo Y
        # if self.rect.top < 0:
        #     self.rect.top = 0
        # elif self.rect.bottom > self.tela[1] + 50:
        #     self.rect.bottom = self.tela[1] + 50
       
