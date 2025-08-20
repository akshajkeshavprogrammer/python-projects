import random
import os
import time

# Screen dimensions
WIDTH, HEIGHT = 80, 20

# Player settings
player_x = WIDTH // 2
player_y = HEIGHT - 2
player_lives = 3

# Bullet and Enemy settings
bullets = []
enemies = []
enemy_spawn_rate = 10
enemy_speed = 1
score = 0

# Game loop
def draw_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Draw player
    screen[player_y][player_x] = 'A'

    # Draw bullets
    for bullet in bullets:
        screen[bullet[1]][bullet[0]] = '|'

    # Draw enemies
    for enemy in enemies:
        screen[enemy[1]][enemy[0]] = 'V'

    # Display screen
    for row in screen:
        print(''.join(row))
    print(f"Score: {score}  Lives: {player_lives}")

def move_player(direction):
    global player_x
    if direction == 'left' and player_x > 0:
        player_x -= 1
    elif direction == 'right' and player_x < WIDTH - 1:
        player_x += 1

def shoot():
    bullets.append([player_x, player_y - 1])

def update_bullets():
    global score
    for bullet in bullets[:]:
        bullet[1] -= 1
        if bullet[1] < 0:
            bullets.remove(bullet)
        else:
            for enemy in enemies[:]:
                if bullet[0] == enemy[0] and bullet[1] == enemy[1]:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

def spawn_enemy():
    if random.randint(1, enemy_spawn_rate) == 1:
        enemies.append([random.randint(0, WIDTH - 1), 0])

def update_enemies():
    global player_lives
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] >= HEIGHT:
            enemies.remove(enemy)
            player_lives -= 1
        elif enemy[0] == player_x and enemy[1] == player_y:
            enemies.remove(enemy)
            player_lives -= 1

def game_over():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Game Over! Your score: {score}")
    exit()

def main():
    global player_lives
    while player_lives > 0:
        draw_screen()
        update_bullets()
        update_enemies()
        spawn_enemy()

        # Simulate key presses
        if random.choice([True, False]):
            move_player('left')
        else:
            move_player('right')
        
        if random.choice([True, False]):
            shoot()

        time.sleep(0.1)

    game_over()

if __name__ == "__main__":
    main()
