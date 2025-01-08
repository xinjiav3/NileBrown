import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def display_message(msg, color, x, y):
    message = font.render(msg, True, color)
    screen.blit(message, [x, y])

def game_loop():
    snake_pos = [[100, 50], [90, 50], [80, 50]]
    direction = "RIGHT"
    change_to = direction

    food_pos = [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
                random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE]
    food_spawn = True

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        direction = change_to

        if direction == "UP":
            snake_pos[0][1] -= CELL_SIZE
        if direction == "DOWN":
            snake_pos[0][1] += CELL_SIZE
        if direction == "LEFT":
            snake_pos[0][0] -= CELL_SIZE
        if direction == "RIGHT":
            snake_pos[0][0] += CELL_SIZE

        if snake_pos[0] == food_pos:
            score += 1
            food_spawn = False
        else:
            snake_pos.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
                        random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE]
        food_spawn = True

        snake_pos.insert(0, list(snake_pos[0]))

        if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT):
            break

        for block in snake_pos[1:]:
            if snake_pos[0] == block:
                break

        screen.fill(BLACK)
        for pos in snake_pos:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

        display_message(f"Score: {score}", WHITE, 10, 10)
        pygame.display.flip()

        clock.tick(15)

    time.sleep(1)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
