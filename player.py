import pygame
from setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('./images/rabbit_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        # 人物的碰撞范围比实际像素小（长宽各少30像素）
        self.hitbox = self.rect.inflate(-30, HITBOX_OFFSET['player'])
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.obstacle_tree_sprites = obstacle_sprites
        self.obstacle_animal_sprites = obstacle_sprites
        # 人物状态
        self.stats = {'leaf': 1}
        self.leaf = self.stats['leaf']
        # 添加音效
        self.tree_attack_sound = pygame.mixer.Sound('./audio/slash.wav')
        self.tree_attack_sound.set_volume(0.2)

    # 将player移动和键盘上的上下左右按键绑定
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    # 让player移动的函数
    def move(self, speed):
        # 使人物朝斜着的方向移动时速度仍保持不变
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    # 检测碰撞方向，使人物从哪个方向试图穿过树都会被挡住
    def collision(self, direction):
        if direction == 'horizontal': # 两个if语句分别定义了从横纵两个方向碰撞的情况
            for sprite in self.obstacle_tree_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # 向右移动
                        self.hitbox.right = sprite.hitbox.left
                        self.tree_attack_sound.play()
                    if self.direction.x < 0:  # 向左移动
                        self.hitbox.left = sprite.hitbox.right
                        self.tree_attack_sound.play()
        if direction == 'vertical':
            for sprite in self.obstacle_tree_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # 向下移动
                        self.hitbox.bottom = sprite.hitbox.top
                        self.tree_attack_sound.play()
                    if self.direction.y < 0:  # 向上移动
                        self.hitbox.top = sprite.hitbox.bottom
                        self.tree_attack_sound.play()

    def update(self):
        self.input()
        self.move(self.speed)
