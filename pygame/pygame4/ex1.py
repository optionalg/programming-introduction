#!/usr/bin/python

import pygame

pygame.init()

BLACK = (0, 0, 0)

done = False
clock = pygame.time.Clock()

display = pygame.display
display.set_caption("Python")
bounds = (1024, 768)
screen = display.set_mode(bounds)
explosion_sound = pygame.mixer.Sound("explosion.ogg")


def make_explosion_image():

    image = pygame.image.load("explosion.png").convert_alpha()
    w, h = image.get_size()
    scale = 1
    image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return image

background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (1024,1024))
background_position = [0, 0]

player_image = pygame.image.load("car.png").convert_alpha()
w, h = player_image.get_size()
scale = 1
player_image = pygame.transform.scale(player_image, (int(w*scale), int(h*scale)))
w, h = player_image.get_size()

explosion_image = make_explosion_image()
global cursor_image
cursor_image = player_image


def loop(event):

    screen.blit(background_image, background_position)

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]



    def image_to_show(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return explosion_image
        else:
            return player_image

    image = image_to_show(event)

    if event.type == pygame.MOUSEBUTTONDOWN:
        explosion_sound.play()

    screen.blit(image, [x - image.get_rect().centerx, y - image.get_rect().centery])




while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    surface = pygame.display.get_surface()
    surface.fill(BLACK)

    loop(event)

    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
pygame.quit()