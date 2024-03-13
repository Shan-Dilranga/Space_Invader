import pygame
import random
import math

# initialize pygame
pygame.init()

# Create display
surface = pygame.display.set_mode((800, 600))

# Title of the game
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


# create player
playerimg = pygame.image.load('player.png')
playerx = 380
playery = 370

playerxchange = 0
playerychange = 0

# creating enemy
# enemyimg = pygame.image.load('enemy.png')
# enemyx = random.randint(0, 800)
# enemyy = random.randint(50, 500)
#
# enemyxchange = 0.1
# enemyychange = 0

# creating multiple enemies
enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []

for i in range(10):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, 800))
    enemyy.append(random.randint(50, 500))
    enemyxchange.append(0.1)
    enemyychange.append(0)

# creating bullet
bulletimg = pygame.image.load('bullet.png')
bulletx = 380
bullety = 370
bulletxchange = 0
bulletychange = 0.3
bullet_state = "ready"


def player(x, y):
    surface.blit(playerimg, (x, y))


def enemy(x, y, i):
    surface.blit(enemyimg[i], (x, y))


def bullet(x, y):
    # global bullet_state
    # bullet_state = "fire"
    surface.blit(bulletimg, (x + 16, y + 10))


def iscollition(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if distance < 18:
        return True
    else:
        return False

# score board
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 0
texty = 10

def show_score(x,y):
    score = font.render("score : "+ str(score_value), True, (255,255, 255))
    surface.blit(score,(x,y))
def collition(i):
    global bullet_state
    global enemyx
    global enemyy
    global score_value
    bullet_state = "ready"
    enemyx[i] = random.randint(0, 800)
    enemyy[i] = random.randint(50, 500)
    score_value += 1



running = True
# Game Loop
while running:
    surface.fill((0, 0, 102))
    # surface colour must initialize before you create other aspects
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Setting to move spaceship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("pressed the left key")
                playerxchange = -0.1
            elif event.key == pygame.K_RIGHT:
                # print("pressed the right key")
                playerxchange = 0.1
            elif event.key == pygame.K_UP:
                playerychange = -0.1
            elif event.key == pygame.K_DOWN:
                playerychange = 0.1
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletx = playerx
                    bullety = playery
                    bullet_state = 'fire'
                    # bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerxchange = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerychange = 0

    playerx += playerxchange
    playery += playerychange

    # Setting up surface boundaries.
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    if playery <= 0:
        playery = 0
    elif playery >= 536:
        playery = 536

    # setting up enemy movements
    for i in range(4):
        enemyx[i] += enemyxchange[i]
        if enemyx[i] <= 0:
            enemyxchange[i] = 0.1
            enemyy[i] += random.randint(10, 20)
        elif enemyx[i] >= 736:
            enemyxchange[i] = -0.1
            enemyy[i] += random.randint(10, 20)

        if enemyy[i] >= 472:
            enemyy[i] = 472

        if iscollition(enemyx[i], enemyy[i], bulletx, bullety):
            collition(i)
        enemy(enemyx[i], enemyy[i], i)

    # setting up firing bullet
    if bullet_state == 'fire':
        bullet(bulletx, bullety)
        bullety -= bulletychange
    if bullety <= 0:
        bullet_state = "ready"

    player(playerx, playery)
    show_score(textx,texty)
    pygame.display.update()
