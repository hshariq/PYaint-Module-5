import pygame
from pygame import gfxdraw


class ShapeCirclePencil:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, WIN, x, y, drawing_color):
        gfxdraw.aacircle(WIN, x, y, 10,  drawing_color)
        gfxdraw.filled_circle(WIN, x, y, 10,  drawing_color)
