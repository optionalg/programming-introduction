#!/usr/bin/python

import pygame

pygame.init()

BLACK = (0, 0, 0)

done = False
clock = pygame.time.Clock()

display = pygame.display
display.set_caption("Python")
bounds = (600, 600)
screen = display.set_mode(bounds)

my_image = pygame.image.load("python-logo.png").convert()
w, h = my_image.get_size()
scale = 1
my_image = pygame.transform.scale(my_image, (int(w*scale), int(h*scale)))
w, h = my_image.get_size()

image_position = [(bounds[0] / 2) - (w / 2),
                  (bounds[1] / 2) - (h / 2)]


def loop():
    pos = pygame.mouse.get_pos()
    x = pos[0] - w/2
    y = pos[1] - h/2

    screen.blit(my_image, [x, y])

z







while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    surface = pygame.display.get_surface()
    surface.fill(BLACK)

    loop()

    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
pygame.quit()