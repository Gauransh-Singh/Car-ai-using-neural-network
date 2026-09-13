import pygame


class Road:
    def __init__(self):
        self.width = 1080
        self.height = 720

        self.track_image = pygame.image.load(
            'assets/track1.png'
        ).convert()

        self.track_image = pygame.transform.scale(
            self.track_image,
            (self.width, self.height)
        )

        self.road_mask = pygame.mask.from_threshold(
            self.track_image,
            (0, 0, 0),
            (10, 10, 10)
        )

    def draw(self, screen):
        screen.blit(self.track_image, (0, 0))

    def is_on_road(self, x, y):
        x = int(x)
        y = int(y)

        # Make sure the position is inside the track image
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False

        return self.road_mask.get_at((x, y))