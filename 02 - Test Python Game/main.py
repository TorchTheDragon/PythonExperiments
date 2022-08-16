import pygame

# Initialize otherwise game no work
pygame.init()

# Create game screen
screen = pygame.display.set_mode((1280, 720))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# PLayer
playerImg = pygame.image.load("Images/player.png")
playerX = 640
playerY = 660
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((45, 0, 45))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1280 - playerImg.get_width():
        playerX = 1280 - playerImg.get_width()
    
    player(playerX, playerY)
    pygame.display.update()

