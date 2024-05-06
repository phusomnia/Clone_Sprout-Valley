import pygame
from support import *
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_asserts()
        self.status = 'down_idle'
        self.frame_index = 0

        # Init image of player 
        # self.image = pygame.Surface((64,32))
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    
        # Init direction of player
        self.direction_of_player = pygame.math.Vector2() 
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
    ##################################################
    def animate(self, dt):
        self.frame_index += 4 * dt
        self.image = self.animation[self.animations][self.frame_index]
    ##################################################
    def import_asserts(self):
        self.animations = {'left': [],'up': [],'down': [],'right': [],
                           'left_idle': [],'up_idle': [],'down_idle': [],'right_idle': [],
                           'left_hoe': [],'up_hoe': [],'down_hoe': [],'right_hoe': [],
                           'left_axe': [],'up_axe': [],'down_axe': [],'right_axe': [],
                           'left_water': [],'up_water': [],'down_water': [],'right_water': []}
        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)
    ##################################################
    def input_from_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            print('right')
            self.direction_of_player.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            print('left')
            self.direction_of_player.x = -1
        else:
            self.direction_of_player.x = 0
        
        # up and down movement of player
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            print('up')
            self.direction_of_player.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            print('down')
            self.direction_of_player.y = 1
        else:
            self.direction_of_player.y = 0
    ##################################################
    def movement_of_player(self, dt):

        # normalizing vector 
        if self.direction_of_player.magnitude() > 0:
            self.direction_of_player = self.direction_of_player.normalize()
        # print(self.direction_of_player)

        # # global movement
        # self.pos += self.direction_of_player * self.speed * dt
        # self.rect.center = self.pos 
        # vertical movemnt
        self.pos.y += self.direction_of_player.y * self.speed * dt
        self.rect.centery = self.pos.y
        # horizontal movement 
        self.pos.x += self.direction_of_player.x * self.speed * dt
        self.rect.centerx = self.pos.x
    ##################################################
    def update(self, dt):
        self.input_from_keyboard()
        self.movement_of_player(dt)
        