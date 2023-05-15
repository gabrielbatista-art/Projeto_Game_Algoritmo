import pygame, sys

# Definição da tela de game over
def game_over_screen(background, screen):
    font = pygame.font.SysFont("arial", 40, True, False) #Fonte do texto do jogo
    while True:
        titulo = "NAVINHA"
        tituloExibir = font.render(titulo, True, (255, 255, 255))

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

        screen.fill((0, 0, 0))
        screen.blit(background, (0,0))
        screen.blit(tituloExibir, (20, 20))
        # draw_text("Game Over", font_big, red, screen, screen_width//2, screen_height//4)
        # draw_text("Sua pontuação: " + str(score), font, white, screen, screen_width//2, screen_height//2)
        # draw_text("Pressione Enter para jogar novamente", font, white, screen, screen_width//2, screen_height*3//4)
        # draw_text("Pressione ESC para sair do jogo", font, white, screen, screen_width//2, screen_height*3//4 + 40)
        pygame.display.flip()