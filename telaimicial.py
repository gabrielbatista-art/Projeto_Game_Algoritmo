import pygame

pygame.init()
# Define as dimensões da janela
imagemfundo = pygame.image.load("Fundo.png")
tela_largura = 720
tela_altura = 480
# Define as cores
preto = (0, 0, 0)
branco = (255, 255, 255)
# Crie a janela
janela = pygame.display.set_mode((tela_largura, tela_altura))
# Defina o título da janela
pygame.display.set_caption("Tela de Início")
# Carregue uma imagem de fundo
background_image =  pygame.transform.scale(imagemfundo,(tela_largura,tela_altura))
# Crie um texto
font = pygame.font.Font(None, 64)
text = font.render(" jogo da navinha", True, preto)
# Defina a posição do texto
text_rect = text.get_rect()
text_rect.centerx = janela.get_rect().centerx
text_rect.centery = janela.get_rect().centery - 100
# Defina os botões
button_font = pygame.font.Font(None, 48)
start_button = button_font.render("Iniciar (Enter)", True, branco)
quit_button = button_font.render("Sair (X)", True, branco)
# Defina as posições dos botões
start_button_rect = start_button.get_rect()
start_button_rect.centerx = janela.get_rect().centerx
start_button_rect.centery = janela.get_rect().centery + 50
quit_button_rect = quit_button.get_rect()
quit_button_rect.centerx = janela.get_rect().centerx
quit_button_rect.centery = janela.get_rect().centery + 150
# Loop que vai aparecer jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Verifica se a tecla Enter foi pressionada
                print("Entrando no jogo...")
            elif event.key == pygame.K_x:  # Verifica se a tecla X foi pressionada
                pygame.quit()
                quit()


    janela.blit(background_image, [0, 0])

    # Desenha o texto
    janela.blit(text, text_rect)

    # Desenha os botões
    janela.blit(start_button, start_button_rect)
    janela.blit(quit_button, quit_button_rect)


    pygame.display.update()
