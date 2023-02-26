import util
import pygame
from segments import Segments


class Snake(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        # one segment
        self.segments = [self.rect.copy()]

    def update(self, dt):
        self.input()
        self.move(dt)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].center = self.segments[i-1].center
        self.segments[0].center = self.rect.center

    def addsegment(self):
        segment = Segments(self.segments[-1].copy(), [pygame.sprite.Group()])
        self.segments.append(segment)

    def draw(self, surface):
        snake_surface = pygame.Surface((16, 16))
        snake_surface.fill((255, 0, 0))
        for segment in self.segments:
            pygame.draw.rect(snake_surface, (255, 255, 255), segment)
        surface.blit(snake_surface, self.rect)
