#!/usr/bin/python

import pygame
import math

pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

done = False
clock = pygame.time.Clock()

display = pygame.display
display.set_caption("Python")
bounds = (1024, 768)
screen = display.set_mode(bounds)

my_image = pygame.image.load("python-logo.png").convert()
w, h = my_image.get_size()
scale = 1
my_image = pygame.transform.scale(my_image, (int(w*scale), int(h*scale)))
w, h = my_image.get_size()

rect_x = 300
rect_y = 300
velocity = 100

angle = 60


def delta_from_angle(angle):
    angle_radians = angle * (math.pi / 180)
    x_delta = math.cos(angle_radians) * velocity
    y_delta = math.sin(angle_radians) * velocity
    return (x_delta, y_delta)


def collided(rect, bounds):

    rect = pygame.Rect(rect)
    if rect.right > bounds[0]:
        return "right"
    elif rect.left < 0:
        return "left"
    elif rect.bottom > bounds[1]:
        return "bottom"
    elif rect.top < 0:
        return "top"
    else:
        return False


def exit_angle(enter_angle, collided_wall):

    exit_angle = 0
    if collided_wall == "bottom" or collided_wall == "top":
        exit_angle = 360 - enter_angle
    elif collided_wall == "left" or collided_wall == "right":
        exit_angle = 180 - enter_angle
    else:
        exit_angle = enter_angle

    return exit_angle


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    surface = pygame.display.get_surface()
    surface.fill(BLACK)



    delta_x, delta_y = delta_from_angle(angle)
    rect_x += delta_x
    rect_y += delta_y

    x = rect_x
    y = rect_y

    screen.blit(my_image, [x, y])


    image_rect = pygame.Rect(rect_x, rect_y, w, h)

    pygame.draw.rect(screen, GREEN, image_rect, 1)

    collided_wall = collided(image_rect, bounds)
    if collided_wall != False:
        angle = exit_angle(angle, collided_wall)


    pygame.display.flip()
    clock.tick(200)

# Close the window and quit.
pygame.quit()






assert collided(pygame.Rect(0, 0, 10, 10), (100, 100)) == False
assert collided(pygame.Rect(-1, 0, 10, 10), (100, 100)) == "left"
assert collided(pygame.Rect(90, 0, 10, 10), (100, 100)) == False
assert collided(pygame.Rect(91, 0, 10, 10), (100, 100)) == "right"
assert collided(pygame.Rect(0, 90, 10, 10), (100, 100)) == False
assert collided(pygame.Rect(0, -1, 10, 10), (100, 100)) == "top"
assert collided(pygame.Rect(0, 90, 10, 10), (100, 100)) == False
assert collided(pygame.Rect(0, 91, 10, 10), (100, 100)) == "bottom"

# assert exit_angle(45, "bottom") == -45
# assert exit_angle(135, "bottom") == -135
# assert exit_angle(90, "bottom") == 90
# assert exit_angle(100, "bottom") == 80
# assert exit_angle(135, "bottom") == 45
# assert exit_angle(170, "bottom") == 10
# assert exit_angle(225, "bottom") == 135




