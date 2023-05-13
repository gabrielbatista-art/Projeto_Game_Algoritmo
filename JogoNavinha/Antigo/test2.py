import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela do jogo
screen_width = 800
screen_height = 600

# Define cores
black = pygame.Color('black')
white = pygame.Color('white')

# Define as fontes
font = pygame.font.SysFont(None, 30)
font_big = pygame.font.SysFont(None, 50)

# Cria a janela do jogo
screen = pygame.display.set_mode((screen_width, screen_height))

# Definição da função de desenhar textos na tela
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Definição da tela inicial do menu
def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        screen.fill(black)
        draw_text("Jogo de Nave", font_big, white, screen, screen_width//2, screen_height//4)
        draw_text("Pressione Enter para iniciar o jogo", font, white, screen, screen_width//2, screen_height//2)
        pygame.display.flip()

# Definição da tela de game over
def game_over_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        screen.fill(black)
        draw_text("Game Over", font_big, white, screen, screen_width//2, screen_height//4)
        draw_text("Sua pontuação: " + str(score), font, white, screen, screen_width//2, screen_height//2)
        draw_text("Pressione Enter para jogar novamente", font, white, screen, screen_width//2, screen_height*3//4)
        pygame.display.flip()

def jogo():
    while True:

        # Processa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualiza os sprites
        all_sprites.update()

        # Verifica se houve colisão entre a nave e algum inimigo
        hits = pygame.sprite.spritecollide(ship, enemies, False)
        if hits:
            # running = False
            break

        # Desenha os sprites na tela
        screen.fill(black)
        all_sprites.draw(screen)
        
        # Desenha a pontuação do jogador na tela
        score_text = font.render("Pontuação: " + str(score), True, white)
        screen.blit(score_text, (10, 10))

        # Atualiza a tela
        pygame.display.flip()

        # Verifica se um inimigo saiu da tela e atualiza a pontuação
        # for enemy in enemies:
        #     if enemy.rect.top > screen_height:
        #         score += 10

        # Cria novos inimigos se não houverem mais na tela
        if len(enemies) == 0:
            for i in range(10):
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)

        # Define a taxa de atualização do jogo
        clock = pygame.time.Clock()
        clock.tick(60)


# Define a variável para a pontuação do jogador
score = 0

# Define o título da janela do jogo
pygame.display.set_caption("Jogo de Nave")

# Define as cores utilizadas no jogo
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define a classe para a nave
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(white)
        pygame.draw.polygon(self.image, black, ((0, 50), (25, 0), (50, 50)))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)

    def update(self):
        # Move a nave para a esquerda ou direita
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Mantém a nave dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

# Define a classe para os inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(red)
        pygame.draw.circle(self.image, black, (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        # Move o inimigo para baixo
        self.rect.y += self.speedy

        # Se o inimigo passar da parte de baixo da tela, volta para cima
        if self.rect.top > screen_height + 10:
            self.rect.x = random.randrange(screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Cria um grupo para os sprites
all_sprites = pygame.sprite.Group()

# Cria a nave e adiciona ao grupo
ship = Ship()
all_sprites.add(ship)

# # Cria um grupo para os inimigos
# enemies = pygame.sprite.Group()

enemies = pygame.sprite.Group()

def inimigo():
       for i in range(10):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

# # Cria 10 inimigos e adiciona ao grupo
# for i in range(10):
#     enemy = Enemy()
#     all_sprites.add(enemy)
#     enemies.add(enemy)

# Define a fonte utilizada para os textos
font = pygame.font.Font(None, 36)



# Define o loop principal do jogo
running = True

while running:

    start_screen()
    inimigo()
    jogo()
    for enemy in enemies:
        all_sprites.remove(enemy)
        enemies.remove(enemy)
    game_over_screen()


# Chama a tela game over


# Encerra o Pygame
pygame.quit()    