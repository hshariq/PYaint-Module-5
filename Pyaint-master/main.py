from pygame import gfxdraw

from utils import *
import pygame

WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH, HEIGHT))  # setting up window
pygame.display.set_caption("Pyaint")
STATE = "COLOR"
Change = False
# Crea te a list to store the mouse positions
points = []


def init_grid(rows, columns, color):  # initialises grid
    grid = []  # grid setup, initlaised as empty grid

    for i in range(rows):
        grid.append([])  # adding rows
        for _ in range(columns):  # use _ when variable is not required
            grid[i].append(color)  # adding col
    return grid


def draw_grid(win, grid):  # draw in grid
    for i, row in enumerate(grid):  # enumerate gives value with index
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, SILVER, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS + 1):
            pygame.draw.line(win, SILVER, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw_mouse_position_text(win):
    pos = pygame.mouse.get_pos()
    pos_font = get_font(MOUSE_POSITION_TEXT_SIZE)
    try:
        row, col = get_row_col_from_pos(pos)
        text_surface = pos_font.render(str(row) + ", " + str(col), 1, BLACK)
        win.blit(text_surface, (5, HEIGHT - TOOLBAR_HEIGHT))
    except IndexError:
        for button in buttons:
            if not button.hover(pos):
                continue
            if button.text == "Clear":
                text_surface = pos_font.render("Clear Everything", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.text == "Erase":
                text_surface = pos_font.render("Erase", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "FillBucket":
                text_surface = pos_font.render("Fill Bucket", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Brush":
                text_surface = pos_font.render("Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.name == "Change":
                text_surface = pos_font.render("Swap Toolbar", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            r, g, b = button.color
            text_surface = pos_font.render("( " + str(r) + ", " + str(g) + ", " + str(b) + " )", 1, BLACK)

            win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))

        for button in brush_widths:
            if not button.hover(pos):
                continue
            if button.width == size_small:
                text_surface = pos_font.render("Small-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_medium:
                text_surface = pos_font.render("Medium-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break
            if button.width == size_large:
                text_surface = pos_font.render("Large-Sized Brush", 1, BLACK)
                win.blit(text_surface, (10, HEIGHT - TOOLBAR_HEIGHT))
                break


def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    draw_brush_widths(win)
    draw_mouse_position_text(win)
    pygame.display.update()


def draw_brush_widths(win):
    brush_widths = [
        Button(rtb_x - size_small / 2, 480, size_small, size_small, drawing_color, None, None, "ellipse"),
        Button(rtb_x - size_medium / 2, 510, size_medium, size_medium, drawing_color, None, None, "ellipse"),
        Button(rtb_x - size_large / 2, 550, size_large, size_large, drawing_color, None, None, "ellipse")
    ]
    for button in brush_widths:
        button.draw(win)
        # Set border colour
        border_color = BLACK
        if button.color == BLACK:
            border_color = GRAY
        else:
            border_color = BLACK
        # Set border width
        border_width = 2
        if ((BRUSH_SIZE == 1 and button.width == size_small) or (BRUSH_SIZE == 2 and button.width == size_medium) or (
                BRUSH_SIZE == 3 and button.width == size_large)):
            border_width = 4
        else:
            border_width = 2
        # Draw border
        pygame.draw.ellipse(win, border_color, (button.x, button.y, button.width, button.height),
                            border_width)  # border


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    if col >= ROWS:
        raise IndexError
    return row, col


def anothercheck_get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    return row, col


def handle_mouse_events(event):
    # If the left mouse button was clicked
    r, c = anothercheck_get_row_col_from_pos(event.pos)
    print(inBounds(r, c))
    print(r, c)
    if event.button == 1 & inBounds(r, c):
        # Append the mouse position to the points list
        points.append(event.pos)


def draw_lines():
    # Iterate through the points list
    global start_pos, end_pos
    print("drawing lines")
    dc = (0, 0, 0)
    for i in range(1, len(points)):
        # Get the starting and ending points of the line
        start_pos = points[i - 1]
        print("hello")
        print(start_pos)
        end_pos = points[i]
        print("end")
        print(end_pos)

    while start_point is None and end_point is None:
        pri

    x, y = get_row_col_from_pos(start_pos)
    x2, y2 = get_row_col_from_pos(end_pos)
    changeX = x2 - x
    changeY = y2 - y
    gradient = changeY / changeX
    c = y - gradient * x
    for i in range(x, x2 + 1):
        if i == x:
            grid[i][int(y)] = dc
        else:
            y = gradient * i + c
            grid[i][int(y)] = dc

    # Draw the line
    # pygame.draw.line(WIN, (0, 0, 0), start_pos, end_pos, 5)
    # pygame.display.update()


def SL():
    start = points[0]
    print("START")
    print(start)
    end = points[1]
    print("END")
    print(end)
    pygame.draw.line(WIN, (0, 0, 0), start, end)
    pygame.display.flip()


def getCircleCoordinates(X, Y, radius):
    list = []
    for i in range(X - 5, X + 6):
        for j in range(Y - 5, Y + 6):
            if not (((X - i) * (X - i)) + ((Y - j) * (Y - j))) < (radius * radius):
                point = i, j
                list.append(point)
                # grid[i][j] = drawing_color
            if i == X - 5 and j not in range(X - 3, X + 2):
                point = i, j
                list.append(point)
                # grid[i][j] = WHITE
            if i == X - 4 and (j == Y - 5 or j == Y + 5 or j == Y - 4 or j == Y + 4):
                point = i, j
                list.append(point)
                # grid[i][j] = WHITE
            if i == X + 5 and j not in range(X - 3, X + 2):
                point = i, j
                list.append(point)
            # grid[i][j] = WHITE
            if i == X + 4 and (j == Y - 5 or j == Y + 5 or j == Y - 4 or j == Y + 4):
                point = i, j
                list.append(point)
                # grid[i][j] = WHITE
            if (i == X - 3 or i == X + 3) and j == Y - 5:
                point = i, j
                list.append(point)
                # grid[i][j] = WHITE
            if (i == X - 3 or i == X + 3) and j == Y + 5:
                point = i, j
                list.append(point)

        return list


def arrow():
    # start = points[0]
    # print("START")
    # print(start)
    # end = points[1]
    # print("END")
    # print(end)
    # pygame.draw.line(WIN, (0, 0, 0), start, end)
    # # Draw the head of the arrow
    # x, y = end
    # # pygame.draw.polygon(screen, (0, 0, 0), [(x-10,y+10), (x,y), (x+10,y+10)])
    # pygame.draw.polygon(WIN, (0, 0, 0), [(x + 10, y), (x, y + 10), (x, y - 10)])
    # pygame.display.flip()
    isPressed = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                #(x, y) = pygame.mouse.get_pos()  # returns the position of mouse cursor
                # pygame.draw.circle(WIN, BLUE, (x, y), 15)
                x,y=get_row_col_from_pos(pygame.mouse.get_pos())
                print(inBounds(x,y))
                grid[x][y]=drawing_color
                isPressed = False
            elif event.type == pygame.MOUSEMOTION and isPressed == True:
                # (x, y) = pygame.mouse.get_pos()  # returns the position of mouse cursor
                x,y=get_row_col_from_pos(pygame.mouse.get_pos())

                grid[x][y]=BLUE
                # pygame.draw.circle(WIN, BLUE, (x,y), 15)
                # coord = getCircleCoordinates(x, y, 15)
                # rect=(x, y, 15, 10)
                # pygame.draw.rect(WIN, BLUE, rect)
                # gfxdraw.aacircle(WIN, x, y, 10, BLUE)
                # gfxdraw.filled_circle(WIN, x, y, 10, BLUE)
                # pygame.gfxdraw.line(WIN, start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, thickness, True)

        pygame.display.flip()

 # start = points[0]
 #    # print("START")
 #    # print(start)
 #    # end = points[1]
 #    # print("END")
 #    # print(end)
 #    # pygame.draw.line(WIN, (0, 0, 0), start, end)
 #    # # Draw the head of the arrow
 #    # x, y = end
 #    # pygame.draw.polygon(WIN, (0, 0, 0), [(x + 10, y), (x, y + 10), (x, y - 10)])
 #    # pygame.display.flip()
 #    # points.clear()
 #    isPressed = False
 #    while True:
 #        for event in pygame.event.get():
 #            if event.type == pygame.MOUSEBUTTONDOWN:
 #                isPressed = True
 #            elif event.type == pygame.MOUSEBUTTONUP:
 #                # (x, y) = pygame.mouse.get_pos()  # returns the position of mouse cursor
 #                # pygame.draw.circle(WIN, BLUE, (x, y), 15)
 #                x, y = get_row_col_from_pos(pygame.mouse.get_pos())
 #                isPressed = False
 #            elif event.type == pygame.MOUSEMOTION and isPressed == True:
 #                # (x, y) = pygame.mouse.get_pos()  # returns the position of mouse cursor
 #                x, y = get_row_col_from_pos(pygame.mouse.get_pos())
 #                pygame.draw.circle(WIN, BLUE, (x, y), 15)
 #                # rect=(x, y, 15, 10)
 #                # pygame.draw.rect(WIN, BLUE, rect)
 #                pygame.display.flip()
 #    #             # gfxdraw.aacircle(WIN, x, y, 10, BLUE)
 #    #             # gfxdraw.filled_circle(WIN, x, y, 10, BLUE)
 #    #             # pygame.gfxdraw.line(WIN, start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, thickness, True)
 #    #
 #    #     pygame.display.flip()

def paint_using_brush(row, col, size):
    if BRUSH_SIZE == 1:
        grid[row][col] = drawing_color
    else:  # for values greater than 1
        r = row - BRUSH_SIZE + 1
        c = col - BRUSH_SIZE + 1

        for i in range(BRUSH_SIZE * 2 - 1):
            for j in range(BRUSH_SIZE * 2 - 1):
                if r + i < 0 or c + j < 0 or r + i >= ROWS or c + j >= COLS:
                    continue
                grid[r + i][c + j] = drawing_color

            # Checks whether the coordinated are within the canvas


def inBounds(row, col):
    if row < 0 or col < 0:
        return 0
    if row >= ROWS or col >= COLS:
        return 0
    return 1


def fill_bucket(row, col, color):
    # Visiting array
    vis = [[0 for i in range(101)] for j in range(101)]

    # Creating queue for bfs
    obj = []

    # Pushing pair of {x, y}
    obj.append([row, col])

    # Marking {x, y} as visited
    vis[row][col] = 1

    # Until queue is empty
    while len(obj) > 0:

        # Extracting front pair
        coord = obj[0]
        x = coord[0]
        y = coord[1]
        preColor = grid[x][y]

        grid[x][y] = color

        # Popping front pair of queue
        obj.pop(0)

        # For Upside Pixel or Cell
        if inBounds(x + 1, y) == 1 and vis[x + 1][y] == 0 and grid[x + 1][y] == preColor:
            obj.append([x + 1, y])
            vis[x + 1][y] = 1

        # For Downside Pixel or Cell
        if inBounds(x - 1, y) == 1 and vis[x - 1][y] == 0 and grid[x - 1][y] == preColor:
            obj.append([x - 1, y])
            vis[x - 1][y] = 1

        # For Right side Pixel or Cell
        if inBounds(x, y + 1) == 1 and vis[x][y + 1] == 0 and grid[x][y + 1] == preColor:
            obj.append([x, y + 1])
            vis[x][y + 1] = 1

        # For Left side Pixel or Cell
        if inBounds(x, y - 1) == 1 and vis[x][y - 1] == 0 and grid[x][y - 1] == preColor:
            obj.append([x, y - 1])
            vis[x][y - 1] = 1


# a simple run loop
run = True  # runnig

clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)  # creates the grid
drawing_color = BLACK

button_width = 40
button_height = 40
button_y_top_row = HEIGHT - TOOLBAR_HEIGHT / 2 - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT / 2 + 1
button_space = 42

size_small = 25
size_medium = 35
size_large = 50

rtb_x = WIDTH + RIGHT_TOOLBAR_WIDTH / 2
brush_widths = [
    Button(rtb_x - size_small / 2, 480, size_small, size_small, drawing_color, None, "ellipse"),
    Button(rtb_x - size_medium / 2, 510, size_medium, size_medium, drawing_color, None, "ellipse"),
    Button(rtb_x - size_large / 2, 550, size_large, size_large, drawing_color, None, "ellipse")
]

button_y_top_row = HEIGHT - TOOLBAR_HEIGHT / 2 - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT / 2 + 1
button_space = 42

# Adding Buttons
buttons = []

for i in range(int(len(COLORS) / 2)):
    buttons.append(Button(100 + button_space * i, button_y_top_row, button_width, button_height, COLORS[i]))

for i in range(int(len(COLORS) / 2)):
    buttons.append(
        Button(100 + button_space * i, button_y_bot_row, button_width, button_height, COLORS[i + int(len(COLORS) / 2)]))

# Right toolbar buttonst
# need to add change toolbar button.
for i in range(10):
    if i == 0:
        buttons.append(Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                              "1/2", name="Change"))  # Change toolbar buttons
    else:
        if i == 1:
            buttons.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="Straight Line", image_url="assets/Straightline.png"))  # append tools
        elif i == 2:
            buttons.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="Dotted Line", image_url="assets/Dotted-line.png"))  # append tools
        elif i == 3:
            buttons.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       "B" + str(i - 1), name="Arrow", image_url="assets/Arrow.png"))  # append tools
        elif i == 4:
            buttons.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       "B" + str(i - 1), name="Multi Line", image_url="assets/Multi-Line.png"))  # append tools
        else:
            buttons.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       "B" + str(i - 1), BLACK))  # append tools

buttons.append(
    Button(WIDTH - button_space, button_y_top_row, button_width, button_height, WHITE, "Erase", BLACK))  # Erase Button
buttons.append(
    Button(WIDTH - button_space, button_y_bot_row, button_width, button_height, WHITE, "Clear", BLACK))  # Clear Button
buttons.append(
    Button(WIDTH - 3 * button_space + 5, button_y_top_row, button_width - 5, button_height - 5, name="FillBucket",
           image_url="assets/paint-bucket.png"))  # FillBucket
buttons.append(
    Button(WIDTH - 3 * button_space + 45, button_y_top_row, button_width - 5, button_height - 5, name="Brush",
           image_url="assets/paint-brush.png"))  # Brush

draw_button = Button(5, HEIGHT - TOOLBAR_HEIGHT / 2 - 30, 60, 60, drawing_color)
buttons.append(draw_button)

start_point = None
end_point = None
draw(WIN, grid, buttons)

while run:
    clock.tick(FPS)  # limiting FPS to 60 or any other value

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user closed the program
            run = False
            #
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     # If this is the first mouse button press, set the starting point
            #     if start_point is None:
            #         start_point = event.pos
            #
            #     # Check if the user released the mouse button
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     # If this is the first mouse button release, set the ending point
            #     if end_point is None:
            #         end_point = event.pos
            #
            #     # If both the starting and ending points have been set, draw a line between them
            # if start_point is not None and end_point is not None:
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_events(event)

            elif event.type == pygame.MOUSEBUTTONUP:
                handle_mouse_events(event)

            # print("THESE ARE POINTS: ")
            # print(points)
            try:
                row, col = get_row_col_from_pos(pos)

                if STATE == "COLOR":
                    paint_using_brush(row, col, BRUSH_SIZE)

                elif STATE == "FILL":
                    fill_bucket(row, col, drawing_color)

                elif STATE == "SL":
                    print("STRAIGHT NAHI")
                    SL()
                    # clicked = True
                    # start=None
                    # if event.type == pygame.MOUSEBUTTONDOWN:
                    #     start = event.pos
                    #     print(start)
                    #     clicked = True
                    # while clicked:
                    #     for event in pygame.event.get():
                    #         if event.type == pygame.MOUSEBUTTONDOWN:
                    #             if start_point is None:
                    #                 start_point = event.pos
                    #             print("START")
                    #             print(start)
                    #         elif event.type == pygame.MOUSEBUTTONUP:
                    #             end = event.pos
                    #             print("ENDlo: ")
                    #             print(start)
                    #             pygame.draw.line(WIN, (0, 0, 0), start, end)
                    #             clicked = False
                    #         # elif event.type == pygame.MOUSEMOTION and clicked == True:
                    #         #     (x, y) = pygame.mouse.get_pos()
                    #     pygame.display.flip()

                    # rST, cST = get_row_col_from_pos(points[0])
                    # rEND, cEND = get_row_col_from_pos(points[1])
                    # pygame.draw.line(WIN, (0, 0, 0), (50, 100), (150, 200))
                    # draw_lines()
                    # Update the display

                elif STATE == "ARR":
                    print("ARROW MEIN")
                    arrow()

            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        draw_button.color = drawing_color
                        STATE = "COLOR"
                        break

                    if button.name == "FillBucket":
                        STATE = "FILL"
                        break

                    if button.name == "Straight Line":
                        STATE = "SL"
                        print("STRIAGHT BUTTON BEING CLICKED")
                        break

                    if button.name == "Arrow":
                        STATE = "ARR"
                        print("STRIAGHT BUTTON BEING CLICKED")
                        break

                    if button.name == "Change":
                        Change = not Change
                        for i in range(10):
                            if i == 0:
                                buttons.append(
                                    Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                                           button_height, WHITE, "2/2", name="Change"))
                            else:
                                if Change == False:
                                    buttons.append(
                                        Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                                               button_height, WHITE, "B" + str(i - 1), BLACK))
                                if Change == True:
                                    buttons.append(
                                        Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                                               button_height, WHITE, "C" + str(i - 1), BLACK))
                        break

                    if button.name == "Brush":
                        STATE = "COLOR"
                        break

                    drawing_color = button.color
                    draw_button.color = drawing_color

                    break

                for button in brush_widths:
                    if not button.clicked(pos):
                        continue
                    # set brush width
                    if button.width == size_small:
                        BRUSH_SIZE = 1
                    elif button.width == size_medium:
                        BRUSH_SIZE = 2
                    elif button.width == size_large:
                        BRUSH_SIZE = 3

                    STATE = "COLOR"

pygame.quit()
