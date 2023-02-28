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
        self.length = 1
        self.speed = 2
        # one segment
        self.time_now = pygame.time.get_ticks()
        self.segments = [self.rect.copy()]

    def update(self, dt):
        self.input()
        self.move(dt)

    def input(self):
        keys = pygame.key.get_pressed()

        print(self.direction)

        if keys[pygame.K_LEFT]:
            self.direction = [-1, 0]
        elif keys[pygame.K_RIGHT]:
            self.direction = [1, 0]
        elif keys[pygame.K_UP]:
            self.direction = [0, -1]
        elif keys[pygame.K_DOWN]:
            self.direction = [0, 1]

    def move(self, dt):
        # can do smthin like self.rect.move_ip(self.direction * self.speed * dt)
        self.rect.move_ip(self.direction)
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].center = self.segments[i-1].center
        self.segments[0].center = self.rect.center

    def addsegment(self):
        segment = Segments(self.segments[-1].copy(), [pygame.sprite.Group()])
        self.segments.append(segment)

    def draw_segments(self, surface):
        [pygame.draw.rect(surface, 'red', segment)
         for segment in self.segments]

        # for segment in self.segments:
        # pygame.draw.rect(snake_surface, (255, 255, 255), segment)
        # surface.blit(snake_surface, self.rect)
    def colision_check(self, other):
        return self.rect.colliderect(other.rect)
