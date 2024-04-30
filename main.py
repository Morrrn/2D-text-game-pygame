import pygame
import sys
from level import Level
from start import Start
from setting import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('森林派对 Forest Party')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.start = Start()
        # 游戏背景音乐
        main_sound = pygame.mixer.Sound('./audio/BGM.mp3')
        main_sound.set_volume(0.6)
        main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.start.run()
            pygame.display.update()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    while True:
                        for event1 in pygame.event.get():
                            if event1.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        bg_color = (173, 188, 58)
                        self.screen.fill(bg_color)
                        self.level.run()
                        pygame.display.update()
                        self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
