import pygame
class Player:
    def __init__(self, x, y, width, height, player_frames):
        self.x = x
        self.y = y - height
        self.width = width
        self.height = height
        self.player_frames = player_frames
        self.frame_index = 0
        self.frame_counter = 0
        self.direction = "right"
        self.x_speed = 0.5
        self.y_speed = 0
        self.jumping = False

    def move(self, keys, ground_y):
        self.frame_counter += 1

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.x_speed
            self.direction = "left"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.x_speed
            self.direction = "right"

        if not self.jumping:
            if keys[pygame.K_SPACE]:
                self.y_speed = -15
                self.jumping = True
        else:
            self.y_speed += 0.5

        self.y += self.y_speed

        if self.y >= ground_y - self.height:
            self.y = ground_y - self.height
            self.jumping = False
            self.y_speed = 0

    def draw(self, screen):
        player_image = self.player_frames[self.frame_index]
        if self.direction == "left":
            player_image = pygame.transform.flip(player_image, True, False)
        screen.blit(player_image, (self.x, self.y))