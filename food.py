import util
import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((32, 32))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)

    def colision_check(self, snake):
        return self.rect.colliderect(snake.rect)
