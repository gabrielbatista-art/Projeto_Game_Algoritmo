import pygame, sys

def tela_inicial(fundo, logo, start):

    pygame.init()

    #resolução da tela
    resolucaox = 420
    resolucaoy =720

    tela = pygame.display.set_mod (resolucaox,resolucaoy)
    pygame.display.set_caption("teste mouse")

    #Fundo
    imagemFundo = pygame.image.load("Sprites/Fundo.png")
    imagemFundo = pygame.transform.scale(imagemFundo, (resolucaox, resolucaoy)) #Ajusta a imagem de fundo para o tamanho da tela
    
    #Imagens
    fundoMenu = "Sprites/Menu/fundo_menu.png"
    startMenu = "Sprites/Menu/start_menu.png"
    logoMenu = "Sprites/Menu/logo_menu.png"


    imagemFundo = pygame.image.load(fundo)
    fundoRect = imagemFundo.get_rect()
    imagemLogo = pygame.image.load(logo)
    rectLogo = imagemLogo.get_rect()
    imagemStart = pygame.image.load(start)
    rectStart = imagemStart.get_rect()

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

    pygame.display.flip()

