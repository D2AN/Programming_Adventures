import pygame
import sys
import os
# Initialize Pygame
pygame.init()
screen_info = pygame.display.Info()
eaukstis = screen_info.current_h
eplotis = screen_info.current_w
# Set up the display
screen = pygame.display.set_mode((eplotis, eaukstis))
pygame.display.set_caption("Pradžia")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to run when a button is pressed
def run_game(game_file):
    os.system(f"python {game_file}")

font = pygame.font.Font(None, 36)  # specify font and size

# Main text
main_text = font.render("Pasirinkite veikla:", True, BLACK)
main_text_rect = main_text.get_rect()
main_text_x = 100
main_text_y = 50
main_text_rect.topleft = (main_text_x, main_text_y)
puse = eplotis / 2
aukstis = eaukstis / 8
# Button texts
kordinate1 = [puse, eaukstis - aukstis]
kordinate2 = [puse, eaukstis - aukstis * 2]
kordinate3 = [puse, eaukstis - aukstis * 3]
button_font = pygame.font.Font(None, 24)
button1_text = button_font.render("Learnig", True, BLACK)
button1_rect = button1_text.get_rect()
button1_x = 0
button1_y = 50
button1_rect.topleft = (kordinate1[0] + 30 , kordinate1[1] + 30 )

button2_text = button_font.render("Tests", True, BLACK)
button2_rect = button2_text.get_rect()
button2_x = 0
button2_y = 150
button2_rect.topleft = (kordinate2[0] + 30 , kordinate2[1] + 30 )
buton = ['buton.png','butononmause.png']
button3_text = button_font.render("Play", True, BLACK)
button3_rect = button3_text.get_rect()
button3_x = 0
button3_y = 250
button3_rect.topleft = (kordinate3[0] + 30 , kordinate3[1] + 30 )

# Main program loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the left mouse button is pressed
            if event.button == 1:
                x, y = event.pos

                # Check which button the user pressed and run the corresponding file
                if pirmas_rect.collidepoint(pygame.mouse.get_pos()):
                    run_game("bandomasis.py")
                if antras_rect.collidepoint(pygame.mouse.get_pos()):
                    run_game("paint.py")
                if trecias_rect.collidepoint(pygame.mouse.get_pos()):
                    run_game("game.py")
    
    pirmas = pygame.image.load(buton[0])
    antras = pygame.image.load(buton[0])
    trecias = pygame.image.load(buton[0])
    pirmas_rect = pirmas.get_rect()
    antras_rect = antras.get_rect()
    trecias_rect = trecias.get_rect()
    pirmas_rect.x = kordinate1[0]
    pirmas_rect.y = kordinate1[1]
    antras_rect.x = kordinate2[0]
    antras_rect.y = kordinate2[1]
    trecias_rect.x = kordinate3[0]
    trecias_rect.y = kordinate3[1]
    screen.blit(pirmas, kordinate1)
    screen.blit(antras, kordinate2)
    screen.blit(trecias, kordinate3)
    # Draw the screen
    screen.fill(WHITE)

    
    if pirmas_rect.collidepoint(pygame.mouse.get_pos()):
       pirmas = pygame.image.load(buton[1])
    else:
        pirmas = pygame.image.load(buton[0])
    if antras_rect.collidepoint(pygame.mouse.get_pos()):
       antras = pygame.image.load(buton[1])
    else:
        antras = pygame.image.load(buton[0])
    if trecias_rect.collidepoint(pygame.mouse.get_pos()):
       trecias = pygame.image.load(buton[1])
    else:
        trecias = pygame.image.load(buton[0])

    # ce darau migtukius
    screen.blit(pirmas, kordinate1)
    screen.blit(antras, kordinate2)
    screen.blit(trecias, kordinate3)
    # uzrasai
    screen.blit(main_text, main_text_rect)
    screen.blit(button1_text, button1_rect)
    screen.blit(button2_text, button2_rect)
    screen.blit(button3_text, button3_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()