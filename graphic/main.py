import pygame, sys
from level import Level

class Game:
    ##################################################
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Sprout Valley')

        self.clock = pygame.time.Clock()
        self.level = Level()
    ##################################################
    def run_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run_game(dt)
            pygame.display.update()
    ##################################################
if __name__ == '__main__':
    game = Game()
    game.run_screen()         