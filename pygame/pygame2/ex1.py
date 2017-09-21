#!/usr/bin/python

import pygame

pygame.init()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# params
bounds = (600, 600)
square_side = 100
line_thickness = 5

display = pygame.display
display.set_caption("Such square.")
screen = display.set_mode(bounds)

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    surface = pygame.display.get_surface()
    surface.fill(BLACK)

    # square
    x_offset = (bounds[0] / 2) - (square_side / 2)
    y_offset = (bounds[1] / 2) - (square_side / 2)

    pygame.draw.line(screen,
                     GREEN,
                     [0 + x_offset, 0 + y_offset],
                     [0 + x_offset, square_side + y_offset],
                     line_thickness)

    pygame.draw.line(screen,
                     GREEN,
                     [0 + x_offset , square_side + y_offset],
                     [square_side + x_offset, square_side + y_offset],
                     line_thickness)

    pygame.draw.line(screen,
                     GREEN,
                     [square_side + x_offset, square_side + y_offset],
                     [square_side + x_offset, 0 + y_offset],
                     line_thickness)

    pygame.draw.line(screen,
                     GREEN,
                     [square_side + x_offset, 0 + y_offset],
                     [0 + x_offset, 0 + y_offset],
                     line_thickness)

    # display.update()

    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
pygame.quit()