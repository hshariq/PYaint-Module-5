import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("My Pygame Paint Program")

# Create a list to store the mouse positions
points = []

# Set the default color to black
color = (0, 0, 0)


def handle_mouse_events(event):
    # If the left mouse button was clicked
    if event.button == 1:
        # Append the mouse position to the points list
        points.append(event.pos)
    # If the right mouse button was clicked
    elif event.button == 3:
        # Update the color to the color at the mouse position
        color = screen.get_at(event.pos)



def draw_grid():
    # Set the grid color to light grey
    grid_color = (200, 200, 200)

    # Set the grid line width
    line_width = 1

    # Set the grid size (in pixels)
    grid_size = 20

    # Calculate the number of vertical and horizontal lines
    num_vertical_lines = window_size[0] // grid_size
    num_horizontal_lines = window_size[1] // grid_size

    # Draw the vertical lines
    for x in range(num_vertical_lines):
        start_pos = (x * grid_size, 0)
        end_pos = (x * grid_size, window_size[1])
        pygame.draw.line(screen, grid_color, start_pos, end_pos, line_width)

    # Draw the horizontal lines
    for y in range(num_horizontal_lines):
        start_pos = (0, y * grid_size)
        end_pos = (window_size[0], y * grid_size)
        pygame.draw.line(screen, grid_color, start_pos, end_pos, line_width)


def draw_lines():
    # Iterate through the points list
    for i in range(1, len(points)):
        # Get the starting and ending points of the line
        start_pos = points[i-1]
        end_pos = points[i]

        # Draw the line
        pygame.draw.line(screen, color, start_pos, end_pos, 5)

