import pygame
from pygame import gfxdraw


class SaveBrush:
    def _init_(self):
        print("hello")

    def draw(self, WIN, color, polygon_points):
        pygame.draw.polygon(WIN, color, polygon_points)