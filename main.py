###########################################
# Flyweight
# taken from: https://sourcemaking.com/design_patterns/flyweight/python/1
# on: 02/29/2023
###########################################


from FlyweightFactory import *
import pygame
import sys
from pympler import asizeof
from datetime import datetime

screen = pygame.display.set_mode((320, 320), 0, 32)
bg_color = (0, 0, 0)
mainloop = True

size = 20

flyweight_factory = FlyweightFactory()
pixel_color_list = [
    flyweight_factory.get_flyweight("white, circle"),
    flyweight_factory.get_flyweight("white, rect"),
    flyweight_factory.get_flyweight("white, rect"),
    flyweight_factory.get_flyweight("red, circle"),
    flyweight_factory.get_flyweight("red, circle"),
    flyweight_factory.get_flyweight("white, rect"),
    flyweight_factory.get_flyweight("white, circle"),
    flyweight_factory.get_flyweight("red, rect"),
    flyweight_factory.get_flyweight("white, circle"),
    flyweight_factory.get_flyweight("black, rect"),
    flyweight_factory.get_flyweight("red, circle"),
]

startTime = datetime.now()

current_x = 0
current_y = 0

screen.fill(bg_color)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()

count = 0

for pixel in pixel_color_list:

    if count == 16:
        current_y += size
        current_x = 0
        count = 0

    if count > 0:
        current_x += size

    if pixel.shape != "rect":
        pygame.draw.circle(screen, pixel.color, (current_x + size / 2, current_y + size / 2), size / 2)
    else:
        pygame.draw.rect(screen, pixel.color, (current_x, current_y, size, size))
    count += 1

pygame.display.flip()
pygame.time.delay(3000)

print(asizeof.asizeof(pixel_color_list))
print(datetime.now() - startTime)
