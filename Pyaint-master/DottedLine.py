import pygame


class DottedLine:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, WIN, start, end):
        dash_size = 10
        x, y = start
        x1, y1 = end
        # Calculate the distance between the starting and ending points
        x_diff = x1 - x
        y_diff = y1 - y
        distance = (x_diff ** 2 + y_diff ** 2) ** 0.5

        # Calculate the number of dashes needed to draw the line
        num_dashes = int(distance / dash_size)

        # Calculate the x and y increments needed to draw the dashes
        x_inc = x_diff / num_dashes
        y_inc = y_diff / num_dashes

        # Draw the dashes
        for i in range(num_dashes):
            dash_start_x = x + i * x_inc
            dash_start_y = y + i * y_inc
            dash_end_x = dash_start_x + x_inc / 2
            dash_end_y = dash_start_y + y_inc / 2
            pygame.draw.line(WIN, (0, 0, 0), (int(dash_start_x), int(dash_start_y)), (int(dash_end_x), int(dash_end_y)))
