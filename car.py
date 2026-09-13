import pygame
import math


class Car:
    def __init__(self):
        self.my_car_image = pygame.image.load('assets/My Porche.png')
        self.x = 700
        self.y = 650

        self.width = 30
        self.height = 45


        self.my_car_image = pygame.transform.scale(
            self.my_car_image,
            (self.width, self.height)
        )

        self.rect = self.my_car_image.get_rect(center = (self.x, self.y))

        self.speed = 0
        self.max_speed = 3
        self.friction = 0.05
        self.angle = -math.pi / 2
        self.steering_strength = 0.04


    def update_position(self):
        self.x += self.speed * math.sin(self.angle)
        self.y -= self.speed * math.cos(self.angle)

        if self.speed > 0:
            self.speed -= self.friction

            if self.speed < 0:
                self.speed = 0

        elif self.speed < 0:
            self.speed += self.friction

            if self.speed > 0:
                self.speed = 0

        self.rect.center = (self.x, self.y)


    def accelerate(self):
        self.speed += 0.1 

        if self.speed > self.max_speed:
            self.speed = self.max_speed


    def reverse(self):
        self.speed -= 0.1

        if self.speed < -self.max_speed:
            self.speed = -self.max_speed 


    def steer(self, direction):
        if self.speed == 0:
            return

        speed_factor = min(abs(self.speed) / self.max_speed, 1.0)
        turn_amount = direction * self.steering_strength * speed_factor

        if self.speed >= 0:
            self.angle += turn_amount
        else:
            self.angle -= turn_amount


    def draw(self, screen):
        rotated_image = pygame.transform.rotate(
            self.my_car_image,
            -math.degrees(self.angle)
        )

        rotated_rect = rotated_image.get_rect(
            center=self.rect.center
        )

        screen.blit(rotated_image, rotated_rect)