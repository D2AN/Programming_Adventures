import pygame
import os
import sys

# Pygame inicializacija
pygame.init()

# Langas
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maikeų peržiūra ir redagavimas")

# Spalvos
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Nustatome direktorijos, kurioje yra maikės, kintamąjį
maikes_dir = "maikės"

# Tikriname, ar direktorija "maikės" egzistuoja, jei ne, sukurkite ją
if not os.path.exists(maikes_dir):
    os.makedirs(maikes_dir)

# Sukuriame sąrašą maikeių failų pavadinimams (nuo m1 iki m31)
maikes_files = [f"m{i}.png" for i in range(1, 32)]

# Pradinės maikeių būsenos (True - turi, False - neturi)
maike_s = []

# Skaitome "numbers.txt" failą ir nustatome maikeių būsenas
with open("numbers.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        has_maike = line.strip().lower() == "true"  # Nenaudokite "true", jei failas turi "True"
        maike_s.append(has_maike)
        print(f"Maike {i}: {has_maike}")


current_maike = 0  # Pradinė maike
change_speed = 500  # Laiko vėlinimas tarp keitimo (milisekundėmis)
last_change_time = pygame.time.get_ticks()

def draw_text():
    screen.fill(white)

    # Tikrina, ar tai yra tinkama maike, kurią reikia rodyti
    if current_maike < len(maikes_files):
        has_maike = maike_s[current_maike]
        filename = maikes_files[current_maike]
        image = pygame.image.load(os.path.join(maikes_dir, filename))
        screen.blit(image, (10, 50))
        status = "Tu turi maikę" if has_maike else "Tu neturi maikės"
        text = font.render(f"{filename}: {status}", True, black)
        screen.blit(text, (350, 50))

    pygame.display.flip()

# Pradinė maikeių peržiūra
draw_text()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = pygame.time.get_ticks()
    if current_time - last_change_time >= change_speed:
        last_change_time = current_time

        # Tikrina rodykles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and current_maike > 0:
            current_maike -= 1
        if keys[pygame.K_DOWN] and current_maike < len(maike_s) - 1:
            current_maike += 1
        if keys[pygame.K_SPACE]:
            maike_s[current_maike] = not maike_s[current_maike]

        draw_text()
