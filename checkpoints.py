
import pygame

class Checkpoint:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, screen):
        pygame.draw.line(
            screen,
            (255, 215, 0),
            self.start,
            self.end,
            4
        )


class Checkpoints:
    def __init__(self):
        self.points = [
            Checkpoint((300, 300), (350, 210)),
            Checkpoint((150, 382), (150, 475)),
            Checkpoint((820, 382), (910, 382)),
            Checkpoint((985, 382), (1070, 382)),
            Checkpoint((900, 30), (900, 125))
        ]

    def check_checkpoint(self, car_x, car_y, checkpoint_index):
        checkpoint = self.points[checkpoint_index]

        x1, y1 = checkpoint.start
        x2, y2 = checkpoint.end

        mid_x = (x1 + x2)/2
        mid_y = (y1 + y2)/2

        distance = (
            (car_x - mid_x)** 2 +
            (car_y - mid_y)** 2
        )** 0.5
        return distance < 25 

    def draw(self, screen):
        for checkpoint in self.points:
            checkpoint.draw(screen)
