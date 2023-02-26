import pygame
import util
from level import Level
# Display Surface


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()  # the same as sys.exit()?
            # Delta Time
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
