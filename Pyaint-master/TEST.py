import numpy
import pygame

x=5
y=10
radius=3
list = []
for i in range(x, x + radius + 1):
    print("i", i)
    for j in range(y, y + radius + 1):
        print("j" , j)
        if i == x:
            poi = i, j
            list.append(poi)
        else:
            if j <= (y + radius) - (i-x):
                # print("HERE")
                poi = i, j
                list.append(poi)
            else:
                count = 0

for i in range(x, x + radius + 1):
    print("i", i)
    for j in range(y,  y - (radius+1), -1):
        print("j" , j)
        if i == x:
            poi = i, j
            if poi not in list:
                list.append(poi)
        else:
            if j >= (y - radius) + (i-x):
                # print("HERE")
                poi = i, j
                if poi not in list:
                    list.append(poi)
            else:
                count = 0

for i in range(x, x - (radius+1), -1):
    print("i", i)
    for j in range(y, y - (radius+1), -1):
        print("j" , j)
        if i == x:
            poi = i, j
            if poi not in list:
                list.append(poi)
        else:
            if j >= (y - radius) + (x-i):
                # print("HERE")
                poi = i, j
                list.append(poi)
            else:
                count = 0

for i in range(x, x - (radius+1), -1):
    print("i", i)
    for j in range(y, y + radius + 1):
        print("j" , j)
        if i == x:
            poi = i, j
            if poi not in list:
                list.append(poi)
        else:
            if j <= (y + radius) - (x-i):
                # print("HERE")
                poi = i, j
                if poi not in list:
                    list.append(poi)
            else:
                count = 0

print(list)

# for straight line
# # Initialize Pygame
# pygame.init()
#
# # Set the window size
# window_size = (800, 600)
#
# # Create the window
# screen = pygame.display.set_mode(window_size)
#
# # Set the background color
# bg_color = (255, 255, 255)
#
# # Initialize variables to store the starting and ending points
# start_point = None
# end_point = None
#
# # Run the game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         # Check if the user closed the window
#         if event.type == pygame.QUIT:
#             running = False
#
#         # Check if the user pressed the mouse button down
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # If this is the first mouse button press, set the starting point
#             if start_point is None:
#                 start_point = event.pos
#
#         # Check if the user released the mouse button
#         elif event.type == pygame.MOUSEBUTTONUP:
#             # If this is the first mouse button release, set the ending point
#             if end_point is None:
#                 end_point = event.pos
#
#     # Fill the background with the background color
#     screen.fill(bg_color)
#
#     # If both the starting and ending points have been set, draw a line between them
#     if start_point is not None and end_point is not None:
#         pygame.draw.line(screen, (0, 0, 0), start_point, end_point)
#
#     # Update the display
#     pygame.display.flip()
#
# # Quit Pygame
# pygame.quit()

# Initialize Pygame


# for arrow
# Set the window size
# window_size = (800, 600)
#
# # Create the window
# screen = pygame.display.set_mode(window_size)
#
# # Set the background color
#
# bg_color = (255, 255, 255)
#
# # Initialize variables to store the starting and ending points
# start_point = None
# end_point = None
#
# # Run the game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         # Check if the user closed the window
#         if event.type == pygame.QUIT:
#             running = False
#
#         # Check if the user pressed the mouse button down
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # If this is the first mouse button press, set the starting point
#             if start_point is None:
#                 start_point = event.pos
#
#         # Check if the user released the mouse button
#         elif event.type == pygame.MOUSEBUTTONUP:
#             # If this is the first mouse button release, set the ending point
#             if end_point is None:
#                 end_point = event.pos
#
#     # Fill the background with the background color
#     screen.fill(bg_color)
#
#     # If both the starting and ending points have been set, draw an arrow between them
#     if start_point is not None and end_point is not None:
#         # Draw the body of the arrow
#         pygame.draw.line(screen, (0, 0, 0), start_point, end_point)
#
#         # Draw the head of the arrow
#         x,y=end_point
#         # pygame.draw.polygon(screen, (0, 0, 0), [(x-10,y+10), (x,y), (x+10,y+10)])
#         pygame.draw.polygon(screen, (0, 0, 0), [(x+10, y), (x,y+ 10), (x,y- 10)])
#
#
#     # Update the display
#     pygame.display.flip()
#
# # Quit Pygame
# pygame.quit()


# for dotted line
# Set the window size
# import pygame
# import math
#
# # Initialize Pygame
# pygame.init()
#
# # Set the window size
# window_size = (800, 600)
#
# # Create the window
# screen = pygame.display.set_mode(window_size)
#
# # Set the background color
# bg_color = (255, 255, 255)
#
# # Initialize variables to store the starting and ending points
# start_point = None
# end_point = None
#
# # Set the size of the dashes
# dash_size = 20
#
# # Run the game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         # Check if the user closed the window
#         if event.type == pygame.QUIT:
#             running = False
#
#         # Check if the user pressed the mouse button down
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # If this is the first mouse button press, set the starting point
#             if start_point is None:
#                 start_point = event.pos
#
#         # Check if the user released the mouse button
#         elif event.type == pygame.MOUSEBUTTONUP:
#             # If this is the first mouse button release, set the ending point
#             if end_point is None:
#                 end_point = event.pos
#
#     # Fill the background with the background color
#     screen.fill(bg_color)
#
#     # If both the starting and ending points have been set, draw a dashed line between them
#     if start_point is not None and end_point is not None:
#         # Calculate the distance between the starting and ending points
#         x_diff = end_point[0] - start_point[0]
#         y_diff = end_point[1] - start_point[1]
#         distance = math.sqrt(x_diff**2 + y_diff**2)
#
#         # Calculate the number of dashes needed to draw the line
#         num_dashes = int(distance / dash_size)
#
#         # Calculate the x and y increments needed to draw the dashes
#         x_inc = x_diff / num_dashes
#         y_inc = y_diff / num_dashes
#
#         # Draw the dashes
#         for i in range(num_dashes):
#             dash_start_x = start_point[0] + i * x_inc
#             dash_start_y = start_point[1] + i * y_inc
#             dash_end_x = dash_start_x + x_inc / 2
#             dash_end_y = dash_start_y + y_inc / 2
#             pygame.draw.line(screen, (0, 0, 0), (int(dash_start_x), int(dash_start_y)), (int(dash_end_x), int(dash_end_y)))
#
#     # Update the display
#     pygame.display.flip()
#
# # Quit Pygame
# pygame.quit()



# # multiple lines
# # Initialize Pygame
# pygame.init()
#
# # Set the window size
# window_size = (800, 600)
#
# # Create the window
# screen = pygame.display.set_mode(window_size)
#
# # Set the background color
# bg_color = (255, 255, 255)
#
# # Initialize variables to store the starting and ending points
# start_point = None
# end_point = None
#
# # Run the game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         # Check if the user closed the window
#         if event.type == pygame.QUIT:
#             running = False
#
#         # Check if the user pressed the mouse button down
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # If this is the first mouse button press, set the starting point
#             if start_point is None:
#                 start_point = event.pos
#
#         # Check if the user released the mouse button
#         elif event.type == pygame.MOUSEBUTTONUP:
#             # If this is the first mouse button release, set the ending point
#             if end_point is None:
#                 end_point = event.pos
#
#     # Fill the background with the background color
#     screen.fill(bg_color)
#
#     # If both the starting and ending points have been set, draw a line between them
#     if start_point is not None and end_point is not None:
#         x, y = start_point
#         x1, y1 = end_point
#         pygame.draw.line(screen, (0, 0, 0), (x, y + 20), (x1, y1 + 20))
#         pygame.draw.line(screen, (0, 0, 0), start_point, end_point)
#         pygame.draw.line(screen, (0, 0, 0), (x, y - 20), (x1, y1 - 20))
#
#     # Update the display
#     pygame.display.flip()
#
# # Quit Pygame
# pygame.quit()
# # end of multiple lines



# def draw_lines():
#     # Iterate through the points list
#     print("drawing lines")
#     dc = (0, 0, 0)
#     # for i in range(1, len(points)):
#     # Get the starting and ending points of the line
#     start_pos = points[0]
#     x, y = get_row_col_from_pos(start_pos)
#     print("hello")
#     print(start_pos)
#     end_pos = points[1]
#     x2, y2 = get_row_col_from_pos(end_pos)
#     changeX = x2 - x
#     changeY = y2 - y
#     gradient = changeY / changeX
#     print(gradient)
#     c = y - gradient * x
#     for i in range(x, x2 + 1):
#         if i == x:
#             grid[i][int(y)] = dc
#         else:
#             y = gradient * i + c
#             grid[i][int(y)] = dc
#
#     # Draw the line
#     # pygame.draw.line(WIN, (0, 0, 0), start_pos, end_pos, 5)
#     # pygame.display.update()
#
#
# def SL():
#     print("STRAIGHT NAHI")
#     start_pos = points[0]
#     x, y = get_row_col_from_pos(start_pos)
#     print("hello")
#     print(start_pos)
#     end_pos = points[1]
#     x1,y1=end_pos
#     pygame.draw.line(WIN, (0, 0, 0), (x,y), (x1, y1))
#     # pygame.draw.line(WIN, (0, 0, 0), (50, 100), (150, 200))
#     # Update the display
#     pygame.display.flip()
