import pygame
from pygame import gfxdraw


class ShapeRhombusPencil:
    def __init__(self, x, y, bound):
        self.x = x
        self.y = y
        self.bound = bound

    def draw(self, WIN, x, y, bound, drawing_color):
        if bound:
            if bound:
                gfxdraw.aatrigon(WIN, x, y, x + 30, y, x + 15, y + 20, drawing_color)
                gfxdraw.aatrigon(WIN, x, y, x + 30, y, x + 15, y - 20, drawing_color)
                gfxdraw.filled_trigon(WIN, x, y, x + 30, y, x + 15, y + 20, drawing_color)
                gfxdraw.filled_trigon(WIN, x, y, x + 30, y, x + 15, y - 20, drawing_color)
                pygame.display.flip()
