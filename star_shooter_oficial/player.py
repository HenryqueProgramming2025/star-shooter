import pygame
from bullets import Bullets

from config import SCREEN_WIDTH, SCREEN_HEIGHT, player_speed, player_hp, player_size, GREEN, RED, WHITE, BLUE, BLACK
from config import bullets_size

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2 - player_size // 2
        self.y = SCREEN_HEIGHT - 80
        self.size = player_size
        self.speed = player_speed
        self.hp = player_hp
        self.color = GREEN
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.bullets = []

    def moving(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

        if self.x < 0:
            self.x = 0
        if self.x > SCREEN_WIDTH - self.size:
            self.x = SCREEN_WIDTH - self.size
        if self.y < 0:
            self.y = 0
        if self.y > SCREEN_HEIGHT - self.size:
            self.y = SCREEN_HEIGHT - self.size

        self.rect.topleft = (self.x, self.y)

    def shooting(self):
        bullet_x = self.x + self.size // 2 - bullets_size[0] // 2
        bullet_y = self.y

        self.bullets.append(Bullets(bullet_x, bullet_y))

    def drawing(self, screen):
        for bullet in self.bullets:
            bullet.moving()
            bullet.draw(screen)
            if bullet.off_screen():
                self.bullets.remove(bullet)

        body = [
            (self.x + 40, self.y),
            (self.x + 10, self.y + 70),
            (self.x + 70, self.y + 70)
        ]

        mini_triangle = [
            (self.x + 40, self.y),
            (self.x + 30, self.y + 20),
            (self.x + 50, self.y + 20)
        ]

        l_wing = [
            (self.x + 18, self.y + 50),
            (self.x + 5, self.y + 78),
            (self.x + 20, self.y + 70)
        ]

        r_wing = [
            (self.x + 62, self.y + 50),
            (self.x + 75, self.y + 78),
            (self.x + 60, self.y + 70)
        ]

        cockpit = (self.x + 40, self.y + 40)

        fire = (self.x + 30, self.y + 85)
        fire2 = (self.x + 50, self.y + 85)

        pygame.draw.polygon(screen, WHITE, body)
        pygame.draw.polygon(screen, RED, mini_triangle)
        pygame.draw.polygon(screen, RED, l_wing)
        pygame.draw.polygon(screen, RED, r_wing)
        pygame.draw.circle(screen, BLACK, cockpit, 10)
        pygame.draw.circle(screen, BLUE, cockpit, 8)
        pygame.draw.circle(screen, (255, 100, 0), fire, 8)
        pygame.draw.circle(screen, (255, 200, 0), fire, 4)
        pygame.draw.circle(screen, (255, 100, 0), fire2, 8)
        pygame.draw.circle(screen, (255, 200, 0), fire2, 4)




