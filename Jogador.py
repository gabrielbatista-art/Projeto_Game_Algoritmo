import pygame
from Tiro import Tiro

class Jogador(pygame.sprite.Sprite): #Cria a classe jogador e suas particularidades e métodos
    def __init__(self, naveJogadorSprite, velocidade : int, vida : int, tela : tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = naveJogadorSprite
        self.sprites = []
        self.sprites.append(pygame.image.load('Sprites/Player/player1.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/player2.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/player3.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/player4.png'))
        self.sprites.append(pygame.image.load('Sprites/Player/player5.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect() #Pega o retangulo para conferir colisão baseado no tamanho da imagem
        self.rect.centerx = tela[0] / 2 #Faz o player iniciar no centro do eixo x da tela
        self.rect.bottom = tela[1] #Faz o player iniciar na parte de baixo da tela
        self.tela = (tela[0], tela[1])
        self.velocidade = velocidade
        self.vida = vida

    # def animacao(self):
    #     self.atual = self.atual + 1
    #     if atual >= len(self.sprites):
    #         atual = 0
    #     self.image = self.sprites[self.atual]


    def update(self):
        # pygame.draw.rect(self.image, (255, 0, 0), self.rect, 1)

        self.atual = self.atual + 0.2
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        
        tecla = pygame.key.get_pressed() #Observa as teclas que são apertadas a cada frame
        #Move a nave no eixo X
        if tecla[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if tecla[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        #Move a nave no eixo Y
        if tecla[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if tecla[pygame.K_DOWN]:
            self.rect.y += self.velocidade

        #Mantém a nave dentro da tela no eixo X
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.tela[0]:
            self.rect.right = self.tela[0]
        #Mantém a nave dentro da tela no eixo Y
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.tela[1]:
            self.rect.bottom = self.tela[1]
            
        