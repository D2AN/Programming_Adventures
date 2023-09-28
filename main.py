import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
PLAYER_COLOR = (0, 255, 0)
BG_COLOR = (0, 0, 0)
GROUND_COLOR = (100, 100, 100)
JUMP_HEIGHT = -15
GRAVITY = 0.5
PLAYER_X_SPEED = 0.5
ANIMATION_SPEED = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("D2AN")

# Load background image
background_image = pygame.image.load("background.png").convert()

# Initialize mixer
pygame.mixer.init()

# Load menu music
menu_music = pygame.mixer.Sound("Menu.mp3")
menu_music.set_volume(0.3)  # Adjust the volume if needed

# Load game music
game_music = pygame.mixer.Sound("Game.mp3")
game_music.set_volume(0.3)  # Adjust the volume if needed

# Start playing menu music
menu_music.play(loops=-1)  # -1 means loop indefinitely

# Player attributes
player_x = 100
player_y = HEIGHT - PLAYER_HEIGHT
player_x_speed = PLAYER_X_SPEED
player_y_speed = 0
jumping = False

# Ground attributes
ground_y = HEIGHT - 50

# Game state
MENU = 0
GAME = 1
game_state = MENU

# Fonts
font = pygame.font.Font(None, 36)

# Main menu text
menu_text = font.render("Press SPACE to Start", True, (255, 255, 255))

# Load player animation frames
player_frames = []
for i in range(1):
    frame = pygame.image.load(f"player_frame{i}.png").convert_alpha()
    player_frames.append(frame)
frame_index = 0
frame_counter = 0

# Initial direction (right)
player_direction = "right"

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_state == MENU:
        if keys[pygame.K_SPACE]:
            game_state = GAME
            menu_music.stop()  # Stop menu music when transitioning to the game
            game_music.play(loops=-1)  # Start playing game music

    elif game_state == GAME:
        frame_counter += 1

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_x_speed
            player_direction = "left"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_x_speed
            player_direction = "right"

        if not jumping:
            if keys[pygame.K_SPACE]:
                player_y_speed = JUMP_HEIGHT
                jumping = True
        else:
            player_y_speed += GRAVITY

        player_y += player_y_speed

        if player_y >= ground_y - PLAYER_HEIGHT:
            player_y = ground_y - PLAYER_HEIGHT
            jumping = False
            player_y_speed = 0

        # Fill the background with the background image
        screen.blit(background_image, (0, 0))

        # Draw the ground
        pygame.draw.rect(screen, GROUND_COLOR, (0, ground_y, WIDTH, HEIGHT - ground_y))

        # Draw the player with animation
        player_image = player_frames[frame_index]
        if player_direction == "left":
            player_image = pygame.transform.flip(player_image, True, False)
        screen.blit(player_image, (player_x, player_y))

    if game_state == MENU:
        screen.fill(BG_COLOR)
        screen.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 2 - menu_text.get_height() // 2))

    pygame.display.update()

# Stop game music when quitting
game_music.stop()

# Quit Pygame
pygame.quit()
sys.exit()