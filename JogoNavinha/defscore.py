import pygame

def desenhar_pontos(pontos,tela):
    fonte = pygame.font.SysFont(None, 60)  #tem que escolher uma fonte
    texto = fonte.render(str(pontos), True, (255, 255, 255))  # tem que escolher uma cor
    tela.blit(texto, (140, 15))  # e saber a posição na tela
