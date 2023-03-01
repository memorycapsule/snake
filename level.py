import pygame
from snake import Snake
import util
from food import Food
import random


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Snake((util.width//2, util.width//2), self.all_sprites)
        # Position the food to spawn within the grids
        self.food = Food(
            (random.randrange(32 + 16, util.width - 32 - 16, 32),
             random.randrange(32 + 16, util.width - 32 - 16, 32)),
            self.all_sprites)

    def run(self, dt):
        self.display_surface.fill('black')
        time_now = pygame.time.get_ticks()
        self.all_sprites.draw(self.display_surface)

        # update every 500 ms?
        if time_now - 500 == 0:
            self.all_sprites.update(dt)
        # drawing segments is not working
        self.player.draw_segments(self.display_surface)
        self.player.update(dt)

        if self.food.colision_check(self.player):
            self.player.add_segment()
            self.food.kill()
            self.food = Food(pygame.Vector2((random.randrange(32 + 16, util.width - 32 - 16, 32),
                                             random.randrange(32 + 16, util.width - 32 - 16, 32)),), self.all_sprites)
