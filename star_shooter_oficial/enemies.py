import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, enemies_size, enemies_bullet_speed, GRAY, RED, vader_size, vader_speed_x, vader_speed_y, vader_hp
from config import bacta_size, bacta_speed, bacta_color

class DarthVader:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = vader_size
        self.speed_x = vader_speed_x
        self.speed_y = vader_speed_y
        self.hp = vader_hp
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.shoot_timer = 0
        self.direction = 1

        try:
            self.image = pygame.image.load("sprites/vader.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        except pygame.error:
            self.image = None

    def update(self):
        self.x += self.speed_x * self.direction

        if self.x <= 0:
            self.x = 0
            self.direction = 1
        elif self.x >= SCREEN_WIDTH - self.size:
            self.x = SCREEN_WIDTH - self.size
            self.direction = -1

        self.y += self.speed_y
        self.rect.topleft = (self.x, self.y)

        self.shoot_timer += 1
        if self.shoot_timer > 60:
            self.shoot_timer = 0
            return True
        return False

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (50, 50, 50), self.rect)

    def is_off(self):
        return self.y > SCREEN_HEIGHT

    def hit(self):
        self.hp -= 1
        return self.hp <= 0

class EnemyBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 6
        self.height = 10
        self.speed = 8
        self.color = RED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), 5)

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.size = enemies_size
        self.speed = speed
        self.color = GRAY
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.shoot_timer = 0

        try:
            self.image = pygame.image.load("sprites/stormtrooper.jpg").convert_alpha()
            self.image.set_colorkey((255, 255, 255))
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        except pygame.error:
            self.image = None

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

        self.shoot_timer += 1
        if self.shoot_timer > 60:
            self.shoot_timer = 0
            return True
        return False

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def is_off(self):
        return self.y > SCREEN_HEIGHT

class Bacta:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = bacta_size
        self.speed = bacta_speed
        self.color = bacta_color
        self.rect = pygame.Rect(self.x, self.y,  self.size, self.size)

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def is_off(self):
        return self.y > SCREEN_HEIGHT

