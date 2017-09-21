#!/usr/bin/python

import pygame

pygame.init()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# params
bounds = (600, 600)

rect_side = 200
rect_x = (bounds[0] / 2) - rect_side / 2
x_offset = rect_side
y_offset = rect_side
scale = 100

display = pygame.display
display.set_caption("Such function.")
screen = display.set_mode(bounds)

done = False
clock = pygame.time.Clock()

font = pygame.font.SysFont('Monaco', 25, True, False)
text = font.render("f(x) = 1 / x", True, WHITE)

graph_x_offset = x_offset + (rect_side / 2)
graph_y_offset = y_offset + (rect_side / 2)
dot_size = 5

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    surface = pygame.display.get_surface()
    surface.fill(BLACK)

    for x in range(-int(rect_side/2), int(rect_side/2)):

        if x == 0:
            continue

        y = 1 / (x/scale)

        pygame.draw.line(screen,
                         GREEN,
                         [x + graph_x_offset, y + graph_y_offset],
                         [x + dot_size + graph_x_offset, y + graph_y_offset],
                         dot_size)

    pygame.draw.rect(screen,
                     WHITE,
                     [0 + x_offset, 0 + y_offset, rect_side, rect_side],
                     1)

    screen.blit(text, [(bounds[0] / 2) - (rect_side / 4),
                       (bounds[1] / 2) + rect_side])

    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
pygame.quit()