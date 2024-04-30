import pygame
from setting import *
from tile import Tile, Grass, Tree, Fox, Wolf, Squirrel
from player import Player
from ui import UI
from npc import *
from player import *


class Level:
    def __init__(self):
        # 获得游戏界面
        self.display_surface = pygame.display.get_surface()
        # 设置sprite组
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.incident_sprites = pygame.sprite.Group()
        self.can_incident_sprites = pygame.sprite.Group()
        # 设置sprite
        self.create_map()
        self.ui = UI()

    # 绘制地图，包括地图上的树、草、人物图标
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'l':
                    Leaf((x, y), [self.visible_sprites])
                if col == 'c':
                    Tile((x, y), [self.visible_sprites])
                if col == 'g':
                    Grass((x, y), [self.visible_sprites])
                if col == 's':
                    Tree((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'q':
                    q = Squirrel((x, y), [self.visible_sprites, self.obstacle_sprites, self.can_incident_sprites])
                if col == 'f':
                    f = Fox((x, y), [self.visible_sprites, self.obstacle_sprites, self.can_incident_sprites])
                if col == 'w':
                    w = Wolf((x, y), [self.visible_sprites, self.obstacle_sprites, self.can_incident_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites, self.incident_sprites], self.obstacle_sprites)

    def incident_logic(self):
        if self.incident_sprites:
            for incident_sprite in self.incident_sprites:
                collision_sprites = pygame.sprite.spritecollide(incident_sprite, self.can_incident_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'fox':
                            self.incident_fox1 = incident_fox1()
                            self.incident_fox1.run()
                            # 此处的+1问题，在ui.py中有解释
                            self.player.leaf += 1
                        elif target_sprite.sprite_type == 'squirrel':
                            self.incident_squirrel2 = incident_squirrel2()
                            self.incident_squirrel2.run()
                            self.player.leaf += 1
                        elif target_sprite.sprite_type == 'wolf':
                            self.incident_wolf1 = incident_wolf1()
                            self.incident_wolf1.run()
                            self.player.leaf += 1

        # 切换结尾
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.incident_ending1 = incident_ending1()
            self.incident_ending1.run()
            self.player.leaf = 0
            if self.incident_sprites:
                for incident_sprite in self.incident_sprites:
                    incident_sprite.kill()
                for incident_sprite in self.can_incident_sprites:
                    incident_sprite.kill()
        elif keys[pygame.K_SPACE]:
            self.picture_happy_ending = picture_happy_ending()
            self.picture_happy_ending.run()

    def run(self):
        # 更新并绘制游戏
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)

        # 人物交互
        self.incident_logic()


# 用来控制人物始终在镜头的中心
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        # 设置背景
        self.floor_surf = pygame.image.load('./images/bg_1.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # 绘制人物
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # 绘制背景
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
