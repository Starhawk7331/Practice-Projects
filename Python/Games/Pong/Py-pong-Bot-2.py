import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong by Daniel Kaiser und Benedikt Werner")


def randpos():
    if random.randint(0, 1) == 0:
        return -1
    else:
        return 1


font = pygame.font.SysFont("comicsans", 40)

FPS = 60
white = (255, 255, 255)

paddle_A_cord = [30, 250, 20, 100]
paddle_B_cord = [750, 250, 20, 100]

speed_mult = 0
ball_cord = [WIDTH / 2, HEIGHT / 2]
ball_speed = [-5 , 5 * randpos()]

move_to = 0

score_A = 0
score_B = 0


def resetball():
    global ball_cord,ball_speed,speed_mult
    speed_mult = 0
    ball_cord = [WIDTH / 2, HEIGHT / 2]
    ball_speed = [-5 ,5 * randpos()]


resetball()


def draw_window():
    window.fill((0, 0, 0))
    pygame.draw.rect(window, white, (paddle_A_cord))
    pygame.draw.rect(window, white, (paddle_B_cord))
    pygame.draw.circle(window, white, (ball_cord), 10)

    window.blit(font.render("A: " + str(score_A), 1, white), (10, 10))
    window.blit(font.render("B: " + str(score_B), 1, white), (10, 50))

    pygame.display.flip()
    pygame.display.update()


def main():

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        A_movement(keys_pressed)
        B_movement()
        ball_movement()

        draw_window()

    pygame.quit()


def A_movement(keys_pressed):
    if keys_pressed[pygame.K_w] and not paddle_A_cord[1] <= 0:
        paddle_A_cord[1] -= 10

    if keys_pressed[pygame.K_s] and not paddle_A_cord[1] >= HEIGHT - 100:
        paddle_A_cord[1] += 10


def B_movement():
    global move_to

    if move_to < paddle_B_cord[1] + 50 and not paddle_B_cord[1] <= 0:
        direct = -1
    elif move_to > paddle_B_cord[1] + 50 and not paddle_B_cord[1] >= HEIGHT - 100:
        direct = 1
    else:
        direct = 0

    paddle_B_cord[1] += 10 * direct



def ball_movement():
    global score_A
    global score_B
    paddle_A = pygame.draw.rect(window, white, (paddle_A_cord))
    paddle_B = pygame.draw.rect(window, white, (paddle_B_cord))
    ball = pygame.draw.circle(window, white, (ball_cord), 10)

    if ball_cord[0] < 0:
        resetball()
        score_B += 1
    elif ball_cord[0] > WIDTH:
        score_A += 1
        resetball()

    if ball_cord[1] < 0 or ball_cord[1] > HEIGHT:
        ball_speed[1] = -1 * ball_speed[1]

    if ball.colliderect(paddle_A):
        global speed_mult

        speed_mult += 1
        ball_speed[0] = -1 * ball_speed[0] + speed_mult
        ball_speed[1] += speed_mult

        find_move_to()
        

    if ball.colliderect(paddle_B):
        ball_speed[0] = -1 * ball_speed[0]
        

    ball_cord[0] = ball_speed[0] + ball_cord[0]
    ball_cord[1] = ball_speed[1] + ball_cord[1]

def find_move_to():
    global move_to
    fake_ball_cord = ball_cord
    while ball_cord[0] < paddle_B_cord[1]:
        if ball_cord[1] < 0 or ball_cord[1] > HEIGHT:
            ball_speed[1] = -1 * ball_speed[1]
        fake_ball_cord[0] += ball_speed[0]
        fake_ball_cord[1] += ball_speed[1]
        
        move_to = ball_cord[1]

if __name__ == "__main__":
    main()
