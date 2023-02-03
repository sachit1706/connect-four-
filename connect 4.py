import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
adjust_size = 100
WINDOW_WIDTH = 7 * adjust_size
WINDOW_HEIGHT = 6 * adjust_size
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
coins = [[0 for i in range(7)] for j in range(6)]
turn = RED


def game():
    global SCREEN
    global run
    pygame.init()
    pygame.display.set_caption("Connect 4")
    SCREEN.fill(WHITE)
    run = True

    while run:
        grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                place_piece()
        pygame.display.update()


def grid():
    for j in range(6):
        for i in range(7):
            box = pygame.Rect(i * adjust_size, j * adjust_size, adjust_size, adjust_size)
            pygame.draw.rect(SCREEN, BLACK, box, 1)


def place_piece():
    global turn
    coords = pygame.mouse.get_pos()
    mouse_x = coords[0] // adjust_size
    mouse_y = coords[1] // adjust_size
    if coins[mouse_y][mouse_x] != 0:
        return
    for i in range(5, -1, -1):
        if coins[i][mouse_x] == 0:
            coins[i][mouse_x] = turn
            pygame.draw.circle(SCREEN,
                               turn,
                               (mouse_x * adjust_size + adjust_size / 2,
                                i * adjust_size + adjust_size / 2),
                               adjust_size // 2,
                               adjust_size // 2,
                               )
            if turn == RED:
                turn = YELLOW
            else:
                turn = RED
            check()
            break


def win_message():
    if turn == RED:
        winner = 'Yellow Wins'
    else:
        winner = 'Red Wins'
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render(winner, True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = 350, 300
    SCREEN.blit(text, text_rect)


def check():
    global run
    # let i = row, j = coluumns
    # row checker
    for i in range(6):
        for j in range(4):
            ppap = coins[i][j]
            if ppap != 0:
                perhaps_win = True
                while perhaps_win:
                    for a in range(1, 4):
                        if coins[i][j + a] != ppap:
                            perhaps_win = False
                            break
                    if perhaps_win:
                        win_message()
                        run = False
                        return

    # column checker
    for j in range(7):
        for i in range(3):
            ppap = coins[i][j]
            if ppap != 0:
                perhaps_win = True
                while perhaps_win:
                    for a1 in range(1, 4):
                        if coins[i + a1][j] != ppap:
                            perhaps_win = False
                            break
                    if perhaps_win:
                        win_message()
                        run = False
                        return

    # diagnal checker
    for i in range(3):
        for j in range(4):
            ppap = coins[i][j]
            if ppap != 0:
                perhaps_win = True
                while perhaps_win:
                    for a2 in range(1, 4):
                        if coins[i + a2][j + a2] != ppap:
                            perhaps_win = False
                            break
                    if perhaps_win:
                        win_message()
                        run = False
                        return

    # other diagonal checker
    for i in range(3,6):
        for j in range(3):
            ppap = coins[i][j]
            if ppap != 0:
                perhaps_win = True
                while perhaps_win:
                    for a3 in range(1, 4):
                        if coins[i - a3][j + a3] != ppap:
                            perhaps_win = False
                            break
                    if perhaps_win:
                        win_message()
                        run = False
                        return


game()
