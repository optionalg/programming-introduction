#!/usr/bin/python

import pygame

pygame.init()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

rect_frame = [image_position[0],
              image_position[1],
              w,
              h]

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    surface = pygame.display.get_surface()
    surface.fill(BLACK)

    screen.blit(my_image, image_position)
    pygame.draw.rect(screen, WHITE, rect_frame, 1)

    # display.update()
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
pygame.quit()