import pygame
import math

from utils import lerp


class Sensor:

    def __init__(self, car):

        self.car = car

        self.ray_count = 7
        self.ray_length = 150
        self.ray_spread = math.pi / 2

        self.rays = []
        self.readings = []


    def update(self, road):

        self.rays = []
        self.readings = []

        for i in range(self.ray_count):

            ray_angle = lerp(
                self.ray_spread / 2,
                -self.ray_spread / 2,
                i / (self.ray_count - 1)
            )

            ray_angle += self.car.angle

            start = (self.car.x, self.car.y)

            distance = self.ray_length

            for j in range(0, self.ray_length, 2):

                x = int(
                    self.car.x +
                    math.sin(ray_angle) * j
                )

                y = int(
                    self.car.y -
                    math.cos(ray_angle) * j
                )

                if not road.is_on_road(x, y):
                    distance = j
                    break

            end_x = (
                self.car.x +
                math.sin(ray_angle) * distance
            )

            end_y = (
                self.car.y -
                math.cos(ray_angle) * distance
            )

            end = (end_x, end_y)

            self.rays.append((start, end))

            self.readings.append(distance / self.ray_length)


    def draw(self, screen):

        for start, end in self.rays:

            pygame.draw.line(
                screen,
                (255, 0, 0),
                start,
                end,
                2
            )