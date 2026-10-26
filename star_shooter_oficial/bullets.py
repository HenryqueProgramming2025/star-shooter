import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, bullets_size, bullets_speed, YELLOW

class Bullets:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = bullets_size[0]
        self.height = bullets_size[1]
        self.speed = bullets_speed
        self.color = YELLOW
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def moving(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.y < 0 or self.y > SCREEN_HEIGHT
