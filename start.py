import pygame


class Start:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        # 更新
        text = pygame.image.load('./text/start_text_all.png')
        self.display_surface.blit(text, (112.5, 112.5))
