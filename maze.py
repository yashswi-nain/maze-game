import pygame


walls = [
    pygame.Rect(150,100,400,20),
    pygame.Rect(150,100,20,250),
    pygame.Rect(300,250,300,20),
    pygame.Rect(600,250,20,200),
    pygame.Rect(200,450,400,20)
]


def draw(screen):

    for wall in walls:
        pygame.draw.rect(
            screen,
            (255,0,150),
            wall
        )
def get_walls():
    return walls        