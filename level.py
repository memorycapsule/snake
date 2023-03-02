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
            (random.randrange(48, util.width - 192, 32),
             random.randrange(48, util.height - 192, 32)),
            self.all_sprites)

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.drawGrid(self.display_surface)
        self.player.draw_segments(self.display_surface)
        if self.player.out_of_bounds(self.player) or self.player.tail_collision_check():
            self.reload()
        self.all_sprites.update(dt)
        # drawing segments is not working
        self.player.update(dt)

        if self.food.colision_check(self.player):
            self.player.add_segment()
            self.food.kill()
            self.food = Food(pygame.Vector2((random.randrange(48, util.width - 192, 32),
                                             random.randrange(48, util.height - 192, 32)),), self.all_sprites)

    def reload(self):
        self.all_sprites.empty()
        self.setup()

    def drawGrid(self, surface):
        blockSize = 32
        for x in range(0, util.width, blockSize):
            for y in range(0, util.height, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(surface, "white", rect, 1)
