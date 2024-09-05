import pygame
import sys
from pygame import gfxdraw
import datetime
from math import sin, cos, pi, radians


# Setting display
WIDTH, HEIGHT = 1500, 1000
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 400
# Init set up
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("J4F")
FPS = 60

# Visual
CLOCK = (33, 35, 57)
BACKGROUND = (217, 215, 211)
RED = (255, 0, 0)
YELLOW = (221, 170, 34)
image_surface = pygame.image.load(
    "/Users/andylenguyen/Documents/A-day-by-Andy/night.png")
image_surface = pygame.transform.scale(
    image_surface, (220, 200))


def numbers(number, size, position):
    font = pygame.font.Font(
        "/Users/andylenguyen/Documents/A-day-by-Andy/Dubai-Regular.ttf", size)
    text = font.render(number, True, CLOCK)
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)


def polar_to_cartesian(radius, theta):
    x = radius * sin(pi * theta / 180)
    y = radius * cos(pi * theta / 180)
    return x + WIDTH / 2, - (y - HEIGHT / 2)


def write_description(text, size, position, font_file, text_rotate_degress=0, align="center"):
    font = pygame.font.Font(
        "/Users/andylenguyen/Documents/A-day-by-Andy/calibri-regular.ttf", size)
    text_surface = font.render(text, True, CLOCK)
    rotated_text_surface = pygame.transform.rotate(
        text_surface, text_rotate_degress)

    text_rect = text_surface.get_rect()

    if align == "right":
        text_rect.topright = position
    elif align == 'left':
        text_rect.topleft = position
    else:
        text_rect.center = position

    screen.blit(text_surface, text_rect)


def update_background():
    currenthour = datetime.datetime.now().hour

    # night
    if 6 < currenthour < 14:
        pass
    # afternoon
    elif 14 <= currenthour < 16:
        pass
    # morning
    elif 12 <= currenthour < 6:
        pass
    # noon
    else:
        pass


def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND)

        # draw circles
        pygame.draw.circle(screen, CLOCK, center, clock_radius - 10, 5)
        pygame.draw.circle(screen, CLOCK, center, clock_radius - 2, 2)
        gfxdraw.aacircle(screen, int(center[0]), int(
            center[1]), clock_radius - 2 + 1, CLOCK)
        gfxdraw.aacircle(screen, int(center[0]), int(
            center[1]), clock_radius - 2, CLOCK)
        gfxdraw.aacircle(screen, int(center[0]), int(
            center[1]), clock_radius - 2 - 1, CLOCK)

        for number in range(1, 25):
            numbers(str(number), 40, polar_to_cartesian(
                clock_radius + 30, number * 15))

        for number in range(0, 360, 15):
            width = 3
            if (number % 90) == 0:
                width = 9
            pygame.draw.line(screen, CLOCK, polar_to_cartesian(
                clock_radius + 8, number), polar_to_cartesian(clock_radius - 22, number), width)

        # display dividing line
        rb = 24
        thetas = [0*rb, 20*rb, 21*rb, 22.5*rb,
                  23.5*rb, 26*rb, 28.5*rb, 29.5*rb]
        for theta in thetas:
            pygame.draw.line(screen, CLOCK, polar_to_cartesian(
                clock_radius - 40, theta), polar_to_cartesian(clock_radius - 335, theta), 3)

        # description
        screen.blit(image_surface, (WIDTH / 2 + 30, HEIGHT / 2 - 300))
        write_description(u"Sleep", 40, (WIDTH / 2 + 300, HEIGHT / 2 - 60),
                          "/Users/andylenguyen/Documents/A-day-by-Andy/Dubai-Regular.ttf", 8, 'right')
        write_description(u"Breakfast", 35, (WIDTH / 2 + 280, HEIGHT / 2 + 160),
                          "/Users/andylenguyen/Documents/A-day-by-Andy/Dubai-Regular.ttf", 100, 'right')
        write_description(u"Study", 40, (WIDTH / 2 + 120, HEIGHT / 2 + 200),
                          "/Users/andylenguyen/Documents/A-day-by-Andy/Dubai-Regular.ttf", 100, 'right')
        write_description(u"Lunch", 35, (WIDTH / 2 - 5, HEIGHT / 2 + 200),
                          "/Users/andylenguyen/Documents/A-day-by-Andy/Dubai-Regular.ttf", 100, 'right')
        write_description(u"Study", 40, (WIDTH / 2 - 150, HEIGHT / 2 + 160),
                          "/Users/andylenguyen/Documents/A-day-by-Andy/Dubai-Regular.ttf", 100, 'right')
        write_description(u"Dinner", 40, (WIDTH / 2 - 150, HEIGHT / 2 - 130),
                          "/Users/andylenguyen/Documents/A-day-by-Andy/Dubai-Regular.ttf", 100, 'right')
        write_description(u"Study", 35, (WIDTH / 2 - 80, HEIGHT / 2 - 280),
                          "/Users/andylenguyen/Documents/A-day-by-Andy/Dubai-Regular.ttf", 100, 'right')

        # change background based on time
        # screen.blit(update_background(), (0, 0))

        # clock time
        current = datetime.datetime.now()
        hour = current.hour
        minute = current.minute
        second = current.second

        r = 130
        theta = (hour + minute / 60 + second / 3600) * (360 / 24)
        pygame.draw.line(screen, YELLOW, center,
                         polar_to_cartesian(r, theta), 14)

        r = 280
        theta = (minute + second / 60) * (360 / 60)
        pygame.draw.line(screen, YELLOW, center,
                         polar_to_cartesian(r, theta), 10)

        r = 340
        theta = second * (360 / 60)
        pygame.draw.line(screen, YELLOW, center,
                         polar_to_cartesian(r, theta), 4)
        pygame.draw.line(screen, YELLOW, center,
                         polar_to_cartesian(80, (theta + 180) % 360), 4)

        r = 130
        # play button
        gfxdraw.filled_circle(screen, int(center[0]), int(
            center[1]), clock_radius - 350, YELLOW)
        pygame.draw.circle(screen, CLOCK, center, clock_radius - 350, 2)
        write_description("START", 30, (WIDTH/2, HEIGHT/2 + 3),
                          "/Users/andylenguyen/Documents/A-day-by-Andy/Dubai-Regular.ttf'", 0)

        pygame.display.update()
        pygame.display.flip()

        clock.tick(FPS)


main()
