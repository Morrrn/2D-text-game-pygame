import pygame
from setting import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./images/grass_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class Grass(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./images/grass_2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class Leaf(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./images/leaf.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./images/03.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        # 树木是障碍物，不能穿过的，且碰撞范围比图像大小小20像素
        self.hitbox = self.rect.inflate(-20, -20)


class Fox(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./images/fox_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -20)
        self.sprite_type = 'fox'


class Wolf(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./images/wolf_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -20)
        self.sprite_type = 'wolf'


class Squirrel(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./images/squirrel_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -20)
        self.sprite_type = 'squirrel'
