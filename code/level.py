import pygame
from settings import *
from player import Player

class Level:
    ##################################################
    def __init__(self):

        # get the display surface 
        self.display_surface = pygame.display.get_surface()

        # sprite 
        self.all_sprites = pygame.sprite.Group()

        # setup
        self.setup()
    ##################################################
    def setup(self):
        self.player = Player((640,360), self.all_sprites)
    ##################################################
    def run_game(self, dt):
        self.display_surface.fill('yellow')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
