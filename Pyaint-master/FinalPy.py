from pygame import gfxdraw

from SaveBrush import SaveBrush
from ShapeCirclePencil import ShapeCirclePencil
from Arrow import Arrow
from DottedLine import DottedLine
from MultiLine import MultiLine
from ShapeRhombusPencil import ShapeRhombusPencil
from ShapedRectPencil import ShapedRectPencil
from StraightLine import StraightLine
from utils import *
import pygame

WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH, HEIGHT))
pygame.display.set_caption("Pyaint")
STATE = "COLOR"
Change = False
points = []
SLlist = []
ArrowList = []
MultiList = []
DotList = []
points2 = []
ShapedRectList = []
ShapeCircletList = []
ShapedRhombusList = []
Translated_pointsL = []
# paint using bursh mai changes t fast, draw grid mai to make it fast
done1 = True
count = -1
prev = None
start1 = None
polygon_points = []
polygon_shapeL = []
input_box = None
colorTxtBox = None
BRUSH_SIZE = 1
inboundcheck = True
pencilClicked = False
dontcalpoints = False
shape=False


def init_grid(rows, columns, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(columns):  # use _ when variable is not required
            grid[i].append(color)
    return grid


def draw_grid(win, grid):
    # for i, row in enumerate(grid):
    #     for j, pixel in enumerate(row):
    #         pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    # if DRAW_GRID_LINES:
    #     for i in range(ROWS + 1):
    #         pygame.draw.line(win, SILVER, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
    #     for i in range(COLS + 1):
    #         pygame.draw.line(win, SILVER, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, SILVER, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))
        for i in range(COLS + 1):
            pygame.draw.line(win, SILVER, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

    pos = pygame.mouse.get_pos()
    pos_font = get_font(MOUSE_POSITION_TEXT_SIZE)

    button_text = {
        "Clear": "Clear Everything",
        "Erase": "Erase",
        "FillBucket": "Fill Bucket",
        "Brush": "Brush",
        "Change": "Swap Toolbar"
    }
    for button in buttons:
        if button.hover(pos):
            if button.text in button_text:
                text_surface = pos_font.render(
                    button_text[button.text], 1, BLACK)
            else:
                r, g, b = button.color
                text = f"( {r}, {g}, {b} )"
                text_surface = pos_font.render(text, 1, BLACK)
            win.blit(text_surface, (5, HEIGHT - TOOLBAR_HEIGHT))
            break

    for button in brush_widths:
        if button.hover(pos):
            if button.width == size_small:
                text = "Small-Sized Brush"
            elif button.width == size_medium:
                text = "Medium-Sized Brush"
            else:
                text = "Large-Sized Brush"
            text_surface = pos_font.render(text, 1, BLACK)
            win.blit(text_surface, (5, HEIGHT - TOOLBAR_HEIGHT))
            break


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
            text_surface = pos_font.render(
                "( " + str(r) + ", " + str(g) + ", " + str(b) + " )", 1, BLACK)

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


def draw2(win, grid, buttons):
    # win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    draw_brush_widths(win)
    # draw_mouse_position_text(win)
    if len(SLlist) != 0:
        for i in SLlist:
            # print("i", i)
            pygame.draw.line(win, (0, 0, 0), i.start, i.end)
            pygame.display.update()

    if len(ArrowList) != 0:
        for i in ArrowList:
            i.draw(win, i.start, i.end)
            pygame.display.update()

    if len(MultiList) != 0:
        for i in MultiList:
            i.draw(win, i.start, i.end)
            pygame.display.update()

    if len(DotList) != 0:
        for i in DotList:
            i.draw(win, i.start, i.end)
            pygame.display.update()

    if len(ShapedRectList) != 0:
        for i in ShapedRectList:
            i.draw(win, i.corners, i.bound, drawing_color)
            pygame.display.update()

    if len(ShapeCircletList) != 0:
        for i in ShapeCircletList:
            i.draw(win, i.x, i.y, drawing_color)
            pygame.display.update()

    if len(ShapedRhombusList) != 0:
        for i in ShapedRhombusList:
            i.draw(win, i.x, i.y, i.bound, drawing_color)
            pygame.display.update()

    if len(Translated_pointsL) != 0:
        for i in Translated_pointsL:
            sb.draw(win, drawing_color,i)
            pygame.display.update()

    pygame.display.update()


def draw3(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    draw_brush_widths(win)
    # draw_mouse_position_text(win)
    if len(SLlist) != 0:
        for i in SLlist:
            # print("i", i)
            pygame.draw.line(win, (0, 0, 0), i.start, i.end)
            pygame.display.update()

    if len(ArrowList) != 0:
        for i in ArrowList:
            i.draw(win, i.start, i.end)
            pygame.display.update()

    if len(MultiList) != 0:
        for i in MultiList:
            i.draw(win, i.start, i.end)
            pygame.display.update()

    if len(DotList) != 0:
        for i in DotList:
            i.draw(win, i.start, i.end)
            pygame.display.update()

    pygame.display.update()


def draw_brush_widths(win):
    brush_widths = [
        Button(rtb_x - size_small / 2, 480, size_small,
               size_small, drawing_color, None, None, "ellipse"),
        Button(rtb_x - size_medium / 2, 510, size_medium,
               size_medium, drawing_color, None, None, "ellipse"),
        Button(rtb_x - size_large / 2, 550, size_large,
               size_large, drawing_color, None, None, "ellipse")
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
    if not dontcalpoints:
        r, c = anothercheck_get_row_col_from_pos(event.pos)
        print(inBounds(r, c))
        print(r, c)
        if event.button == 1 & inBounds(r, c):
            # Append the mouse position to the points list
            points.append(event.pos)


def RhomInGrid(x, y, radius):
    list = []
    for i in range(x, x + radius + 1):
        for j in range(y, y + radius + 1):
            if i == x:
                poi = i, j
                list.append(poi)
            else:
                if j <= (y + radius) - (i - x):
                    poi = i, j
                    list.append(poi)

    for i in range(x, x + radius + 1):
        for j in range(y, y - (radius + 1), -1):
            if i == x:
                poi = i, j
                if poi not in list:
                    list.append(poi)
            else:
                if j >= (y - radius) + (i - x):
                    poi = i, j
                    if poi not in list:
                        list.append(poi)

    for i in range(x, x - (radius + 1), -1):
        for j in range(y, y - (radius + 1), -1):
            if i == x:
                poi = i, j
                if poi not in list:
                    list.append(poi)
            else:
                if j >= (y - radius) + (x - i):
                    poi = i, j
                    list.append(poi)

    for i in range(x, x - (radius + 1), -1):
        for j in range(y, y + radius + 1):
            if i == x:
                poi = i, j
                if poi not in list:
                    list.append(poi)
            else:
                if j <= (y + radius) - (x - i):
                    poi = i, j
                    if poi not in list:
                        list.append(poi)

    return list


def CircleinGrid(x, y, size):
    list = []
    c = 0
    this = 0
    print(x, y)
    for j in range(y - size, y + size + 1):
        for i in range(x - size, x + size + 1):
            # if count == size:
            if j != y:
                if j == (y - (size - c)):
                    s = int((size / 2) + c)
                    if (x - s) <= i <= (x + s):
                        poi = i, j
                        list.append(poi)
                    this = 1
                if j == (y + (size - c)):
                    s = int((size / 2) + c)
                    if (x - s) <= i <= (x + s):
                        poi = i, j
                        list.append(poi)
                    this = 0
            else:
                c = size - 2
                poi = i, j
                list.append(poi)
        if this == 1:
            c = c + 1
        else:
            c = c - 1

    return list


def RectangleInGrid(x, y, size):
    list = []
    for i in range(x, x + size):
        for j in range(y, y + size + 1):
            poi = i, j
            list.append(poi)

    for i in range(x, x + size):
        for j in range(y, y - (size + 1), -1):
            poi = i, j
            if poi not in list:
                list.append(poi)

    for i in range(x, x - size, -1):
        for j in range(y, y - (size + 1), -1):
            poi = i, j
            if poi not in list:
                list.append(poi)

    for i in range(x, x - size, -1):
        for j in range(y, y + size + 1):
            poi = i, j
            if poi not in list:
                list.append(poi)

    return list


def SL():
    start = points[0]
    print("START")
    print(start)
    end = points[1]
    SL1 = StraightLine(start, end)
    SLlist.append(StraightLine(start, end))
    print("END")
    print(end)
    pygame.draw.line(WIN, (0, 0, 0), SL1.start, SL1.end)
    pygame.display.flip()
    points.clear()


def arrow():
    start = points[0]
    print("START")
    print(start)
    end = points[1]
    print("END")
    print(end)
    A1 = Arrow(start, end)
    ArrowList.append(Arrow(start, end))
    A1.draw(WIN, start, end)
    # pygame.draw.line(WIN, (0, 0, 0), start, end)
    # Draw the head of the arrow
    # x, y = end
    # pygame.draw.polygon(WIN, (0, 0, 0), [(x + 10, y), (x, y + 10), (x, y - 10)])
    pygame.display.flip()
    points.clear()


def shapedBrush1(BS):
    print(BS)
    if pencilClicked:
        isPressed = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    isPressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    x1, y1 = x + 30, y
                    x3, y3 = x + 15, y + 20
                    x2, y2 = x + 15, y - 20
                    bound = False
                    corners = [(x, y), (x1, y1), (x3, y3), (x2, y2)]
                    for i in corners:
                        boundx, boundy = get_row_col_from_pos(i)
                        if inBounds(boundx, boundy):
                            bound = True
                        else:
                            bound = False
                    S3 = ShapeRhombusPencil(x, y, bound)
                    ShapedRhombusList.append(ShapeRhombusPencil(x, y, bound))
                    S3.draw(WIN, x, y, bound, drawing_color)
                    if DRAW_GRID_LINES:
                        for i in range(ROWS + 1):
                            pygame.draw.line(WIN, SILVER, (0, i * PIXEL_SIZE),
                                             (WIDTH, i * PIXEL_SIZE))
                        for i in range(COLS + 1):
                            pygame.draw.line(WIN, SILVER, (i * PIXEL_SIZE, 0),
                                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
                    pygame.display.flip()
                    isPressed = False
                elif event.type == pygame.MOUSEMOTION and isPressed == True:
                    x, y = pygame.mouse.get_pos()
                    x1, y1 = x + 30, y
                    x3, y3 = x + 15, y + 20
                    x2, y2 = x + 15, y - 20
                    bound = False
                    corners = [(x, y), (x1, y1), (x3, y3), (x2, y2)]
                    for i in corners:
                        boundx, boundy = get_row_col_from_pos(i)
                        if inBounds(boundx, boundy):
                            bound = True
                        else:
                            bound = False
                    S3 = ShapeRhombusPencil(x, y, bound)
                    ShapedRhombusList.append(ShapeRhombusPencil(x, y, bound))
                    S3.draw(WIN, x, y, bound, drawing_color)
                    if DRAW_GRID_LINES:
                        for i in range(ROWS + 1):
                            pygame.draw.line(WIN, SILVER, (0, i * PIXEL_SIZE),
                                             (WIDTH, i * PIXEL_SIZE))
                        for i in range(COLS + 1):
                            pygame.draw.line(WIN, SILVER, (i * PIXEL_SIZE, 0),
                                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
                    pygame.display.flip()
    else:
        isPressed = False
        size = 0
        if BS == 1:
            size = 2
        elif BS == 2:
            size = 3
        elif BS == 3:
            size = 5

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    isPressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = get_row_col_from_pos(pygame.mouse.get_pos())
                    list = RhomInGrid(x, y, size)
                    for i in list:
                        x, y = i
                        grid[x][y] = drawing_color

                    draw2(WIN, grid, buttons)

                    isPressed = False
                elif event.type == pygame.MOUSEMOTION and isPressed == True:
                    x, y = get_row_col_from_pos(pygame.mouse.get_pos())
                    list = RhomInGrid(x, y, size)
                    for i in list:
                        x, y = i
                        grid[x][y] = drawing_color

                    draw2(WIN, grid, buttons)
            points.clear()


def shapedBrush2(BS):
    # bw = [
    #     Button(rtb_x - size_small / 2, 480, size_small,
    #            size_small, drawing_color, None, "rect"),
    #     Button(rtb_x - size_medium / 2, 510, size_medium,
    #            size_medium, drawing_color, None, "ellipse"),
    #     Button(rtb_x - size_large / 2, 550, size_large,
    #            size_large, drawing_color, None, "ellipse")
    # ]
    # for button in bw:
    #     if not button.clicked(pos):
    #         continue
    #     # set brush width
    #     if button.width == size_small:
    #         print("HERE")
    #         BS = 1
    #     elif button.width == size_medium:
    #         print("HERE 2")
    #         BS = 2
    #     elif button.width == size_large:
    #         BS = 3

    if pencilClicked:
        isPressed = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    isPressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    x1, y1 = x + 40, y
                    x3, y3 = x + 40, y + 20
                    x2, y2 = x, y + 20
                    corners = [(x, y), (x1, y1), (x3, y3), (x2, y2)]
                    bound = False
                    for i in corners:
                        boundx, boundy = get_row_col_from_pos(i)
                        if inBounds(boundx, boundy):
                            bound = True
                        else:
                            bound = False

                    S1 = ShapedRectPencil(corners, bound)
                    ShapedRectList.append(ShapedRectPencil(corners, bound))
                    S1.draw(WIN, corners, bound,drawing_color)
                    if DRAW_GRID_LINES:
                        for i in range(ROWS + 1):
                            pygame.draw.line(WIN, SILVER, (0, i * PIXEL_SIZE),
                                             (WIDTH, i * PIXEL_SIZE))
                        for i in range(COLS + 1):
                            pygame.draw.line(WIN, SILVER, (i * PIXEL_SIZE, 0),
                                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
                    pygame.display.flip()
                    isPressed = False
                elif event.type == pygame.MOUSEMOTION and isPressed == True:
                    x, y = pygame.mouse.get_pos()
                    x1, y1 = x + 40, y
                    x3, y3 = x + 40, y + 20
                    x2, y2 = x, y + 20
                    corners = [(x, y), (x1, y1), (x3, y3), (x2, y2)]
                    bound = False
                    for i in corners:
                        boundx, boundy = get_row_col_from_pos(i)
                        if inBounds(boundx, boundy):
                            bound = True
                        else:
                            bound = False

                    S1 = ShapedRectPencil(corners, bound)
                    ShapedRectList.append(ShapedRectPencil(corners, bound))
                    S1.draw(WIN, corners, bound,drawing_color)
                    if DRAW_GRID_LINES:
                        for i in range(ROWS + 1):
                            pygame.draw.line(WIN, SILVER, (0, i * PIXEL_SIZE),
                                             (WIDTH, i * PIXEL_SIZE))
                        for i in range(COLS + 1):
                            pygame.draw.line(WIN, SILVER, (i * PIXEL_SIZE, 0),
                                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

    else:
        isPressed = False

        size = 0
        if BS == 1:
            size = 2
        elif BS == 2:
            size = 3
        elif BS == 3:
            size = 5

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    isPressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = get_row_col_from_pos(pygame.mouse.get_pos())
                    list = RectangleInGrid(x, y, size)
                    for i in list:
                        x, y = i
                        grid[x][y] = drawing_color

                    draw2(WIN, grid, buttons)
                    isPressed = False
                elif event.type == pygame.MOUSEMOTION and isPressed == True:
                    x, y = get_row_col_from_pos(pygame.mouse.get_pos())
                    list = RectangleInGrid(x, y, size)
                    for i in list:
                        x, y = i
                        grid[x][y] = drawing_color

                    draw2(WIN, grid, buttons)
            points.clear()

def shapedBrush3(BS):
    if pencilClicked:
        isPressed = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    isPressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    boundx, boundy = get_row_col_from_pos(pygame.mouse.get_pos())
                    if inBounds(boundx, boundy):
                        S2 = ShapeCirclePencil(x, y)
                        ShapeCircletList.append(ShapeCirclePencil(x, y))
                        S2.draw(WIN, x, y, drawing_color)
                        if inBounds(boundx, boundy):
                            S2 = ShapeCirclePencil(x, y)
                            ShapeCircletList.append(ShapeCirclePencil(x, y))
                            S2.draw(WIN, x, y,drawing_color)
                            if DRAW_GRID_LINES:
                                for i in range(ROWS + 1):
                                    pygame.draw.line(WIN, SILVER, (0, i * PIXEL_SIZE),
                                                     (WIDTH, i * PIXEL_SIZE))
                                for i in range(COLS + 1):
                                    pygame.draw.line(WIN, SILVER, (i * PIXEL_SIZE, 0),
                                                     (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
                        pygame.display.flip()
                    isPressed = False
                elif event.type == pygame.MOUSEMOTION and isPressed == True:
                    x, y = pygame.mouse.get_pos()
                    boundx, boundy = get_row_col_from_pos(pygame.mouse.get_pos())
                    print(x, y)
                    if inBounds(boundx, boundy):
                        S2 = ShapeCirclePencil(x, y)
                        ShapeCircletList.append(ShapeCirclePencil(x, y))
                        S2.draw(WIN, x, y, drawing_color)
                        if DRAW_GRID_LINES:
                            for i in range(ROWS + 1):
                                pygame.draw.line(WIN, SILVER, (0, i * PIXEL_SIZE),
                                                 (WIDTH, i * PIXEL_SIZE))
                            for i in range(COLS + 1):
                                pygame.draw.line(WIN, SILVER, (i * PIXEL_SIZE, 0),
                                                 (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
                        pygame.display.flip()

    else:
        isPressed = False

        size = 0
        if BS == 1:
            size = 1
        if BS == 2:
            size = 3
        elif BS == 3:
            size = 5

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    isPressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = get_row_col_from_pos(pygame.mouse.get_pos())
                    list = CircleinGrid(x, y, size)
                    for i in list:
                        x, y = i
                        grid[x][y] = drawing_color

                    draw2(WIN, grid, buttons)
                    isPressed = False

                elif event.type == pygame.MOUSEMOTION and isPressed == True:
                    x, y = get_row_col_from_pos(pygame.mouse.get_pos())
                    list = CircleinGrid(x, y, size)
                    for i in list:
                        x, y = i
                        grid[x][y] = drawing_color

                    draw2(WIN, grid, buttons)
            points.clear()


def Text():
    font = pygame.font.Font(None, 15)
    # Set up the input box
    input_box = pygame.Rect(645, 80, 140, 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''

    # Run the game loop
    running = True
    while running:
        # Check for key press events
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                running = False
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        # text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Render the current text.
        # print("TEXT IN LOOP", text)
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = 40
        input_box.w = width
        # Blit the text.
        WIN.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(WIN, color, input_box, 2)
        pygame.display.flip()
        # running=False
        # Update the display
    print("TECXT IS", text)
    if text:
        print("hello")
        integer = int(text)
        print(integer)
        BRUSH_SIZE = text
        print(BRUSH_SIZE)
    else:
        # The string is empty, so don't try to convert it
        print("The string is empty")
    # r,c=get_row_col_from_pos(pos)
    # print(r,c)
    # paint_using_brush(r,c, BS)
    print("HELLO")
    print("TEH BS", BRUSH_SIZE)
    text = ' '
    return BRUSH_SIZE


def multiline():
    start = points[0]
    print("START")
    print(start)
    end = points[1]
    print("END")
    print(end)
    ML1 = MultiLine(start, end)
    MultiList.append(MultiLine(start, end))
    ML1.draw(WIN, ML1.start, ML1.end)
    pygame.display.flip()
    points.clear()


def DOT():
    start = points[0]
    print("START")
    print(start)
    end = points[1]
    print("END")
    print(end)
    D1 = DottedLine(start, end)
    DotList.append(DottedLine(start, end))
    D1.draw(WIN, D1.start, D1.end)

    # Update the display
    pygame.display.flip()
    points.clear()


# def antiali():
#     isPressed = False
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 isPressed = True
#             elif event.type == pygame.MOUSEBUTTONUP:
#                 # (x, y) = pygame.mouse.get_pos()  # returns the position of mouse cursor
#                 # pygame.draw.circle(WIN, BLUE, (x, y), 15)
#                 x, y = get_row_col_from_pos(pygame.mouse.get_pos())
#                 isPressed = False
#             elif event.type == pygame.MOUSEMOTION and isPressed == True:
#                 # (x, y) = pygame.mouse.get_pos()  # returns the position of mouse cursor
#                 x, y = get_row_col_from_pos(pygame.mouse.get_pos())
#                 gfxdraw.aacircle(WIN, x, y, 10, BLUE)
#                 gfxdraw.filled_circle(WIN, x, y, 10, BLUE)
#                 pygame.display.flip()
#                 # pygame.gfxdraw.line(WIN, start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, thickness, True)


def paint_using_brush(row, col, size):
    # if BRUSH_SIZE == 1:
    #     grid[row][col] = drawing_color
    #     # pygame.display.flip()
    # else:  # for values greater than 1
    #     r = row - BRUSH_SIZE + 1
    #     c = col - BRUSH_SIZE + 1

    #     for i in range(BRUSH_SIZE * 2 - 1):
    #         for j in range(BRUSH_SIZE * 2 - 1):
    #             if r + i < 0 or c + j < 0 or r + i >= ROWS or c + j >= COLS:
    #                 continue
    #             grid[r + i][c + j] = drawing_color

    modified = set()  # Set to store modified pixels
    BRUSH_SIZE = int(size)
    if BRUSH_SIZE == 1:
        index = row * COLS + col
        if index not in modified:
            grid[row][col] = drawing_color
            modified.add(index)
    else:  # for values greater than 1
        r = row - BRUSH_SIZE + 1
        c = col - BRUSH_SIZE + 1

        indices = range(min(BRUSH_SIZE * 2 - 1, ROWS - r))
        for i, ri in enumerate(indices):
            indices = range(min(BRUSH_SIZE * 2 - 1, COLS - c))
            for j, cj in enumerate(indices):
                index = (r + ri) * COLS + (c + cj)
                if index in modified:
                    break
                grid[r + ri][c + cj] = drawing_color
                modified.add(index)
    points.clear()

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
    points.clear()


def createButton2(buttonsSide, button_width, button_height):
    for i in range(11):
        if i == 0:
            continue
        else:
            if i == 1:
                buttonsSide.append(
                    Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                           "Enter Size",
                           name="Text", image_url="assets/Empty.png"))
            if i == 2:
                buttonsSide.append(
                    Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                           name="khaali", image_url="assets/Empty.png"))
            if i == 3:
                # Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                #        button_height, WHITE, "C" + str(i - 1), BLACK))
                buttonsSide.append(
                    Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                           button_height, WHITE, "SAVE BRUSH", BLACK)
                )


def createButton1(buttonsSide, button_width, button_height):
    for i in range(10):
        if i == 0:
            continue
            # buttonsSide.append(
            #     Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
            #         name="Change", image_url="assets/12.png"))  # Change toolbar buttons

        elif i == 1:
            buttonsSide.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="Straight Line", image_url="assets/Straightline.png"))  # append tools
        elif i == 2:
            buttonsSide.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="Dotted Line", image_url="assets/Dotted-line.png"))  # append tools
        elif i == 3:
            buttonsSide.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="Arrow", image_url="assets/Arrow.png"))  # append tools
        elif i == 4:
            buttonsSide.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="Multi Line", image_url="assets/Multi-Line.png"))  # append tools
        elif i == 7:
            buttonsSide.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="Shape1", image_url="assets/Shape1.png"))  # append tools

        elif i == 8:
            buttonsSide.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="Shape2", image_url="assets/Shape2.png"))  # append tools

        elif i == 9:
            buttonsSide.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="Shape3", image_url="assets/Circle.png"))  # append tools

        else:
            buttonsSide.append(
                Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width, button_height, WHITE,
                       name="empty", image_url="assets/Empty.png"))


run = True

clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
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
    Button(rtb_x - size_small / 2, 480, size_small,
           size_small, drawing_color, None, "ellipse"),
    Button(rtb_x - size_medium / 2, 510, size_medium,
           size_medium, drawing_color, None, "ellipse"),
    Button(rtb_x - size_large / 2, 550, size_large,
           size_large, drawing_color, None, "ellipse")
]

button_y_top_row = HEIGHT - TOOLBAR_HEIGHT / 2 - button_height - 1
button_y_bot_row = HEIGHT - TOOLBAR_HEIGHT / 2 + 1
button_space = 42

# draw2(WIN,grid,buttonsSide)
# Adding Buttons
buttons = []

for i in range(int(len(COLORS) / 2)):
    buttons.append(Button(100 + button_space * i, button_y_top_row,
                          button_width, button_height, COLORS[i]))

for i in range(int(len(COLORS) / 2)):
    buttons.append(
        Button(100 + button_space * i, button_y_bot_row, button_width, button_height, COLORS[i + int(len(COLORS) / 2)]))

# Right toolbar buttonst
# need to add change toolbar button.
# for i in range(10):
#     if i == 0:
#         buttons.append(Button(HEIGHT - 2*button_width,(i*button_height)+5,button_width,button_height,WHITE,name="Change"))#Change toolbar buttons
#     else: 
#         buttons.append(Button(HEIGHT - 2*button_width,(i*button_height)+5,button_width,button_height,WHITE,"B"+str(i-1), BLACK))#append tools

for i in range(10):
    if i == 0:
        buttons.append(
            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width, button_height, WHITE,
                   name="Change", image_url="assets/12.png"))  # Change toolbar buttons

    elif i == 1:
        buttons.append(
            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width, button_height, WHITE,
                   name="Straight Line", image_url="assets/Straightline.png"))  # append tools
    elif i == 2:
        buttons.append(
            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width, button_height, WHITE,
                   name="Dotted Line", image_url="assets/Dotted-line.png"))  # append tools
    elif i == 3:
        buttons.append(
            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width, button_height, WHITE,
                   name="Arrow", image_url="assets/Arrow.png"))  # append tools
    elif i == 4:
        buttons.append(
            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width, button_height, WHITE,
                   name="Multi Line", image_url="assets/Multi-Line.png"))  # append tools
    elif i == 7:
        buttons.append(
            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width, button_height, WHITE,
                   name="Shape1", image_url="assets/RHO.png"))  # append tools

    elif i == 8:
        buttons.append(
            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width, button_height, WHITE,
                   name="Shape2", image_url="assets/RECT.png"))  # append tools

    elif i == 9:
        buttons.append(
            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width, button_height, WHITE,
                   name="Shape3", image_url="assets/CIR.png"))  # append tools

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
buttons.append(
    Button(WIDTH - 3 * button_space + 5, button_y_top_row + 45, button_width - 5, button_height - 5, name="Pencil tool",
           image_url="assets/pencilTool.jpeg"))  # Pencil TOol
buttons.append(
    Button(WIDTH - 3 * button_space + 45, button_y_top_row + 45, button_width - 5, button_height - 5, name="Pen tool",
           image_url="assets/penTool.png"))
draw_button = Button(5, HEIGHT - TOOLBAR_HEIGHT /
                     2 - 30, 60, 60, drawing_color)
buttons.append(draw_button)

start_point = None
end_point = None
draw(WIN, grid, buttons)

while run:
    clock.tick(240)  # limiting FPS to 60 or any other value

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user closed the program
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_events(event)

            elif event.type == pygame.MOUSEBUTTONUP:
                handle_mouse_events(event)

            try:
                row, col = get_row_col_from_pos(pos)

                if STATE == "COLOR":
                    paint_using_brush(row, col, BRUSH_SIZE)
                    draw2(WIN, grid, buttons)

                elif STATE == "FILL":
                    fill_bucket(row, col, drawing_color)
                    draw2(WIN, grid, buttons)

                elif STATE == "SL":
                    print("STRAIGHT NAHI")
                    SL()

                elif STATE == "ARR":

                    # STATE = "COLOR"
                    # Change = False
                    # points = []
                    # SLlist = []
                    # ArrowList = []
                    # MultiList = []
                    # DotList = []
                    # points2=[]
                    # paint using bursh mai changes t fast, draw grid mai to make it fast

                    arrow()

                elif STATE == "MULTI":
                    print("MULTI MEIN")
                    multiline()

                elif STATE == "PEN":
                    print("Pen MEIN")
                    count += 1
                    print("count is")
                    print(count)
                    count1 = count
                    # # Run the game loop
                    done = done1
                    # start = points[0]
                    # end = points[1]
                    # prev = points[1]
                    # print(prev)
                    if count1 == 0:
                        start1 = points[0]
                    elif count1 == 1:

                        start1 = points[0]
                        print(start1)
                        start = points[0]
                        end = points[1]
                        prev = points[1]
                        polygon_points.append(start)
                        polygon_points.append(end)
                        SL1 = StraightLine(start, end)
                        pygame.draw.line(WIN, (0, 0, 0), SL1.start, SL1.end)
                        pygame.display.flip()
                        points.clear()
                        print("less 1")
                        print("Start")
                        print(start)
                        print(end)
                        print(prev)
                        # count1 = 1
                    elif count1 == 5:
                        start = prev
                        end = points[0]
                        prev = end
                        polygon_points.append(start)
                        polygon_points.append(end)
                        print(start)
                        print(end)
                        SL1 = StraightLine(start, end)
                        pygame.draw.line(WIN, (0, 0, 0), SL1.start, SL1.end)
                        pygame.display.flip()
                        points.clear()
                        pygame.draw.line(WIN, (0, 0, 0), SL1.end, start1)
                        pygame.draw.polygon(WIN, (0, 0, 0), polygon_points)
                        polygon_shapeL.append(polygon_points)
                        # STATE = "COLOR"
                        pygame.display.flip()
                        # polygon_points.clear()
                        points.clear()
                        count = -1
                        prev = None
                        start1 = None
                        # polygon_points = []

                    else:
                        print("else main")
                        print("Start")

                        start = prev
                        end = points[0]
                        prev = end
                        polygon_points.append(start)
                        polygon_points.append(end)
                        print(start)
                        print(end)
                        SL1 = StraightLine(start, end)
                        pygame.draw.line(WIN, (0, 0, 0), SL1.start, SL1.end)
                        pygame.display.flip()
                        points.clear()
                        print("less not")

                elif STATE == "PENCIL":
                    print("hello")

                elif STATE == "SB":
                    print("SB MEIN")
                    grid = init_grid(ROWS, COLS, BG_COLOR)
                    draw2(WIN, grid, buttons)
                    drawing_color = BLACK
                    draw_button.color = drawing_color
                    pygame.display.flip()
                    done1 = True
                    count = -1
                    prev = None
                    start1 = None
                    # polygon_points = []
                    count = -1

                    # print (points[0])
                    sb = SaveBrush()
                    a, b = points[0]
                    print(a)
                    print(b)

                    center_x = sum(x for (x, y) in polygon_points) / \
                               len(polygon_points)
                    center_y = sum(y for (x, y) in polygon_points) / \
                               len(polygon_points)
                    target_x, target_y = points[0]
                    dx = target_x - center_x
                    dy = target_y - center_y

                    # apply the translation transformation to each vertex of the polygon
                    translated_points = [(x + dx, y + dy)
                                         for (x, y) in polygon_points]
                    for i in translated_points:
                        print(i)
                        r, c = get_row_col_from_pos(i)
                        if inBounds(r, c) == 0:
                            inboundcheck = False
                            print(inboundcheck)
                    for i in Translated_pointsL:
                        # pygame.draw.polygon(WIN, RED, i)
                        sb.draw(WIN, drawing_color, i)
                        if DRAW_GRID_LINES:
                            for i in range(ROWS + 1):
                                pygame.draw.line(WIN, SILVER, (0, i * PIXEL_SIZE),
                                                 (WIDTH, i * PIXEL_SIZE))
                            for i in range(COLS + 1):
                                pygame.draw.line(WIN, SILVER, (i * PIXEL_SIZE, 0),
                                                 (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
                        pygame.display.flip()
                    if (inboundcheck == False):
                        break
                    Translated_pointsL.append(translated_points)
                    # if inboundcheck == False:
                    #     break

                    # for i in polygon_points:
                    #     print(i)
                    #     x,y = i
                    #     print("for mein")
                    #     print(x+(x-a))
                    #     print(y+(y-b))
                    #     polygon_points2.append((x-(x-a),y-(y-b)))
                    for i in Translated_pointsL:
                        sb.draw(WIN, drawing_color, i)
                        if DRAW_GRID_LINES:
                            for i in range(ROWS + 1):
                                pygame.draw.line(WIN, SILVER, (0, i * PIXEL_SIZE),
                                                 (WIDTH, i * PIXEL_SIZE))
                            for i in range(COLS + 1):
                                pygame.draw.line(WIN, SILVER, (i * PIXEL_SIZE, 0),
                                                 (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
                        pygame.display.flip()
                        # pygame.draw.polygon(WIN, RED, i)

                    pygame.display.flip()
                    points = []
                    break

                elif STATE == "DOT":
                    print("DOT MEIN")
                    DOT()

                elif STATE == "SHP1":
                    print("Shape 1 MEIN")
                    shapedBrush1(BRUSH_SIZE)

                elif STATE == "SHP2":
                    print("Shape 2 MEIN")
                    # brush_widths.clear()
                    # draw_brush_widthsRect(WIN)
                    shapedBrush2(BRUSH_SIZE)

                elif STATE == "SHP3":
                    print("Shape 3 MEIN")
                    shapedBrush3(BRUSH_SIZE)

                elif STATE == "TXT":
                    print("Text MEIN")
                    BRUSH_SIZE = Text()

            except IndexError:

                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    # if button.text == "Clear":
                    #     grid = init_grid(ROWS, COLS, BG_COLOR)
                    #     drawing_color = BLACK
                    #     draw_button.color = drawing_color
                    #     STATE = "COLOR"
                    #     Change = False
                    #     points = []
                    #     SLlist = []
                    #     ArrowList = []
                    #     MultiList = []
                    #     DotList = []
                    #     points2 = []
                    #     # paint using bursh mai changes t fast, draw grid mai to make it fast
                    #     done1 = True
                    #     count = -1
                    #     prev = None
                    #     start1 = None
                    #     polygon_points = []
                    #     count = -1
                    #     break

                    if button.name == "FillBucket":
                        STATE = "FILL"
                        break
                    if not button.clicked(pos):
                        continue
                    if button.text == "Clear":
                        Change = False
                        points = []
                        SLlist = []
                        ArrowList = []
                        MultiList = []
                        DotList = []
                        points2 = []
                        ShapedRectList = []
                        ShapeCircletList = []
                        ShapedRhombusList = []
                        Translated_pointsL = []
                        done1 = True
                        count = -1
                        prev = None
                        start1 = None
                        polygon_points = []
                        polygon_shapeL = []
                        input_box = None
                        colorTxtBox = None
                        BRUSH_SIZE = 1
                        inboundcheck = True
                        pencilClicked = False
                        dontcalpoints = False
                        shape = False
                        SB=None
                        STATE = "COLOR"
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                        draw_button.color = drawing_color
                        draw(WIN, grid, buttons)
                        pygame.display.update()
                        break

                    if button.name == "FillBucket":
                        STATE = "FILL"
                        break

                    if button.name == "Pencil tool":
                        pencilClicked = not pencilClicked
                        print(pencilClicked)
                        STATE = "PENCIL"
                        break

                    if button.name == "Pen tool":
                        STATE = "PEN"
                        break
                    if button.name == "SB":
                        STATE = "SB"
                        break

                    if button.name == "CB":
                        STATE = "CB"
                        break

                    if button.name == "Straight Line":
                        STATE = "SL"
                        print("STRIAGHT BUTTON BEING CLICKED")
                        break

                    if button.name == "Arrow":
                        STATE = "ARR"
                        print("ARROW BUTTON BEING CLICKED")
                        break

                    if button.name == "Multi Line":
                        STATE = "MULTI"

                        print("MULTI BUTTON BEING CLICKED")
                        break

                    if button.name == "Dotted Line":
                        STATE = "DOT"
                        print("Dotted BUTTON BEING CLICKED")
                        break

                    if button.name == "Shape1":
                        STATE = "SHP1"
                        shape = True
                        print("Shape1 BUTTON BEING CLICKED")
                        break

                    if button.name == "Shape2":
                        STATE = "SHP2"
                        shape = True
                        print("Shape2 BUTTON BEING CLICKED")
                        break

                    if button.name == "Shape3":
                        STATE = "SHP3"
                        shape = True
                        print("Shape3 BUTTON BEING CLICKED")
                        break

                    if button.name == "Text":
                        STATE = "TXT"
                        BRUSH_SIZE = Text()
                        print("TEXT BUTTON BEING CLICKED")
                        break

                    if button.name == "Change":
                        # Change = not Change
                        # print(Change)
                        # for i in range(10):
                        #     if i == 0:
                        #         buttons.append(Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                        #                               button_height, WHITE, name="Change", image_url="assets/22.png"))
                        #     else:
                        #         if Change == False:
                        #             createButton1(buttons, button_width, button_height)
                        #         else:
                        #             # buttons.clear()
                        #             # pygame.display.update()
                        #             buttons.append(
                        #                 Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                        #                        button_height, WHITE, "C" + str(i - 1), BLACK))

                        #     draw2(WIN, grid, buttons)
                        Change = not Change
                        print("here")
                        for i in range(10):
                            if i == 0:
                                buttons.append(
                                    Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                                           button_height, WHITE,
                                           name="Change", image_url="assets/12.png"))
                            else:
                                if Change == True:
                                    for button in buttons:
                                        if button.name == "Straight Line":
                                            buttons.remove(button)
                                            break
                                        elif button.name == "Change":
                                            buttons.remove(button)
                                            break
                                        elif button.name == "Arrow":
                                            buttons.remove(button)
                                            break

                                        elif button.name == "Multi Line":
                                            buttons.remove(button)
                                            break

                                        elif button.name == "Dotted Line":
                                            buttons.remove(button)
                                            break

                                        elif button.name == "Shape1":
                                            buttons.remove(button)
                                            break

                                        elif button.name == "Shape2":
                                            buttons.remove(button)
                                            break

                                        elif button.name == "Shape3":
                                            buttons.remove(button)
                                            break
                                    # draw2(WIN, grid, buttons)
                                    draw(WIN, grid, buttons)
                                    pygame.display.flip()
                                    buttons.append(
                                            Button(HEIGHT - 2 * button_width + 25, (0 * button_height) + 5,
                                                   button_width,
                                                   button_height, WHITE,
                                                   name="Change", image_url="assets/22.png"))
                                    if i == 1:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width, (i * button_height) + 5,
                                                   button_width + 50, button_height, WHITE,
                                                   "Enter Size", BLACK,
                                                   name="Text", image_url="assets/Empty.png"))
                                    elif i == 2:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width, (i * button_height) + 5, button_width,
                                                   button_height, WHITE,
                                                   name="khaali", image_url="assets/Empty.png"))
                                    elif i == 3:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width, (i * button_height) + 5,
                                                   button_width + 50,
                                                   button_height, WHITE, "SAVE BRUSH", BLACK, name="SB")
                                        )
                                    elif i == 5:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width, (i * button_height) + 5,
                                                   button_width + 50,
                                                   button_height, BLACK, "Custom Brush", WHITE, shape="ellipse",
                                                   name="CB")
                                        )

                                if Change == False:
                                    for button in buttons:
                                        if button.name == "Text":
                                            buttons.remove(button)
                                            break
                                        elif button.name == "Change":
                                            print(button.name)
                                            buttons.remove(button)
                                            break
                                        elif button.name == "SB":
                                            buttons.remove(button)
                                            break

                                        elif button.name == "CB":
                                            buttons.remove(button)
                                            break
                                    draw(WIN, grid, buttons)
                                    pygame.display.flip()
                                    if i == 1:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width,
                                                   button_height, WHITE,
                                                   name="Straight Line",
                                                   image_url="assets/Straightline.png"))  # append tools
                                    elif i == 2:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width,
                                                   button_height, WHITE,
                                                   name="Dotted Line",
                                                   image_url="assets/Dotted-line.png"))  # append tools
                                    elif i == 3:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width,
                                                   button_height, WHITE,
                                                   name="Arrow", image_url="assets/Arrow.png"))  # append tools
                                    elif i == 4:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width,
                                                   button_height, WHITE,
                                                   name="Multi Line",
                                                   image_url="assets/Multi-Line.png"))  # append tools
                                    elif i == 7:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width,
                                                   button_height, WHITE,
                                                   name="Shape1", image_url="assets/RHO.png"))  # append tools

                                    elif i == 8:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width,
                                                   button_height, WHITE,
                                                   name="Shape2", image_url="assets/RECT.png"))  # append tools

                                    elif i == 9:
                                        buttons.append(
                                            Button(HEIGHT - 2 * button_width+25, (i * button_height) + 5, button_width,
                                                   button_height, WHITE,
                                                   name="Shape3", image_url="assets/CIR.png"))  # append tools

                        draw(WIN, grid, buttons)
                        draw2(WIN, grid, buttons)
                        # draw2(WIN, grid, buttonsSide)
                        pygame.display.update()
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
                        print("HERE")
                        BRUSH_SIZE = 1
                    elif button.width == size_medium:
                        print("jdj")
                        BRUSH_SIZE = 2
                    elif button.width == size_large:
                        BRUSH_SIZE = 3
                        print("3 here")

                    # STATE = "COLOR"

pygame.quit()
