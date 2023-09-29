import pygame
import sys
import random

# Inicializuojame Pygame
pygame.init()

# Ekranas
screen_info = pygame.display.Info()
eaukstis = screen_info.current_h
eplotis = screen_info.current_w
width, height = 800, 600
screen = pygame.display.set_mode((eplotis, eaukstis))
pygame.display.set_caption("Interaktyvūs kvadratai")
main = 10
raudonumas = 1
melinumumas = 1
zalumas = 1
# Kvadrato sąrašas
squares = []

# Kvadrato dydis
square_size = main

def draw_square(x, y, color):
    pygame.draw.rect(screen, color, (x, y, square_size, square_size))


running = True

# Žingsnio dydis
step_size = 2

# Pradinė spalva
current_color = pygame.Color(melinumumas, zalumas, raudonumas)  # Pradėsime su raudona spalva

# Galimos pagrindinės spalvos
main_colors = [(255, 0, 0), (0, 255, 0)]

# Nustatome pakartotinį klavišų paspaudimą ir užlaikymą
pygame.key.set_repeat(1, 1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Valome ekraną

    # Kvadrato kūrimas spaudžiant klavišą 'e'
    keys = pygame.key.get_pressed()
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        squares.append([x - square_size / 2, y - square_size / 2, current_color])

    # Keičiame visų kvadratų spalvą į atsitiktinę paspaudus "r"
    if keys[pygame.K_r]:
        current_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Pašaliname visus kvadratus paspaudus "x"
    if keys[pygame.K_x]:
        squares = []

    # Pašaliname tik kvadratą, ant kurio yra pelės taškas, paspaudus "c"
    

    # Judėjimo logika laikant klavišus
    if keys[pygame.K_a]:
        for square in squares:
            square[0] -= step_size
    if keys[pygame.K_d]:
        for square in squares:
            square[0] += step_size
    if keys[pygame.K_w]:
        for square in squares:
            square[1] -= step_size
    if keys[pygame.K_s]:
        for square in squares:
            square[1] += step_size
    if keys[pygame.K_ESCAPE]:
        sys.exit()

    if keys[pygame.K_UP]:
        raudonumas = raudonumas + 1
        if raudonumas < 0:
            raudonumas = 0
        if raudonumas > 255:
            raudonumas = 255
        current_color = pygame.Color(melinumumas, zalumas, raudonumas)
        pygame.draw.rect(screen, current_color, (0, 0, 1000000, 100))

    if keys[pygame.K_RIGHT]:
        melinumumas = melinumumas + 1
        if melinumumas < 0:
            melinumumas = 0
        if melinumumas > 255:
            melinumumas = 255
        current_color = pygame.Color(melinumumas, zalumas, raudonumas)
        pygame.draw.rect(screen, current_color, (0, 0, 1000000, 100))

    if keys[pygame.K_DOWN]:
        zalumas = zalumas + 1
        if zalumas < 0:
            zalumas = 0
        if zalumas > 255:
            zalumas = 255
        current_color = pygame.Color(melinumumas, zalumas, raudonumas)
        pygame.draw.rect(screen, current_color, (0, 0, 1000000, 100))

    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        raudonumas -= 2
        if raudonumas < 0:
            raudonumas = 0
        if raudonumas > 255:
            raudonumas = 255
        current_color = pygame.Color(melinumumas, zalumas, raudonumas)
        pygame.draw.rect(screen, current_color, (0, 0, 1000000, 100))
        

    if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
        melinumumas -= 2
        if melinumumas < 0:
            melinumumas = 0
        if melinumumas > 255:
            melinumumas = 255
        current_color = pygame.Color(melinumumas, zalumas, raudonumas)
        pygame.draw.rect(screen, current_color, (0, 0, 1000000, 100))

    if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        zalumas -= 2
        if zalumas < 0:
            zalumas = 0
        if zalumas > 255:
            zalumas = 255
        current_color = pygame.Color(melinumumas, zalumas, raudonumas)
        pygame.draw.rect(screen, current_color, (0, 0, 1000000, 100))

    if keys[pygame.K_SPACE] or keys[pygame.K_LEFT]:
        pygame.draw.rect(screen, current_color, (0, 0, 1000000, 100))
    if keys[pygame.K_KP1]:
        square_size = 5
    if keys[pygame.K_KP2]:
        square_size = 10
    if keys[pygame.K_KP3]:
        square_size = 15
    if keys[pygame.K_KP4]:
        square_size = 20
    if keys[pygame.K_KP5]:
        square_size = 25
    if keys[pygame.K_6]:
        square_size = 30
    if keys[pygame.K_KP7]:
        square_size = 35
    if keys[pygame.K_KP8]:
        square_size = 40
    if keys[pygame.K_KP9]:
        square_size = 45
    if pygame.mouse.get_pressed()[2]:
        x, y = pygame.mouse.get_pos()
        squares_to_remove = []
        for square in squares:
            if square[0] <= x <= square[0] + square_size and square[1] <= y <= square[1] + square_size:
                squares_to_remove.append(square)
        for square in squares_to_remove:
            squares.remove(square)

    # Piešiame visus kvadratus
    for square in squares:
        draw_square(square[0], square[1], square[2])

    
        
    pygame.display.flip()  # Atnaujiname ekraną

pygame.quit()
sys.exit()