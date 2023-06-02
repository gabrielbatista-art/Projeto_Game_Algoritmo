import pygame
import Navinha
import utilitarios

#Tela
larguraTela, alturaTela = utilitarios.resolucaoX, utilitarios.resolucaoY #Define a resolução do jogo

class Tiro(pygame.sprite.Sprite):
    def __init__(self, balaSprite, velocidade : int, forca : int, tela:tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = balaSprite
        self.rect = self.image.get_rect()
        self.velocidade = velocidade
        self.forca = forca
        self.tela = (tela[0], tela[1])
    
    def update(self):
        self.rect.y -= self.velocidade

        if self.rect.top > alturaTela:
            self.kill()
            
