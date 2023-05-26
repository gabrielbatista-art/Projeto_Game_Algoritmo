import pygame, sys
import utilitarios

# Definição da tela de game over
def game_over_screen(fundo, over, sair : tuple, restart : tuple):
    pygame.init()

    font = pygame.font.SysFont("arial", 40, True, False) #Fonte do texto do jogo

    #VARIÁVEIS GERAIS ---------------------------------------------------------------------
    #Tela
    larguraTela, alturaTela = utilitarios.resolucaoX, utilitarios.resolucaoY #Define a resolução do jogo
    tela = pygame.display.set_mode((larguraTela, alturaTela)) #Define a janela onde o jogo irá rodar.
    telaRect = tela.get_rect()
    pygame.display.set_caption(utilitarios.tituloGame) #Define o título da janela.
    imagemFundo = pygame.image.load(fundo)
    fundoRect = imagemFundo.get_rect()


    imagemGameover = pygame.image.load(over)
    rectGameover = imagemGameover.get_rect()

    imagemExit1 = pygame.image.load(sair[0])
    imagemExit2 = pygame.image.load(sair[1])
    rectExit = imagemExit1.get_rect()
    rectExit.x = fundoRect.centerx - rectExit.centerx
    rectExit.y = fundoRect.bottom - rectGameover.bottom * 0.5

    imagemRestart1 = pygame.image.load(restart[0])
    imagemRestart2 = pygame.image.load(restart[1])
    rectRestart = imagemRestart1.get_rect()
    rectRestart.x = fundoRect.centerx - rectRestart.centerx
    rectRestart.y = fundoRect.bottom - rectGameover.bottom * 0.85

    #CURSOR DO MOUSE --------------------
    pygame.mouse.set_visible(False)
    imagem_cursor = pygame.image.load("Sprites/Menu/cursor_navinha_export.png")
    imagem_cursor_rect = imagem_cursor.get_rect()

    
    while True:
        # titulo = "GAME OVER"
        # restart = "<ENTER> para reiniciar"
        # sair = "<X> para sair"

        # tituloExibir = font.render(titulo, True, (255, 255, 255))
        # rectTitulo = tituloExibir.get_rect()

        # restartExibir = font.render(restart, True, (255, 255, 255))
        # rectRestart = restartExibir.get_rect()
       

        # sairExibir = font.render(sair, True, (255, 255, 255))
        # rectExibir = sairExibir.get_rect()
        imagem_cursor_rect = imagem_cursor.get_rect() #retangulo do mouse
        posicao_mouse = pygame.mouse.get_pos()  # update position


        imagem_cursor_rect.x = posicao_mouse[0]
        imagem_cursor_rect.y = posicao_mouse[1]

        colisaoRestart = pygame.Rect.colliderect(imagem_cursor_rect, rectRestart)
        colisaoexit = pygame.Rect.colliderect(imagem_cursor_rect, rectExit)

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
        
        if pygame.mouse.get_pressed()[0] and colisaoRestart:
            break
        
        if pygame.mouse.get_pressed()[0] and colisaoexit:
            pygame.quit()
            sys.exit()
            
        # tela.fill((0, 0, 0))
        # tela.blit(imagemFundo, (0,0))
        # tela.blit(tituloExibir, (telaRect.centerx - rectTitulo.centerx, telaRect.centery - rectTitulo.centery))
        # tela.blit(restartExibir, (telaRect.centerx - rectRestart.centerx, telaRect.bottom - (rectRestart.bottom * 4)))
        # tela.blit(sairExibir, (telaRect.centerx - rectExibir.centerx, telaRect.bottom - (rectExibir.bottom * 2)))
        # pygame.display.flip()

     

        tela.fill((0, 0, 0))
        tela.blit(imagemFundo, (0, 0))
        tela.blit(imagemGameover, (fundoRect.centerx - rectGameover.centerx, fundoRect.centery - rectGameover.bottom * 0.8))
        
        colisMenu = pygame.Rect.colliderect(imagem_cursor_rect, rectRestart)
        if colisMenu:
            tela.blit(imagemRestart2, (rectRestart.x, rectRestart.y))
        else:
            tela.blit(imagemRestart1, (rectRestart.x, rectRestart.y))

        colisMenu = pygame.Rect.colliderect(imagem_cursor_rect, rectExit)
        if colisMenu:
            tela.blit(imagemExit2, (rectExit.x, rectExit.y))
        else:
            tela.blit(imagemExit1, (rectExit.x, rectExit.y))

        tela.blit(imagem_cursor, posicao_mouse) # draw the cursor

        pygame.display.flip()

        
