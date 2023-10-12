import pygame
import sys

pygame.init()

# Žaidimo lango nustatymai
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kaladėlių žaidimas")

# Spalvos
WHITE = (255, 255, 255)

# Kaladėlės nustatymai
card_image = pygame.image.load('pelyte.png')  # Paveikslėlis, kurį naudosime kaip kaladėlę
card_rect = card_image.get_rect()
card_rect.center = (WIDTH // 2, HEIGHT // 2)
angle = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gaukime žaidėjo įvestį
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        card_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        card_rect.x += 5
    if keys[pygame.K_UP]:
        card_rect.y -= 5
    if keys[pygame.K_DOWN]:
        card_rect.y += 5

    # Pasukime kaladėlę
    if keys[pygame.K_SPACE]:
        angle += 5
        card_image = pygame.transform.rotate(card_image, 5)

    # Valom ekraną
    window.fill(WHITE)

    # Piešiame kaladėlę
    window.blit(pygame.transform.rotate(card_image, angle), card_rect.topleft)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()