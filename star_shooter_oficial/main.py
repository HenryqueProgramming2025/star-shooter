import pygame
import sys
import random
import os
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE
from player import Player
from enemies import Enemy, enemies_size, EnemyBullet, DarthVader, Bacta

pygame.init()
pygame.mixer.init()

def load_sound(path):
    try:
        sound = pygame.mixer.Sound(path)
        print(f"SUCCESS: {path}")
        return sound
    except:
        print(f"ERROR: {path}")
        return None

laser_sound = load_sound("sounds/laser.wav")
vader_appear_sound = load_sound("sounds/vader_appear.wav")
vader_hit_sound = load_sound("sounds/vader_hit.wav")
vader_defeat_sound = load_sound("sounds/vader_defeat.wav")
victory_sound = load_sound("sounds/victory.wav")
bacta_sound = load_sound("sounds/bacta.wav")

try:
    pygame.mixer.music.load("sounds/menu_music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    print("SUCCESS: menu music")
except:
    print("menu_music.mp3 not found")

print("Directory:", os.getcwd())
print("Files:", os.listdir())

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Star Shooter Official - The Valter Dizney Studios (2026)")
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont("Arial", 36)

def load_image(filename, size):
    try:
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, size)
        print(f"SUCCESS: {filename}")
        return img
    except:
        print(f"ERROR: {filename}")
        return None

menu_background = load_image("sprites/swmenu.jpg", (SCREEN_WIDTH, SCREEN_HEIGHT))
game_background = load_image("sprites/gameback.jpg", (SCREEN_WIDTH, SCREEN_HEIGHT))

def main_menu():
    options = ["START", "DIFFICULTIES", "QUIT"]
    difficulties = ["EASY", "MEDIUM", "HARD"]
    idx_option = 0
    idx_difficulty = 1

    while True:
        if menu_background:
            SCREEN.blit(menu_background, (0, 0))
        else:
            SCREEN.fill((0, 0, 0))

        title = font.render("STAR SHOOTER OFFICIAL (2026)", True, (255, 255, 0))
        SCREEN.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        for i, op in enumerate(options):
            color = (255, 255, 255) if i == idx_option else (100, 100, 100)
            txt = font.render(op, True, color)
            SCREEN.blit(txt, (SCREEN_WIDTH // 2 - txt.get_width() // 2, SCREEN_HEIGHT // 2 - 20 + i * 60))

        dif_txt = font.render(f"Difficulty: {difficulties[idx_difficulty]}", True, (200, 200, 200))
        SCREEN.blit(dif_txt, (SCREEN_WIDTH // 2 - dif_txt.get_width() // 2, SCREEN_HEIGHT // 2 + 180))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    idx_option = (idx_option - 1) % len(options)
                if event.key == pygame.K_DOWN:
                    idx_option = (idx_option + 1) % len(options)
                if event.key == pygame.K_RETURN:
                    if options[idx_option] == "START":
                        return difficulties[idx_difficulty]
                    elif options[idx_option] == "DIFFICULTIES":
                        idx_difficulty = (idx_difficulty + 1) % 3
                    elif options[idx_option] == "QUIT":
                        pygame.quit()
                        sys.exit()

def pause_menu():
    options = ["CONTINUE", "RETURN TO MENU", "QUIT"]
    idx = 0
    while True:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        SCREEN.blit(overlay, (0, 0))
        for i, op in enumerate(options):
            color = (255, 255, 255) if i == idx else (100, 100, 100)
            txt = font.render(op, True, color)
            SCREEN.blit(txt, (SCREEN_WIDTH // 2 - txt.get_width() // 2, SCREEN_HEIGHT // 2 - 30 + i * 60))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    idx = (idx - 1) % 3
                if event.key == pygame.K_DOWN:
                    idx = (idx + 1) % 3
                if event.key == pygame.K_RETURN:
                    if options[idx] == "CONTINUE":
                        return "continue"
                    elif options[idx] == "RETURN TO MENU":
                        return "menu"
                    elif options[idx] == "QUIT":
                        pygame.quit()
                        sys.exit()

def game_over_screen(score):
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    if os.path.exists("sounds/gameover.mp3"):
        pygame.mixer.music.load("sounds/gameover.mp3")
        pygame.mixer.music.play(-1)
    else:
        print("gameover.mp3 not found")
    waiting = True
    while waiting:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_r:
                    waiting = False
                if ev.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        SCREEN.fill(BLACK)
        go_text = font.render("GAME OVER!", True, (255, 0, 0))
        SCREEN.blit(go_text, (SCREEN_WIDTH // 2 - go_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        score_text = font.render(f"FINAL SCORE: {score}", True, WHITE)
        SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        restart_text = font.render("Press R to restart", True, WHITE)
        SCREEN.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()
        clock.tick(FPS)

def win_screen(score):
    pygame.mixer.music.stop()
    if victory_sound:
        victory_sound.play()
    waiting = True
    while waiting:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_r or ev.key == pygame.K_RETURN:
                    waiting = False
                if ev.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        SCREEN.fill(BLACK)
        win_text = font.render("VICTORY! YOU DEFEATED DARTH VADER", True, (0, 255, 0))
        SCREEN.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        score_text = font.render(f"FINAL SCORE: {score}", True, WHITE)
        SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        restart_text = font.render("Press R to return to menu", True, WHITE)
        SCREEN.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()
        clock.tick(FPS)

def run_game(difficulty):
    if difficulty == "EASY":
        enemy_speed = 2
    elif difficulty == "MEDIUM":
        enemy_speed = 4
    else:
        enemy_speed = 6

    player = Player()
    enemies = []
    enemy_bullets = []
    bacta_items = []
    vader = None
    vader_defeated = False
    spawn_timer = 0
    score = 0
    start_ticks = pygame.time.get_ticks()

    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load("sounds/game_music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        print("SUCCESS: game music")
    except:
        print("game_music.mp3 not found")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shooting()
                    if laser_sound:
                        laser_sound.play()
                if event.key == pygame.K_ESCAPE:
                    action = pause_menu()
                    if action == "menu":
                        pygame.mixer.music.load("sounds/menu_music.mp3")
                        pygame.mixer.music.play(-1)
                        return
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.moving(keys)

        if vader is None and score < 200:
            spawn_timer += 1
            if spawn_timer > 35:
                spawn_timer = 0
                if random.randint(1, 3) == 1:
                    enemy_x = random.randint(0, SCREEN_WIDTH - enemies_size)
                    enemies.append(Enemy(enemy_x, -enemies_size, enemy_speed))
        elif vader is None and score >= 200 and not vader_defeated:
            from config import vader_size
            vader = DarthVader(SCREEN_WIDTH // 2 - vader_size // 2, -vader_size)
            enemies.clear()
            print("Darth Vader appears! Shoot him 5 times!")
            pygame.mixer.music.stop()
            if vader_appear_sound:
                vader_appear_sound.play()

        for bullet in player.bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    if bullet in player.bullets:
                        player.bullets.remove(bullet)
                    if enemy in enemies:
                        enemies.remove(enemy)
                    score += 10
                    if random.random() < 0.2:
                        bacta_items.append(Bacta(enemy.x + enemy.size // 2, enemy.y + enemy.size // 2))
                    break

        for enemy in enemies[:]:
            if player.rect.colliderect(enemy.rect):
                player.hp -= 1
                enemies.remove(enemy)
                print(f"Player HP: {player.hp}")
                if player.hp <= 0:
                    game_over_screen(score)
                    pygame.mixer.music.load("sounds/menu_music.mp3")
                    pygame.mixer.music.play(-1)
                    return
                break

        for enemy in enemies[:]:
            if enemy.update():
                bullet_x = enemy.x + enemy.size // 2 - 3
                bullet_y = enemy.y + enemy.size
                enemy_bullets.append(EnemyBullet(bullet_x, bullet_y))
            if enemy.is_off():
                enemies.remove(enemy)

        if vader is not None:
            if vader.update():
                bullet_x = vader.x + vader.size // 2 - 3
                bullet_y = vader.y + vader.size
                enemy_bullets.append(EnemyBullet(bullet_x, bullet_y))
            if vader.is_off():
                vader = None

            for bullet in player.bullets[:]:
                if bullet.rect.colliderect(vader.rect):
                    player.bullets.remove(bullet)
                    if vader_hit_sound:
                        vader_hit_sound.play()
                    if vader.hit():
                        score += 200
                        if vader_defeat_sound:
                            vader_defeat_sound.play()
                        win_screen(score)
                        pygame.mixer.music.load("sounds/menu_music.mp3")
                        pygame.mixer.music.play(-1)
                        return
                    else:
                        print(f"Vader HP: {vader.hp}")
                    break

        for bullet in enemy_bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                enemy_bullets.remove(bullet)

        for item in bacta_items[:]:
            item.update()
            if item.is_off():
                bacta_items.remove(item)

        for item in bacta_items[:]:
            if player.rect.colliderect(item.rect):
                player.hp += 1
                print(f"Bacta! HP now: {player.hp}")
                if bacta_sound:
                    bacta_sound.play()
                bacta_items.remove(item)

        for bullet in enemy_bullets[:]:
            if player.rect.colliderect(bullet.rect):
                player.hp -= 1
                enemy_bullets.remove(bullet)
                print(f"Player HP: {player.hp}")
                if player.hp <= 0:
                    game_over_screen(score)
                    pygame.mixer.music.load("sounds/menu_music.mp3")
                    pygame.mixer.music.play(-1)
                    return
                break

        if game_background:
            SCREEN.blit(game_background, (0, 0))
        else:
            SCREEN.fill(BLACK)

        for bullet in enemy_bullets:
            bullet.draw(SCREEN)

        for item in bacta_items:
            item.draw(SCREEN)

        elapsed = (pygame.time.get_ticks() - start_ticks) // 1000
        minutes = elapsed // 60
        seconds = elapsed % 60
        timer_surface = font.render(f"TIME: {minutes:02}:{seconds:02}", True, WHITE)
        SCREEN.blit(timer_surface, (SCREEN_WIDTH - 200, 10))

        score_text = font.render(f"Score: {score}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))

        hp_text = font.render(f"HP: {player.hp}", True, WHITE)
        SCREEN.blit(hp_text, (10, 50))

        bar_width = int((player.hp / 3) * 200)
        bar_width = max(0, bar_width)
        pygame.draw.rect(SCREEN, (0, 255, 0), (10, 90, bar_width, 20))
        pygame.draw.rect(SCREEN, (255, 0, 0), (10, 90, 200, 20), 2)

        player.drawing(SCREEN)

        for enemy in enemies:
            enemy.draw(SCREEN)

        if vader is not None:
            vader.draw(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

while True:
    difficulty = main_menu()
    run_game(difficulty)