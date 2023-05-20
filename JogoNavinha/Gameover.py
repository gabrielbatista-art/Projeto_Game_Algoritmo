import pygame, sys
import utilitarios

# Definição da tela de game over
def game_over_screen(fundo):
    font = pygame.font.SysFont("arial", 40, True, False) #Fonte do texto do jogo

    #VARIÁVEIS GERAIS ---------------------------------------------------------------------
    #Tela
    larguraTela, alturaTela = utilitarios.resolucaoX, utilitarios.resolucaoY #Define a resolução do jogo
    tela = pygame.display.set_mode((larguraTela, alturaTela)) #Define a janela onde o jogo irá rodar.
    telaRect = tela.get_rect()
    pygame.display.set_caption(utilitarios.tituloGame) #Define o título da janela.

    imagemFundo = pygame.image.load(fundo)


    while True:
        titulo = "GAME OVER"
        restart = "<ENTER> para reiniciar"
        sair = "<X> para sair"

        tituloExibir = font.render(titulo, True, (255, 255, 255))
        rectTitulo = tituloExibir.get_rect()

        restartExibir = font.render(restart, True, (255, 255, 255))
        rectRestart = restartExibir.get_rect()


        sairExibir = font.render(sair, True, (255, 255, 255))
        rectExibir = sairExibir.get_rect()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        tela.fill((0, 0, 0))
        tela.blit(imagemFundo, (0,0))
        tela.blit(tituloExibir, (telaRect.centerx - rectTitulo.centerx, telaRect.centery - rectTitulo.centery))
        tela.blit(restartExibir, (telaRect.centerx - rectRestart.centerx, telaRect.bottom - (rectRestart.bottom * 4)))
        tela.blit(sairExibir, (telaRect.centerx - rectExibir.centerx, telaRect.bottom - (rectExibir.bottom * 2)))
        pygame.display.flip()

        