import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

font = pygame.font.SysFont("comicsans", 40)

FPS = 60
white = (255, 255, 255)


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

    pygame.draw.rect(window, white, ())

    pygame.display.flip()
    pygame.display.update()
    window.fill((0, 0, 0))


if __name__ == "__main__":
    main()
