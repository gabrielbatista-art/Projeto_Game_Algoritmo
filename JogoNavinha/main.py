import pygame, sys
import utilitarios
import Navinha as jogoNavinha
import StartGame as menu
import Gameover as gameover

pygame.init()

#VARIÁVEIS GERAIS ---------------------------------------------------------------------
#Tela
larguraTela, alturaTela = utilitarios.resolucaoX, utilitarios.resolucaoY #Define a resolução do jogo
tela = pygame.display.set_mode((larguraTela, alturaTela)) #Define a janela onde o jogo irá rodar.
pygame.display.set_caption(utilitarios.tituloGame) #Define o título da janela.

#Gameplay
Clock = pygame.time.Clock()
fps = 60 #Define a quantidade de quadros por segundo que o jogo roda

pontos : int = 0

while True:
    menu.start_screen(utilitarios.fundoMenu, utilitarios.logoMenu, [utilitarios.startMenu, utilitarios.startMenu2])
    jogoNavinha.jogoNavinha()
    gameover.game_over_screen(utilitarios.background)
