import pygame
from pygame.math import Vector2

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

font = pygame.font.SysFont("comicsans", 40)

FPS = 60
white = (255, 255, 255)

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


def main():

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        draw_window()

    pygame.quit()


def draw_window():

    pygame.draw.polygon(window, white, pieces[6][3])

    pygame.display.flip()
    pygame.display.update()
    window.fill((0, 0, 0))


if __name__ == "__main__":
    main()
