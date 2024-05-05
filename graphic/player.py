import pygame

class Player(pygame.sprite.Sprite):
    def __init__ (self, pos, group):
        super().__init__(group)

        self.image = pygame.surface((64,32))
        self.image.fill('green')
        self.rect = self.image_get_rect(center = pos)
        ##################################################