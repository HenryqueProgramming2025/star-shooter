import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
LIGHT_BLUE = (173, 255, 230)

game_difficulties = {
    "Fácil": 2,
    "Médio": 4,
    "Difícil": 6
}

player_speed = 5
player_size = 80
player_hp = 3

bullets_speed = -8
bullets_size = (6, 10)

enemies_size = 50
enemies_bullet_speed = 5

vader_size = 70
vader_speed_y = 1
vader_speed_x = 3
vader_hp = 5

bacta_size = 15
bacta_speed = 3
bacta_color = (0, 255, 0)