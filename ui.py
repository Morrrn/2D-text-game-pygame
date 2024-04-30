import pygame
from setting import *


class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.bar_rect = pygame.Rect(10, 10, BAR_WIDTH, BAR_HIGHT)

    def show_bar(self, current, max_amount, bg_rect, color):
        # 绘制叶子拥有数进度条
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        ratio = current / 100
        current_width = 0.1 * bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        # 绘制左上角计数获得金叶子的数量
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, current_rect, 3)
        if current > 100: # 当进度条达到某个数值时，就增加一个金叶子图标
            self.display_surface.blit(pygame.image.load('./images/leaf.png'), (8, 20))
        if current > 600:
            self.display_surface.blit(pygame.image.load('./images/leaf.png'), (52, 20))
        if current > 900:
            self.display_surface.blit(pygame.image.load('./images/leaf.png'), (94, 20))

    def display(self, player):
        self.show_bar(player.leaf, player.stats['leaf'], self.bar_rect, LEAF_COLOR)
