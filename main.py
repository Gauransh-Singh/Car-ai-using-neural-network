import pygame
from car import Car
from road import Road
from sensor import Sensor
from network import Network

pygame.init()

WIDTH,HEIGHT = 1080, 720 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lets Race")
clock = pygame.time.Clock()


car = Car()
road = Road()
sensor = Sensor(car)
network = Network()

running = True

while running:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        car.accelerate()

    if keys[pygame.K_a]:
        car.steer(-0.8)

    if keys[pygame.K_d]:
        car.steer(0.8)

    if keys[pygame.K_s]:
        car.reverse()

    car.update_position()
    sensor.update(road)
    print(sensor.readings)

    if not road.is_on_road(car.x, car.y):
        print("OFF ROAD")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    road.draw(screen)
    car.draw(screen)
    sensor.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()