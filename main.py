import pygame
import sys
import os

# Inicializuojame Pygame
pygame.init()

# Nustatome ekraną
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Žaidimų pasirinkimas")

# Spalvos
WHITE = (255, 255, 255)

# Funkcija, kuri vykdoma, kai paspaudžiamas mygtukas
def run_game(game_file):
    os.system(f"python {game_file}")

# Pagrindinis programos ciklas
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Jei paspaudžiamas kairysis pelės mygtukas
            if event.button == 1:
                x, y = event.pos
                # Tikriname, kurį mygtuką paspaudė vartotojas ir paleidžiame atitinkamą failą
                if 100 <= x <= 200 and 150 <= y <= 250:
                    run_game("bandomasis.py")
                elif 200 <= x <= 300 and 150 <= y <= 250:
                    run_game("game.py")

    # Nupiešiame ekraną
    screen.fill(WHITE)
    # Piešiame mygtukus
    pygame.draw.rect(screen, (0, 255, 0), (100, 150, 100, 100))
    pygame.draw.rect(screen, (0, 0, 255), (200, 150, 100, 100))
    pygame.display.flip()

# Išeiname iš Pygame
pygame.quit()
sys.exit()
