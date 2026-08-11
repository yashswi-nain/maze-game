import pygame

from player import Player
from maze import draw, get_walls


pygame.init()


WIDTH = 800
HEIGHT = 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Neon Escape: AI Maze Runner")


clock = pygame.time.Clock()


# TIMER STARTS HERE
start_time = pygame.time.get_ticks()

font = pygame.font.Font(None,40)


player = Player(100,100)

walls = get_walls()


running = True

while running:
 screen.fill((5,5,20))


draw(screen)

player.move(walls)

player.draw(screen)


seconds = (pygame.time.get_ticks() - start_time)//1000


timer_text = font.render(
    f"Time: {seconds}",
    True,
    (255,255,255)
)


screen.blit(timer_text,(20,20))

pygame.display.update()
for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


screen.fill((5,5,20))

player.move(walls)
draw(screen)
player.draw(screen)

pygame.display.update()

clock.tick(60)