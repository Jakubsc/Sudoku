from math import floor
import pygame


def solve(board:list)-> bool:
    '''
    This function solves a sudoku using brute force + if it is wrong it will back track. 
    It is implemented with a recursion
    '''
    position = find_empty(board)
    if position:
        y, x = position
    else:
        return True

    for i in range(9):
        if valid(board, i+1, x, y):
            board[y][x] = i+1
            if(solve(board)):
                return True
            board[y][x] = 0
    return False


def solve_and_show(screen, board:list,my_font)->bool:
    '''
    This function solves a sudoku using brute force + if it is wrong it will back track and 
    also it will call function draw to draw squares. 
    It is implemented with a recursion
    '''
    position = find_empty(board)
    red = (255, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    if position:
        y, x = position
    else:
        return True

    for i in range(9):  # trying all numbers in one spot
        if valid(board, i+1, x, y):
            board[y][x] = i+1
            display = my_font.render(str(board[y][x]), 1, white)
            draw(screen, x, y, green)
            if x % 3:
                # displaying number
                screen.blit(display, (x*52+(x//3-1)*2+17, y*52+(y//3-1)*2+8))
            else:
                screen.blit(display, (x*52+(x//3)*2+17, y*52+(y//3)*2+8))
            pygame.time.delay(100)
            pygame.display.flip()
            if(solve_and_show(screen, board, my_font)):
                return True
            board[y][x] = 0
            pygame.draw.rect(screen, (0, 0, 0), (x*52+(x//3)
                                                 * 2+2, y*52+(y//3)*2+2, 49, 49))
            draw(screen, x, y, red)
    return False


def valid(board:list, num:int, x:int, y:int)->bool:
    """
    checks if num is valid in particular spot on the board
    therefore check:
    3x3 square, line and
    """
    for i in range(9):
        # checks if there is a same value in same row or column
        if((board[y][i] == num) or (board[i][x] == num)):
            return False
    x = floor(x/3)
    y = floor(y/3)
    for i in range(y*3, y*3+3):  # checks if in 3x3 square is already that number
        for j in range(x*3, x*3+3):
            if(board[i][j] == num):
                return False
    return True


def find_empty(bo:list)->tuple or None:
    """
    find empty tile on a board
    """
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return(i, j)
    return None


def draw(screen, x:int, y:int, colour:tuple)->None:  # drawing square
    """
    draw a square on a screen on coordinates x and y with specified colour
    """
    pygame.draw.line(screen, colour, (x*52+(x//3)*2, y*52+(y//3)*2),
                     ((x+1)*52+(x//3)*2, y*52+(y//3)*2), 2)  # upper line
    pygame.draw.line(screen, colour, (x*52+(x//3)*2, y*52+(y//3)*2),
                     (x*52+(x//3)*2, (y+1)*52+(y//3)*2), 2)  # left line
    pygame.draw.line(screen, colour, ((x+1)*52+(x//3)*2, (y+1)*52+(y//3)*2),
                     ((x+1)*52+(x//3)*2, y*52+(y//3)*2), 2)  # right line
    pygame.draw.line(screen, colour, ((x+1)*52+(x//3)*2, (y+1)*52+(y//3)*2),
                     (x*52+(x//3)*2, (y+1)*52+(y//3)*2), 2)  # lower line
    pygame.display.flip()

def main()->None:
    """
    drawing grid, drawing numbers,checks for all events on the keyboard and mouse
    """
    board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    users_board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    # this we will use as tool to compare when user put number in a marked square
    solve(board)
    pygame.init()
    background_colour = (0, 0, 0)  # black
    white = (255, 255, 255)
    green = (0, 255, 0)
    (width, height) = (476, 500)

    my_font = pygame.font.SysFont("Times New Roman", 40)
    screen = pygame.display.set_mode((width, height))
    screen.fill(background_colour)

    for i in range(0, 10):  # drawing lines
        if i % 3 == 0 and i != 0:
            pygame.draw.line(screen, white, (i*52+(i//3)*2-1, 0),
                            (i*52+(i//3)*2-1, 474), 4)
            pygame.draw.line(screen, white, (0, i*52+(i//3)*2-1),
                            (474, i*52+(i//3)*2-1), 4)

        else:
            pygame.draw.line(screen, white, (i*52+(i//3)*2, 0),
                            (i*52+(i//3)*2, 474), 2)
            pygame.draw.line(screen, white, (0, i*52+(i//3)*2),
                            (474, i*52+(i//3)*2), 2)


    for y in range(0, 9):  # drawing numbers
        for x in range(0, 9):
            if(users_board[y][x] != 0):
                display = my_font.render(str(users_board[y][x]), 1, white)
                if y % 3 and y != 0:
                    screen.blit(display, (x*52+(x//3-1)*2+17, y*52+(y//3-1)*2+8))
                else:
                    screen.blit(display, (x*52+(x//3)*2+17, y*52+(y//3)*2+8))
    pygame.display.set_caption('Sudoku')
    pygame.display.flip()
    running = True
    marked = False
    x_prev = -1
    y_prev = -1
    key = None
    while running:
        for event in pygame.event.get(): #this checks for all events on the keyboard and mouse
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in(pygame.K_KP1,pygame.K_1):
                    key = 1
                if event.key in(pygame.K_KP2,pygame.K_2):
                    key = 2
                if event.key in(pygame.K_KP3,pygame.K_3):
                    key = 3
                if event.key in(pygame.K_KP4,pygame.K_4):
                    key = 4
                if event.key in(pygame.K_KP5,pygame.K_5):
                    key = 5
                if event.key in(pygame.K_KP6,pygame.K_6):
                    key = 6
                if event.key in(pygame.K_KP7,pygame.K_7):
                    key = 7
                if event.key in(pygame.K_KP8,pygame.K_8):
                    key = 8
                if event.key in(pygame.K_KP9,pygame.K_9):
                    key = 9
                if event.key == pygame.K_SPACE:
                    if marked:
                        draw(screen, x, y, white)
                    solve_and_show(screen, users_board, my_font)

                if key is not None: #this part coresponds to when a user already pressed a number on a keyboard
                    if marked:
                        display = my_font.render(str(key), 1, white)
                        if(users_board[y][x] == 0):
                            if(key == board[y][x]):
                                users_board[y][x] = key
                                print("*******")
                                print("Succes!")
                                print("*******")
                                if x_prev % 3 and x_prev != 0:  # drawing succesful number
                                    screen.blit(
                                        display, (x_prev*52+(x_prev//3-1)*2+17, y_prev*52+(y_prev//3-1)*2+8))
                                else:
                                    screen.blit(
                                        display, (x_prev*52+(x_prev//3)*2+17, y_prev*52+(y_prev//3)*2+8))
                                pygame.display.flip()
                            else:
                                print("------")
                                print("Wrong!")
                                print("------")
                        else:
                            print("mark empty square")
                    else:
                        print("mark empty square")

            elif event.type == pygame.MOUSEBUTTONUP: #this part coresponds to when user clicks on a tile and it will show a marked tile on the screen.
                pos = pygame.mouse.get_pos()
                x_rem = 0
                y_rem = 0
                if(pos[0] > 156):#this part is beacuse we have 2 middle lines that are 2 pixels wider than the other ones
                    if(pos[0] > 316):
                        x_rem += 2
                    x_rem += 2
                x = (pos[0]-x_rem)//52
                if(pos[1] > 156):#this part is beacuse we have 2 middle lines that are 2 pixels wider than the other ones
                    if(pos[1] > 316):
                        y_rem += 2
                    y_rem += 2
                y = (pos[1]-y_rem)//52

                if marked:#this is when user clicks somewhere else it will draw a white square on the last spot and draw a green one to the new spot
                    draw(screen, x_prev, y_prev, white)
                draw(screen, x, y, green)
                marked = True
                x_prev = x
                y_prev = y
main()
