# Definição da tela de game over
import pygame
import sys

def start_screen(background, screen):
    font = pygame.font.SysFont("arial", 40, True, False)
    game_over_text = font.render("NAVINHA", True, (255, 255, 255))
    # score_text = font.render("Score:", True, (255, 255, 255))
    # play_again_text = font.render("Jogar de novo", True, (255, 255, 255))
    start_text = font.render("ENTER para iniciar", True, (255, 255, 255))

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

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2,
                                      screen.get_height() // 4 - game_over_text.get_height() // 2))
        # screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2,
        #                           screen.get_height() // 2 - score_text.get_height() // 2))
        # screen.blit(play_again_text, (screen.get_width() // 2 - play_again_text.get_width() // 2,
        #                                screen.get_height() * 3 // 4 - play_again_text.get_height() // 2))
        screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2,
                                screen.get_height() * 3 // 4 + 40 - start_text.get_height() // 2))

        pygame.display.flip()

