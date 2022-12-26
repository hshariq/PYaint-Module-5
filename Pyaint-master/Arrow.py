import pygame
import math


class Arrow:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, WIN, start, end):
        # Draw the line
        pygame.draw.line(WIN, (0, 0, 0), start, end)

        # Calculate the slope of the line
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        slope = dy / dx
        print(dy, "dy")
        print(dx, "dx")
        print(slope, "slope")
        # Calculate the angle of the line in radians
        angle = math.atan(slope)

        if dx < 0 and slope < 0:
            angle += math.pi
        if dx < 0 and dy < 0:
            angle += math.pi

        x, y = end
        center = (x, y)
        points = [(x + 10, y), (x, y + 10), (x, y - 10)]
        rotated_points = [self.rotate_point(point, center, angle) for point in points]

        # Draw the rotated triangle
        pygame.draw.polygon(WIN, (0, 0, 0), rotated_points)

    def rotate_point(self, point, center, angle):
        """Rotate a point around a center by a given angle in radians"""
        x, y = point
        cx, cy = center
        s = math.sin(angle)
        c = math.cos(angle)

        # Translate point back to origin
        x -= cx
        y -= cy

        # Rotate point
        xnew = x * c - y * s
        ynew = x * s + y * c

        # Translate point back
        x = xnew + cx
        y = ynew + cy
        return x, y



