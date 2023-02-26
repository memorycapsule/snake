import pygame

# Maybe segments should be a sprite group?


class Segments(pygame.sprite.Sprite):
    def __init__(self, rect, group):
        super().__init__(group)
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
        self.rect = rect
