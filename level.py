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
        self.player = Snake((util.width/2, util.width/2), self.all_sprites)
        self.food = Food((random.randint(0, util.width),
                         random.randint(0, util.height)), self.all_sprites)

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        self.player.draw(self.display_surface)

        if self.food.colision_check(self.player):
            self.player.addsegment()
            self.food.kill()
            self.food = Food((random.randint(0, util.width),
                             random.randint(0, util.height)), self.all_sprites)
