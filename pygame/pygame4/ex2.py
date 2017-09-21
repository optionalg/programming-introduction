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

player_position = [0, 0]

def car_rect():
    return pygame.Rect(player_position[0], player_position[1], w, h)


def speed_from_event(event):

    x_speed = 0
    y_speed = 0
    velocity = 10
    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        if event.key == pygame.K_LEFT:
            x_speed = -velocity
        elif event.key == pygame.K_RIGHT:
            x_speed = velocity
        elif event.key == pygame.K_UP:
            y_speed = -velocity
        elif event.key == pygame.K_DOWN:
            y_speed = velocity
    # User let up on a key
    elif event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_speed = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_speed = 0

    return (x_speed, y_speed)


def image_to_show(collided):
    if collided:
        return explosion_image
    else:
        return player_image



def loop(event):

    screen.blit(background_image, background_position)

    x_speed, y_speed = speed_from_event(event)

    player_position[0] += x_speed
    player_position[1] += y_speed

    car_rect = pygame.Rect(player_position[0], player_position[1], w, h)
    collided_wall = collided(car_rect, bounds)
    image = image_to_show(collided_wall)
    if collided_wall:
        if not pygame.mixer.get_busy():
            explosion_sound.play()




    screen.blit(image, [player_position[0],
                        player_position[1]])




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