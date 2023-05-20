# Definição da tela de game over
import pygame, sys
import utilitarios

def start_screen(fundo, logo, start):
    pygame.init()

    larguraTela, alturaTela = utilitarios.resolucaoX, utilitarios.resolucaoY #Define a resolução do jogo
    tela = pygame.display.set_mode((larguraTela, alturaTela)) #Define a janela onde o jogo irá rodar.
    pygame.display.set_caption(utilitarios.tituloGame) #Define o título da janela.

    imagemFundo = pygame.image.load(fundo)
    fundoRect = imagemFundo.get_rect()
    imagemLogo = pygame.image.load(logo)
    rectLogo = imagemLogo.get_rect()
    imagemStart = pygame.image.load(start)
    rectStart = imagemStart.get_rect()

    font = pygame.font.SysFont("arial", 40, True, False)
    # game_over_text = font.render("NAVINHA", True, (255, 255, 255))
    # start_text = font.render("ENTER para iniciar", True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        tela.fill((0, 0, 0))
        tela.blit(imagemFundo, (0, 0))
        tela.blit(imagemLogo, (fundoRect.centerx - rectLogo.centerx, fundoRect.centery - rectLogo.bottom * 1.3))
        tela.blit(imagemStart, (fundoRect.centerx - rectStart.centerx, fundoRect.bottom - rectLogo.bottom * 0.87))

        # tela.blit(game_over_text, (tela.get_width() // 2 - game_over_text.get_width() // 2,
        #                               tela.get_height() // 4 - game_over_text.get_height() // 2))
        # tela.blit(start_text, (tela.get_width() // 2 - start_text.get_width() // 2,
        #                         tela.get_height() * 3 // 4 + 40 - start_text.get_height() // 2))

        pygame.display.flip()

