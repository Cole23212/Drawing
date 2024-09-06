import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

display_surface.fill(WHITE)

START = (100,100)
END = (500,500)
pygame.draw.line(display_surface, BLACK, START, END, 20)

STart = (500,100)
ENd = (100,500)
pygame.draw.line(display_surface, BLACK, STart, ENd, 20)

CENTER = (300,300)
RADIUS = 100
pygame.draw.circle(display_surface, CYAN, CENTER, RADIUS)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
