import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 500))
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

# Button texts
button_font = pygame.font.Font(None, 24)
button1_text = button_font.render("Mokykis", True, BLACK)
button1_rect = button1_text.get_rect()
button1_x = 0
button1_y = 50
button1_rect.topleft = (button1_x, button1_y)

button2_text = button_font.render("Testuokis", True, BLACK)
button2_rect = button2_text.get_rect()
button2_x = 0
button2_y = 150
button2_rect.topleft = (button2_x, button2_y)

button3_text = button_font.render("Žaisk", True, BLACK)
button3_rect = button3_text.get_rect()
button3_x = 0
button3_y = 250
button3_rect.topleft = (button3_x, button3_y)

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
                if 0 <= x <= 100 and 0 <= y <= 100:
                    run_game("bandomasis.py")
                        
                elif 0 <= x <= 100 and 100 <= y <= 200:
                    run_game("paint.py")
                        
                elif 0 <= x <= 100 and 200 <= y <= 300:
                    run_game("game.py")
                    
   
    # Draw the screen
    screen.fill(WHITE)

    # Draw the buttons
    pirmas = pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 100))
    antras = pygame.draw.rect(screen, (0, 0, 255), (0, 100, 100, 100))
    trecias = pygame.draw.rect(screen, (255, 0, 0), (0, 200, 100, 100))
    if pirmas.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 200, 0), (0, 0, 100, 100))
    if antras.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 200), (0, 100, 100, 100))
    if trecias.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (200, 0, 0), (0, 200, 100, 100))


    # Draw the texts
    screen.blit(main_text, main_text_rect)
    screen.blit(button1_text, button1_rect)
    screen.blit(button2_text, button2_rect)
    screen.blit(button3_text, button3_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()