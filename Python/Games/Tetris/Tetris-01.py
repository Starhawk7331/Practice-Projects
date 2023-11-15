import pygame, random
from pygame.math import Vector2

pygame.init()

WIDTH, HEIGHT = 400, 850
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

font = pygame.font.SysFont("comicsans", 40)

FPS = 60


white = (255, 255, 255)
colors = [
    (145, 32, 167),
    (40, 227, 240),
    (208, 215, 115),
    (210, 4, 4),
    (210, 4, 4),
    (4, 11, 210),
    (4, 11, 210),
]

rows = 20
colums = 10
square_size = 40

button_queue = []


pieces = [
    [
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2 - 40, 90),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2 + 80, 130),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2 + 40, 90),
            Vector2(WIDTH / 2 + 40, 50),
        ],  # rot 1
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 - 40, 170),
            Vector2(WIDTH / 2, 170),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 + 40, 90),
            Vector2(WIDTH / 2, 90),
        ],
        [
            Vector2(WIDTH / 2 + 80, 50),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2 + 40, 90),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2 - 40, 90),
            Vector2(WIDTH / 2 - 40, 50),
        ],
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2 + 40, 50),
            Vector2(WIDTH / 2 + 40, 170),
            Vector2(WIDTH / 2, 170),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2 - 40, 90),
            Vector2(WIDTH / 2, 90),
        ],
    ],  # T-Piece
    [
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2, 210),
            Vector2(WIDTH / 2 + 40, 210),
            Vector2(WIDTH / 2 + 40, 50),
        ],
        [
            Vector2(WIDTH / 2 - 80, 50),
            Vector2(WIDTH / 2 - 80, 90),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2 + 80, 50),
        ],
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2, 210),
            Vector2(WIDTH / 2 + 40, 210),
            Vector2(WIDTH / 2 + 40, 50),
        ],
        [
            Vector2(WIDTH / 2 - 80, 50),
            Vector2(WIDTH / 2 - 80, 90),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2 + 80, 50),
        ],
    ],  # Line-Piece
    [
        [
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 + 40, 50),
        ],
        [
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 + 40, 50),
        ],
        [
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 + 40, 50),
        ],
        [
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 + 40, 50),
        ],
    ],  # Square-Piece
    [
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2 - 40, 90),
            Vector2(WIDTH / 2 - 40, 170),
            Vector2(WIDTH / 2, 170),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 + 40, 50),
        ],
        [
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 + 40, 50),
            Vector2(WIDTH / 2 + 40, 90),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2 + 80, 130),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2 - 40, 90),
        ],
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2 - 40, 90),
            Vector2(WIDTH / 2 - 40, 170),
            Vector2(WIDTH / 2, 170),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 + 40, 50),
        ],
        [
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 + 40, 50),
            Vector2(WIDTH / 2 + 40, 90),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2 + 80, 130),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2 - 40, 90),
        ],
    ],  # S-Piece mirrored
    [
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2, 170),
            Vector2(WIDTH / 2 + 40, 170),
            Vector2(WIDTH / 2 + 40, 90),
            Vector2(WIDTH / 2, 90),
        ],
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2 + 80, 50),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2 + 40, 90),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2 - 40, 90),
            Vector2(WIDTH / 2, 90),
        ],
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2, 170),
            Vector2(WIDTH / 2 + 40, 170),
            Vector2(WIDTH / 2 + 40, 90),
            Vector2(WIDTH / 2, 90),
        ],
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2 + 80, 50),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2 + 40, 90),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2 - 40, 90),
            Vector2(WIDTH / 2, 90),
        ],
    ],  # S-Piece
    [
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2 - 40, 130),
            Vector2(WIDTH / 2 - 40, 170),
            Vector2(WIDTH / 2 + 40, 170),
            Vector2(WIDTH / 2 + 40, 50),
        ],
        [
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2 + 80, 130),
            Vector2(WIDTH / 2 - 40, 130),
        ],
        [
            Vector2(WIDTH / 2 + 40, 50),
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 - 40, 170),
            Vector2(WIDTH / 2, 170),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2 + 40, 90),
        ],
        [
            Vector2(WIDTH / 2 + 40, 50),
            Vector2(WIDTH / 2 - 80, 50),
            Vector2(WIDTH / 2 - 80, 90),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2 + 40, 130),
        ],
    ],  # L-Piece mirrored
    [
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 - 40, 170),
            Vector2(WIDTH / 2 + 40, 170),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2, 50),
        ],
        [
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 + 80, 50),
            Vector2(WIDTH / 2 + 80, 90),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2, 130),
            Vector2(WIDTH / 2 - 40, 130),
        ],
        [
            Vector2(WIDTH / 2 - 40, 50),
            Vector2(WIDTH / 2 + 40, 50),
            Vector2(WIDTH / 2 + 40, 170),
            Vector2(WIDTH / 2, 170),
            Vector2(WIDTH / 2, 90),
            Vector2(WIDTH / 2 - 40, 90),
        ],
        [
            Vector2(WIDTH / 2, 50),
            Vector2(WIDTH / 2 + 40, 50),
            Vector2(WIDTH / 2 + 40, 130),
            Vector2(WIDTH / 2 - 80, 130),
            Vector2(WIDTH / 2 - 80, 90),
            Vector2(WIDTH / 2, 90),
        ],
    ],  # L-Piece
]

game_over = False


class Pieces:
    def __init__(self):
        self.rotation = random.randint(0, 3)
        self.index = random.randint(0, 6)
        self.piece = pieces[self.index][self.rotation]
        self.color = colors[self.index]

        self.at_left = False
        self.at_right = False
        self.at_bottom = False

        self.disabled = False
        self.piece_added = False
        self.position = Vector2(0, 0)
        self.points_overlap = 0

    def move_pieces(self, keys_pressed, count):

        for i in range(len(self.piece)):
            if self.piece[i].x <= 0:
                self.at_left = True

            elif self.piece[i].x >= WIDTH:
                self.at_right = True

            if self.piece[i].y == HEIGHT:
                self.at_bottom = True
                self.disabled = True
            if self.piece[i].y == 50 and self.at_bottom == True:
                game_over = True

        if count % 6 == 0 and self.disabled == False:
            count = 0

            if keys_pressed[pygame.K_a] and self.at_left == False:
                for i in range(len(self.piece)):
                    self.piece[i] += Vector2(-40, 0)
                    self.position += Vector2(-40, 0)
                    self.at_left = False

            elif keys_pressed[pygame.K_d] and self.at_right == False:
                for i in range(len(self.piece)):
                    self.piece[i] += Vector2(40, 0)
                    self.position += Vector2(40, 0)
                    self.at_right = False

            # if keys_pressed[pygame.K_SPACE]:
            # if self.rotation < 3:
            # self.rotation += 1
            # else:
            # self.rotation = 0
            # self.piece = pieces[self.random][self.rotation]
            # for i in range(len(self.piece)):
            # self.piece[i] += self.position

        if self.at_bottom == False:
            self.at_right = False
            self.at_left = False

            for i in range(len(self.piece)):
                self.piece[i] += Vector2(0, 4)
                self.position += Vector2(0, 4)

    def draw_pieces(self):
        pygame.draw.polygon(window, self.color, self.piece)

    def add_piece(self):
        if self.at_bottom == True and self.piece_added == False:
            Shapes.append(Pieces())
            self.piece_added = True

    def piece_collisions(self):
        for i in range(len(self.piece)):
            for n in range(len(Shapes) - 1):
                for j in range(len(Shapes[n].piece) - 1):
                    if (
                        self.piece[i].y == Shapes[n].piece[j].y
                        and self.piece[i].x > Shapes[n].piece[j].x
                        and self.piece[i].x < Shapes[n].piece[j + 1].x
                    ):
                        self.disabled = True
                        self.at_bottom = True
                    if self.piece[i] == Shapes[n].piece[j]:
                        self.points_overlap += 1
                    if self.points_overlap >= 2:
                        self.at_bottom = True
                        self.disabled = True
                    self.points_overlap = 0


Shapes = [Pieces()]


def main():

    count = 0

    clock = pygame.time.Clock()

    run = True

    while run:

        count += 1

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        draw_grid()

        Shapes[-1].move_pieces(keys_pressed, count)
        Shapes[-1].piece_collisions()
        Shapes[-1].add_piece()

        for i in range(len(Shapes)):
            Shapes[i].draw_pieces()

        end_game()

        update_window()

    pygame.quit()


def end_game():
    if game_over == True:
        pygame.time.delay(5000)
        run = False


def update_window():
    pygame.display.flip()
    pygame.display.update()
    window.fill((0, 0, 0))


def draw_grid():
    for i in range(colums):
        pygame.draw.line(window, white, (i * 40, 50), (i * 40, HEIGHT))
    for i in range(rows):
        pygame.draw.line(window, white, (0, i * 40 + 50), (WIDTH, i * 40 + 50))


if __name__ == "__main__":
    main()
