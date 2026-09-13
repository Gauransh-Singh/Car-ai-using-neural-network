import pygame
import math
from utils import lerp

class Sensor:
    def _init_(self, car):
        self.car = car
        self.ray_count = 3;
        self.ray_length = 100
        self.ray_spread = math.pi / 4

        self.rays = []

    def update(self):
        self. rays = []
        for i in range(self.ray_count):
            RAY_ANGLE = lerp(
            self.ray_spread / 2,
            -self.ray_spread /2,
            i/(self.ray_count - 1)