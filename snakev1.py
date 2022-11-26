import pygame
import sys
import allcolors as al
import random

pygame.init()

# параметры экрана
screen_width = 900
screen_height = 800

# создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ьъьъьъьъььъьъььъьъьъъьъ')
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

# шрифты
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)


# функция удлинения змейки
def big_snake(snake_block1, snake_block2, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, al.black, [x[0], x[1], snake_block1, snake_block2])


# вывод результата
def Your_score(score):
    value = score_font.render("Счёт: " + str(score), True, al.yellow)
    screen.blit(value, [0, 0])


# рекорд
def high_score(rec):
    vl = score_font.render("Рекорд: " + str(rec), True, al.yellow)
    screen.blit(vl, [700, 0])


# функция для вывода сообщения о проигрыше
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [40, 350])


# вывод жизней
def snake_lives(lives):
    snlv = score_font.render("Жизни:" + str(lives), True, al.yellow)
    screen.blit(snlv, [400, 0])


# основной цикл всех процессов
def all_game():
    snake_block1 = 13
    snake_block2 = 13

    # изменённые координаты
    x1_change = 0
    y1_change = 0

    # кол-во жизней
    lives = 3

    # скорость змейки
    snake_speed = 17

    # словарь противоположного движения
    dirs = {"W": True, "S": True, "A": True, "D": True}

    # вывод рекорда
    rec = 0
    with open('high_record.txt', 'r') as f:
        rec = int(f.readline())

    # спавн еды
    foodx = round(random.randrange(0, screen_width) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_width) / 10.0) * 10.0

    # основные координаты
    x1 = screen_width / 2
    y1 = screen_height / 2

    # параметры выхода
    game_over = False
    game_close = False

    # длина змейки
    snake_List = []
    Length_of_snake = 1

    # все процессы
    while not game_over:

        while game_close == True:
            screen.fill(al.blue)
            message("Проигрыш! Нажми C-Играть снова или Q-Выход", al.red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        all_game()

        for event in pygame.event.get():
            """контроль кнопками"""
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and dirs["A"]:
                    x1_change = -10
                    y1_change = 0
                    dirs = {"W": True, "S": True, "A": True, "D": False}
                elif event.key == pygame.K_d and dirs["D"]:
                    x1_change = 10
                    y1_change = 0
                    dirs = {"W": True, "S": True, "A": False, "D": True}
                elif event.key == pygame.K_w and dirs["W"]:
                    y1_change = -10
                    x1_change = 0
                    dirs = {"W": True, "S": False, "A": True, "D": True}
                elif event.key == pygame.K_s and dirs["S"]:
                    y1_change = 10
                    x1_change = 0
                    dirs = {"W": False, "S": True, "A": True, "D": True}
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

        # уничтожение об границы
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            lives = lives - 1
            x1 = screen_width / 2
            y1 = screen_height / 2
            if lives == 0:
                game_close = True

        # добавление длинны змейкм
        x1 += x1_change
        y1 += y1_change
        screen.fill(al.blue)

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # соприкосновение с хвостом
        for x in snake_List[:-1]:
            if x == snake_Head:
                lives = lives - 1
                x1 = screen_width / 2
                y1 = screen_height / 2
                if lives == 0:
                    game_close = True

        # отрисовка еды и змейки
        # 1. Змейка
        pygame.draw.rect(screen, al.green, (x1, y1, snake_block1, snake_block2))
        # 2. Еда
        pygame.draw.rect(screen, al.ruby, [foodx, foody, 15, 15])

        # счёт
        Your_score(Length_of_snake - 1)

        # жизни
        snake_lives(lives)

        # рекорд
        high_score(rec - 1)

        big_snake(snake_block1, snake_block2, snake_List)

        # Соприкосновение еды и змейки
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block1) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block2) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed += 1

        # записывание в файл рекорда
        if Length_of_snake > rec:
            rec = Length_of_snake
            with open('high_record.txt', 'w') as f:
                f.write(str(rec))

        # обновление экрана
        pygame.display.flip()
        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()


all_game()
