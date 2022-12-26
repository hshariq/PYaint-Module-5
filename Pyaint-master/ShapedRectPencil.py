import pygame
from pygame import gfxdraw


class ShapedRectPencil:
    def __init__(self, corners, bound):
        self.corners = corners
        self.bound = bound

    def draw(self, WIN, corners, bound, drawing_color):
        if bound:
            gfxdraw.aapolygon(WIN, corners, drawing_color)
            gfxdraw.filled_polygon(WIN, corners, drawing_color)
