import pygame

# Initialize the Game
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Deckbuilding")
icon = pygame.image.load("Images/Icons/logo.png")
pygame.display.set_icon(icon)

# Main Menu - Start Button
startIMG = pygame.image.load("Images/Icons/start.png")
startIMGx = screen.get_width() / 2 - startIMG.get_width() / 2
startIMGy = screen.get_height() / 2 - startIMG.get_height() / 2 + 100

# Colors - RGBA
transparent = (0, 0, 0, 0)
black = (0, 0, 0, 255)
white = (255, 255, 255 ,255)
invisible = 0
maxAlpha = 255

# Screen Elements
def startButton(x, y):
    screen.blit(startIMG, (x, y))
    

def refreshScreen():
    screen.fill(black)


# Animation Loop
running = True
state = "MainMenu"
while running:
    refreshScreen()
    for event in pygame.event.get():
        # All the mouse buttons
        leftMouse, middleMouse, rightMouse, button4, button5 = pygame.mouse.get_pressed(5)
        # Checks to see if player has hit the quit button
        if event.type == pygame.QUIT:
            running = False
        # Checks to see if the left mouse button is pushed down
        if event.type == pygame.MOUSEBUTTONDOWN and leftMouse:
            # From Main Menu to Play State
            if pygame.rect.Rect(startIMGx, startIMGy, startIMG.get_width(), startIMG.get_height()).collidepoint(pygame.mouse.get_pos()):
                state = "PlayState"
                startIMG.set_alpha(invisible)
    
    # Checks for what state it is
    if state.lower() == "mainmenu":
        startButton(startIMGx, startIMGy)
        startIMG.set_alpha(maxAlpha)
    elif state.lower() == "playstate":
        pass
        
        
    pygame.display.update()