import pygame

class Jogador(pygame.sprite.Sprite): #Cria a classe jogador e suas particularidades e métodos
    def __init__(self, naveJogadorSprite, velocidade : int, tela : tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = naveJogadorSprite
        self.rect = self.image.get_rect() #Pega o retangulo para conferir colisão baseado no tamanho da imagem
        self.tela = (tela[0], tela[1])
        self.velocidade = velocidade

    def update(self):
        pygame.draw.rect(self.image, (255, 0, 0), self.rect, 1)


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