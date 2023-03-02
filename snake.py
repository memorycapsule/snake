import util
import pygame
from segments import Segments


class Snake(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)

        self.segments = [self.rect.copy()]
        self.direction = pygame.math.Vector2(0, 0)
        self.length = 1
        self.speed = .1
        self.last_time, self.time_delay = 0, 200

    def update(self, dt):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_time >= self.time_delay:
            self.last_time = time_now
            self.move(dt)

        self.input()
        self.draw_segments(self.image)

    def input(self):
        keys = pygame.key.get_pressed()

        print(self.direction)

        if keys[pygame.K_LEFT]:
            self.direction = pygame.Vector2(-32, 0)
        elif keys[pygame.K_RIGHT]:
            self.direction = pygame.Vector2(32, 0)
        elif keys[pygame.K_UP]:
            self.direction = pygame.Vector2(0, -32)
        elif keys[pygame.K_DOWN]:
            self.direction = pygame.Vector2(0, 32)

    def move(self, dt):
        self.rect.move_ip(self.direction)
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].center = self.segments[i-1].center
        self.segments[0].center = self.rect.center

    def add_segment(self):
        self.segments.append(self.segments[-1].copy())

    def draw_segments(self, surface):
        # Working on this part
        [pygame.draw.rect(surface, 'blue', segment) if segment != self.segments[0] else pygame.draw.rect(
            surface, 'red', segment) for segment in self.segments]

    def colision_check(self, other):
        return self.rect.colliderect(other.rect)

    def tail_collision_check(self):
        pass
        # OK needs to be fixed
        # return [True for segment in self.segments if self.rect.colliderect(segment)]

    def out_of_bounds(self, snake):
        if snake.rect.x < 0 or snake.rect.x > util.width or snake.rect.y < 0 or snake.rect.y > util.height:
            return True
        return False
