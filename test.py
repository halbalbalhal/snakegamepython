import pygame
import allcolors as al
import sys

pygame.init()

screen_width = 800
screen_height = 700

Length_of_snake = 1
rec = 1

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ьъьъьъьъььъьъььъьъьъъьъ')

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)

game_over = False


def Your_score(score):
    value = score_font.render("Score: " + str(score), True, al.yellow)
    screen.blit(value, [0, 0])


def high_score(score2):
    vl = score_font.render(" " + str(score2), True, al.yellow)
    screen.blit(vl, [500, 0])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                Length_of_snake += 1

    Your_score(Length_of_snake - 1)
    high_score(rec - 1)

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
quit()
