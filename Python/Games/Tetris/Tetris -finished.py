import pygame, random

pygame.init()

WIDTH, HEIGHT = 400, 850
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris by Daniel Kaiser")

font = pygame.font.SysFont("comicsans", 40)

FPS = 60

white = (255, 255, 255)

RED = (255, 0, 0)

rows = 20
colums = 10
square_size = 40

points = 0

count = 0

fill_clear_line = False

squares = [False] * 200 + [True] * 10

game_over = False

OG_Pos = [
    [3, 4, 5, 6],  # Line-piece
    [3, 13, 14, 15],  # J-Piece
    [5, 13, 14, 15],  # L-Piece
    [4, 5, 13, 14],  # S-piece
    [4, 13, 14, 15],  # T-piece
    [3, 4, 14, 15],  # Z-piece
    [4, 5, 14, 15],  # square-piece
]

rot_vars = [
    [
        [[-11, 0, 11, 22], [-9, 0, 9, 18], [11, 0, -11, -22], [9, 0, -9, - 18]],
        [[9, 0, -9, -18], [-11, 0, 11, 22], [-9, 0, 9, 18], [11, 0, -11, -22]],
    ],
    [
        [[-20, -11, 0, 11], [2, -9, 0, 9], [20, 11, 0, -11], [-2, 9, 0, -9]],
        [[-2, 9, 0, -9], [-20, -11, 0, 11], [2, -9, 0, 9], [20, 11, 0, -11]],
    ],
    [
        [[2, -11, 0, 11], [20, -9, 0, 9], [-2, 11, 0, -11], [-20, 9, 0, -9]],
        [[-20, 9, 0, -9], [2, -11, 0, 11], [20, -9, 0, 9], [-2, 11, 0, -11]],
    ],
    [
        [[-9, 2, -11, 0], [11, 20, -9, 0], [9, -2, 11, 0], [-11, -20, 9, 0]],
        [[-11, -20, 9, 0], [-9, 2, -11, 0], [11, 20, -9, 0], [9, -2, 11, 0]],
    ],
    [
        [[-9, -11, 0, 11], [11, -9, 0, 9], [9, 11, 0, -11], [-11, 9, 0, -9]],
        [[-11, 9, 0, -9], [-9, -11, 0, 11], [11, -9, 0, 9], [9, 11, 0, -11]],
    ],
    [
        [[-20, -9, 0, 11], [2, 11, 0, 9], [20, 9, 0, -11], [-2, -11, 0, -9]],
        [[-2, -11, 0, -9], [-20, -9, 0, 11], [2, 11, 0, 9], [20, 9, 0, -11]],
    ],
    [
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    ],
]

colors = [
    (0, 255, 255),
    (0, 0, 255),
    (255, 127, 0),
    (0, 255, 0),
    (128, 0, 128),
    (255, 0, 0),
    (255, 255, 0),
]


class Pieces:
    def __init__(self):
        self.index = random.randint(0, 6)
        self.rot_pos = 0
        self.color = colors[self.index]
        self.piece = OG_Pos[self.index]
        self.disabled = False


Shapes = [Pieces()]


def main():
    global count, run

    clock = pygame.time.Clock()

    run = True

    while run:

        count += 1

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()

        draw_grid()

        if count % 5 == 0 and fill_clear_line == False:
            handle_pieces(key_pressed)

        clear_lines()
        set_squares()

        if count % 15 == 0 and fill_clear_line == True:
            move_cleared()

        clean_Shapes()

        reset_OG_Pos()

        fill_grid()

        update_window()

    pygame.quit()


def handle_pieces(key_pressed):
    global count

    if count % 30 == 0 or key_pressed[pygame.K_s]:
        down()
        count = 0


    if key_pressed[pygame.K_a]:
        left()

    if key_pressed[pygame.K_d]:
        right()

    if key_pressed[pygame.K_SPACE] and count % 10 == 0:
        rotate(0)
    elif key_pressed[pygame.K_LSHIFT] and count % 10 == 0:
        rotate(1)

def clear_lines():
    global fill_clear_line,points

    full_line = False

    filled_rows = []
    
    for row in range(20):

        filled_squares = 0

        for columns in range(10):
            if squares[row*10 + columns] == True:
                filled_squares += 1

        if filled_squares == 10:
            filled_rows.insert(0,row)
            full_line = True

    if full_line == True:

        points += len(filled_rows) * 10

        for row in range(len(filled_rows)):
            for column in range(10):
                for i in range(len(Shapes)):

                    to_remove = []

                    for n in range(len(Shapes[i].piece)):

                        if Shapes[i].piece[n] == filled_rows[row]*10 + column:
                            to_remove.append([i,n])
                    for n in range(len(to_remove)):    
                        Shapes[to_remove[n][0]].piece.pop(to_remove[n][1])
        
        fill_clear_line = True

def move_cleared():
    global fill_clear_line

    fill_clear_line = False

    for i in range(len(Shapes)):        
        for n in range(len(Shapes[i].piece)):
            
            if squares[Shapes[i].piece[n] + 10] == False:
                Shapes[i].piece[n] += 10
                fill_clear_line = True

    if Shapes[-1].disabled == True and fill_clear_line == False:
        Shapes.append(Pieces())

def down():

    for i in range(len(Shapes)):
        if Shapes[i].disabled == False:

            collision = collisions(Shapes[i].piece, 10)

            if collision == False:
                for n in range(len(Shapes[i].piece)):
                    Shapes[i].piece[n] += 10
            elif collision == True:
                Shapes[-1].disabled = True
                end_game()
                Shapes.append(Pieces())


def left():
    at_left_1 = False
    at_left_2 = False

    for n in range(len(Shapes[-1].piece)):
        if Shapes[-1].piece[n] % 10 == 0:
            at_left_1 = True

    at_left_2 = collisions(Shapes[-1].piece, -1)

    if at_left_1 == False and at_left_2 == False:
        for n in range(len(Shapes[-1].piece)):
            Shapes[-1].piece[n] -= 1

def right():

    at_right_1 = False
    at_right_2 = False

    for n in range(len(Shapes[-1].piece)):
        if Shapes[-1].piece[n] % 10 == 9:
            at_right_1 = True

    at_right_2 = collisions(Shapes[-1].piece, 1)

    if at_right_1 == False and at_right_2 == False:
        for n in range(len(Shapes[-1].piece)):
            Shapes[-1].piece[n] += 1

def rotate(rot_direc):

    if rot_direc == 0:
        Shapes[-1].rot_pos += 1
    elif rot_direc == 1:
        Shapes[-1].rot_pos -= 1

    if Shapes[-1].rot_pos == -1:
        Shapes[-1].rot_pos = 3
    elif Shapes[-1].rot_pos == 4:
        Shapes[-1].rot_pos = 0

    for i in range(len(Shapes[-1].piece)):
        Shapes[-1].piece[i] += rot_vars[Shapes[-1].index][rot_direc][Shapes[-1].rot_pos][i]


def collisions(piece, direc):

    arr = []

    for i in range(len(piece)):

        contact = False

        for n in range(len(piece)):
            if piece[n] == piece[i] + 1 * direc:
                contact = True
                break

        if contact == False:
            arr.append(piece[i])

    for i in range(len(arr)):
        if squares[arr[i] + 1 * direc] == True:
            return True

    return False

def clean_Shapes():
    remove = []
    for i in range(len(Shapes)):
        if Shapes[i].piece == []:
            remove.append(i)

    for i in range(len(remove)):
        Shapes.pop(remove[i]-i)


def set_squares():
    for i in range(len(squares) - 10):
        squares[i] = False

    for i in range(len(Shapes)):
        for n in range(len(Shapes[i].piece)):
            squares[Shapes[i].piece[n]] = True

def end_game():
    global run
    for i in range(len(Shapes[-1].piece)):
        if Shapes[-1].piece[i] <= 9:
            pygame.time.delay(5000)
            run = False


def reset_OG_Pos():
    global OG_Pos

    OG_Pos = [
        [3, 4, 5, 6],  # Line-piece
        [3, 13, 14, 15],  # J-Piece
        [5, 13, 14, 15],  # L-Piece
        [4, 5, 13, 14],  # S-piece
        [4, 13, 14, 15],  # T-piece
        [3, 4, 14, 15],  # Z-piece
        [4, 5, 14, 15],  # square-piece
    ]


def fill_grid():

    for i in range(len(Shapes)):
        for n in range(len(Shapes[i].piece)):
            x = int(Shapes[i].piece[n] % 10) * square_size
            y = int(Shapes[i].piece[n] / 10) * square_size + 50

            pygame.draw.rect(
                window, Shapes[i].color, (x, y, square_size, square_size), square_size
            )


def draw_grid():
    for i in range(colums):
        pygame.draw.line(window, white, (i * 40, 50), (i * 40, HEIGHT))
    for i in range(rows):
        pygame.draw.line(window, white, (0, i * 40 + 50), (WIDTH, i * 40 + 50))

    point_text = font.render("Points:"+str(points), 1, (255,255,255))

    window.blit(point_text,(1,0))


def update_window():
    pygame.display.flip()
    pygame.display.update()
    window.fill((0, 0, 0))


if __name__ == "__main__":
    main()
