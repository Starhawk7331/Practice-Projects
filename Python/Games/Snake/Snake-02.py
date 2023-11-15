import pygame, random
from pygame.math import Vector2

pygame.init()

pygame.display.set_caption("Snake by Daniel Kaiser")

font = pygame.font.SysFont("comicsans", 40)

cell_size = 30
cell_number = 30

FPS = 10
white = (255, 255, 255)
red = (255, 40, 0)
black = (0, 0, 0)

placeholder = 0

button_queue = []

window = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))


class FRUIT:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.pos = Vector2(self.x, self.y)
        global fruit_location
        fruit_location = self.pos

    def change_location(self):
        self.y = random.randint(0, 29) * 30
        self.x = random.randint(0, 29) * 30
        self.pos = Vector2(self.x, self.y)
        global fruit_location
        fruit_location = self.pos

    def draw_fruit(self):
        global window
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_number)
        pygame.draw.rect(window, red, fruit_rect)


class snake:
    def __init__(self):
        self.body = [Vector2(60, 0), Vector2(30, 0), Vector2(0, 0)]
        self.direction = Vector2(30, 0)
        self.new_block = False

    def draw_snake(self):
        for i in range(len(self.body)):
            x = self.body[i].x
            y = self.body[i].y
            pygame.draw.rect(window, black, pygame.Rect(x, y, cell_size, cell_number))

    def move(self, key_pressed):
        if key_pressed[pygame.K_w]:
            self.direction = Vector2(0, -30)
        elif key_pressed[pygame.K_s]:
            self.direction = Vector2(0, 30)
        elif key_pressed[pygame.K_a]:
            self.direction = Vector2(-30, 0)
        elif key_pressed[pygame.K_d]:
            self.direction = Vector2(30, 0)

        if self.new_block == True:
            body_copy = self.body
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def collision(self, apple):
        global fruit_location
        if self.body[0] == fruit_location:
            self.add_block()
            apple.change_location()

        if (
            self.body[0].x < 0
            or self.body[0].x > cell_number * cell_size
            or self.body[0].y < 0
            or self.body[0].y > cell_number * cell_size
        ):
            end_game(self.body)

        for i in range(len(self.body) - 1):
            if self.body[0] == self.body[i + 1]:
                end_game(self.body)

    def add_block(self):
        self.new_block = True


def end_game(body):
    global run
    score = len(body) - 3
    with open("C:\SEW\Python\Games\Snake\Snake_Highscore.txt", "r") as f:
        highscore = int(f.readline())
    if score > highscore:
        highscore = score
        with open("C:\SEW\Python\Games\Snake\Snake_Highscore.txt", "w") as f:
            f.write(str(highscore))

    end_text = "Game Over.Points: " + str(score)
    high_score = "Highscore:" + str(highscore)
    game_over = font.render(end_text, 1, red)
    highscore_text = font.render(high_score, 1, red)
    window.blit(
        game_over, ((cell_size * cell_number) / 2, (cell_size * cell_number) / 2)
    )
    window.blit(
        highscore_text,
        ((cell_size * cell_number) / 2, (cell_size * cell_number) / 2 - 50),
    )

    pygame.display.update()
    pygame.time.delay(3000)
    run = False


def main():
    global run
    clock = pygame.time.Clock()

    apple = FRUIT()
    apple.change_location()
    Snake = snake()

    run = True

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

        key_pressed = pygame.key.get_pressed()
        button_queue.append(key_pressed)

        window.fill((175, 215, 70))

        apple.draw_fruit()
        Snake.move(button_queue[0])
        button_queue.pop(0)
        Snake.draw_snake()
        Snake.collision(apple)

        draw_display()
        pygame.display.set_caption(
            "Snake by Daniel Kaiser - Score: " + str(len(Snake.body) - 3)
        )

    pygame.quit()


def draw_display():
    pygame.display.flip()
    pygame.display.update()


if __name__ == "__main__":
    main()
