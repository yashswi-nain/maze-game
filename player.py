import pygame


class Player:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.speed = 5


def move(self, walls):

    keys = pygame.key.get_pressed()

    old_x = self.rect.x
    old_y = self.rect.y


    if keys[pygame.K_LEFT]:
        self.rect.x -= self.speed

    if keys[pygame.K_RIGHT]:
        self.rect.x += self.speed

    if keys[pygame.K_UP]:
        self.rect.y -= self.speed

    if keys[pygame.K_DOWN]:
        self.rect.y += self.speed


    # Wall collision
    for wall in walls:

        if self.rect.colliderect(wall):
            self.rect.x = old_x
            self.rect.y = old_y


    # Screen boundary
    if self.rect.left < 0:
        self.rect.left = 0

    if self.rect.right > 800:
        self.rect.right = 800

    if self.rect.top < 0:
        self.rect.top = 0

    if self.rect.bottom > 600:
        self.rect.bottom = 600


    def draw(self, screen):

        center_x = self.rect.centerx
        center_y = self.rect.centery


        # Pink petals
        pygame.draw.circle(
            screen,
            (255,105,180),
            (center_x, center_y-15),
            15
        )

        pygame.draw.circle(
            screen,
            (255,105,180),
            (center_x, center_y+15),
            15
        )

        pygame.draw.circle(
            screen,
            (255,105,180),
            (center_x-15, center_y),
            15
        )

        pygame.draw.circle(
            screen,
            (255,105,180),
            (center_x+15, center_y),
            15
        )


        # Yellow center
        pygame.draw.circle(
            screen,
            (255,220,0),
            (center_x, center_y),
            15
        )
