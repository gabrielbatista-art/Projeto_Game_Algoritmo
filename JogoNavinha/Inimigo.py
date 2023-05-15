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
        # self.rect.y += self.velocidade #A nave só se move p baixo
        pass
