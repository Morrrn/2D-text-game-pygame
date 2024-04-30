import pygame
from tile import *
from player import *


class incident_fox1():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        text = pygame.image.load('./text/text_fox1.png')
        self.display_surface.blit(text, (120, 200))


class incident_fox2():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        text = pygame.image.load('./text/text_fox2.png')
        self.display_surface.blit(text, (120, 200))
        reward = pygame.image.load('./images/leaf.png')
        self.display_surface.blit(reward, (10, 40))


class incident_squirrel1():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        text = pygame.image.load('./text/text_squirrel1.png')
        self.display_surface.blit(text, (120, 200))


class incident_squirrel2():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        text = pygame.image.load('./text/text_squirrel2.png')
        self.display_surface.blit(text, (120, 200))


class incident_wolf1():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        text = pygame.image.load('./text/text_wolf1.png')
        self.display_surface.blit(text, (120, 200))


class incident_ending1():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        text = pygame.image.load('./text/text_ending.png')
        self.display_surface.blit(text, (0, 0))


class picture_happy_ending():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        pic = pygame.image.load('./images/happy_ending.png')
        self.display_surface.blit(pic, (320, 192))
