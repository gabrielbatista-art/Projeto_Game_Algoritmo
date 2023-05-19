import pygame

def desenhar_pontos(pontos,tela):
    fonte = pygame.font.SysFont(None, 30)  #tem que escolher uma fonte
    texto = fonte.render("Pontos: " + str(pontos), True, (255, 255, 255))  # tem que escolher uma cor
    tela.blit(texto, (10, 10))  # e saber a posição na tela
