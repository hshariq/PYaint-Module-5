import pygame


class MultiLine:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, WIN, start, end):
        x, y = start
        x1, y1 = end
        changeX = x1 - x
        if changeX == 0:
            changeX = 0.00001
        changeY = y1 - y
        gradient = changeY / changeX
        absM = abs(gradient)
        # for straighter lines that have may have a gradient equivalent to infinity since diff in x v less
        if absM > 3:
            pygame.draw.line(WIN, (0, 0, 0), (x + 20, y), (x1 + 20, y1))
            pygame.draw.line(WIN, (0, 0, 0), start, end)
            pygame.draw.line(WIN, (0, 0, 0), (x - 20, y), (x1 - 20, y1))
        # for lines that have may have change in y<change in x
        else:
            pygame.draw.line(WIN, (0, 0, 0), (x, y + 20), (x1, y1 + 20))
            pygame.draw.line(WIN, (0, 0, 0), start, end)
            pygame.draw.line(WIN, (0, 0, 0), (x, y - 20), (x1, y1 - 20))

