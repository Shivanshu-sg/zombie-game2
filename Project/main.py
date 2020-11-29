import pygame
import random
import math
from pygame import mixer

#modules initialsed
pygame.init()

#screen height and width and caption
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Zombie shooter by Shivanshu Gupta')

#Icon
icon = pygame.image.load('sprites/logo.png')
pygame.display.set_icon(icon)

#Background
background = pygame.image.load('sprites/background.png')

#Background soumd
mixer.music.load('sound/Creepy-Action.mp3')
mixer.music.play(-1)

#Player
playerimg = pygame.image.load('sprites/player.png')
playerX = 370
playerY = 480
playerX_change = 0


#Enemy
enemyimg = pygame.image.load('sprites/enemy.png')
enemyX = random.randint(50,750)
enemyY = random.randint(50,200)
enemyX_change = 0.3
enemyY_change = 20

#Enemy 2 
enemy2img = pygame.image.load('sprites/enemy 2.png')
enemy2X = random.randint(50,750)
enemy2Y = random.randint(50,200)
enemy2X_change = 0.5
enemy2Y_change = 25

#Enemy 3
enemy3img = pygame.image.load('sprites/enemy3.png')
enemy3X = random.randint(50,750)
enemy3Y = random.randint(50,200)
enemy3X_change = 0.4
enemy3Y_change = 30

#Enemy 4
enemy4img = pygame.image.load('sprites/enemy4.png')
enemy4X = random.randint(50,750)
enemy4Y = random.randint(50,200)
enemy4X_change = 0.3
enemy4Y_change = 20

#Enemy 5
enemy5img = pygame.image.load('sprites/enemy5.png')
enemy5X = random.randint(50,750)
enemy5Y = random.randint(50,200)
enemy5X_change = 0.3
enemy5Y_change = 20



#Bullet
bulletimg = pygame.image.load('sprites/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state ='ready' # Ready - you cant see bullet on screen
                     # fire - the bullet is currently moving
#Score
score_value = 0
font = pygame.font.SysFont("comicsansms", 32)
textX = 10
textY = 10 

#Game Over
font1 = pygame.font.SysFont("comicsansms", 65)
text1X = 200
test1Y = 150

def game_over():
    game = font1.render('GAME OVER',True,(0,0,0))
    screen.blit(game, (text1X,test1Y))

def show_score(x,y):
    score = font.render('Score : ' + str(score_value),True,(255,0,0))
    screen.blit(score, (x,y))

def player(X,Y):
    screen.blit(playerimg, (X,Y))

def enemy(A,B):
    screen.blit(enemyimg,(A,B))

def enemy2(x,y):
    screen.blit(enemy2img, (enemy2X,enemy2Y))

def enemy3(x,y):
    screen.blit(enemy3img, (enemy3X,enemy3Y))

def enemy4(x,y):
    screen.blit(enemy4img, (enemy4X,enemy4Y))

def enemy5(x,y):
    screen.blit(enemy5img, (enemy5X,enemy5Y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg,(x + 6, y ))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2) + math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        False

def iscollision2(enemy2X,enemy2Y,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemy2X - bulletX,2) + math.pow(enemy2Y - bulletY,2)))
    if distance < 27:
        return True
    else:
        False

def iscollision3(enemy3X,enemy3Y,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemy3X - bulletX,2) + math.pow(enemy3Y - bulletY,2)))
    if distance < 27:
        return True
    else:
        False

def iscollision4(enemy4X,enemy4Y,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemy4X - bulletX,2) + math.pow(enemy4Y - bulletY,2)))
    if distance < 27:
        return True
    else:
        False

def iscollision5(enemy5X,enemy5Y,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemy5X - bulletX,2) + math.pow(enemy5Y - bulletY,2)))
    if distance < 27:
        return True
    else:
        False

#Gaame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False

        #Movement of player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':  
                    bullet_sound = pygame.mixer.Sound('sound/laser.wav')
                    pygame.mixer.Sound.play(bullet_sound )
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or  event.key == pygame.K_LEFT:
                playerX_change = 0
            


                

    score = 0
    #Screen color
    screen.fill((0,128,0))

    #showing background
    screen.blit(background,(0,0))

    #setting of boundaries for player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >750:
        playerX =750
    
    
    #Movement of enemy
    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    if enemyX >= 770:
        enemyX_change = -1
        enemyY += enemyY_change
    enemyX += enemyX_change
    if enemyY >=400:
        game_over()
        playerX_change = 0
        enemy2X_change = 0
        enemy3X_change = 0
        enemy4X_change = 0
        enemy5X_change = 0
        enemyX_change = 0
        bulletY_change = 0
        over_sound = pygame.mixer.Sound('sound/game over.wav')
        pygame.mixer.Sound.play(over_sound )
        
    #Movement of enemy 2 
    if enemy2X <= 0:
        enemy2X_change = 0.8
        enemy2Y += enemy2Y_change
    if enemy2X >= 770:
        enemy2X_change = -0.8
        enemy2Y += enemy2Y_change
    enemy2X += enemy2X_change
    if enemy2Y >=400:
        game_over()
        playerX_change = 0
        enemy2X_change = 0
        enemy3X_change = 0
        enemy4X_change = 0
        enemy5X_change = 0
        enemyX_change = 0
        bulletY_change = 0
        over_sound = pygame.mixer.Sound('sound/game over.wav')
        pygame.mixer.Sound.play(over_sound )

     #Movement of enemy 3
    if enemy3X <= 0:
        enemy3X_change = 0.9
        enemy3Y += enemy3Y_change
    if enemy3X >= 770:
        enemy3X_change = -0.9
        enemy3Y += enemy3Y_change
    enemy3X += enemy3X_change
    if enemy3Y >=400:
        game_over()
        playerX_change = 0
        enemy2X_change = 0
        enemy3X_change = 0
        enemy4X_change = 0
        enemy5X_change = 0
        enemyX_change = 0
        bulletY_change = 0
        over_sound = pygame.mixer.Sound('sound/game over.wav')
        pygame.mixer.Sound.play(over_sound )

     #Movement of enemy 4
    if enemy4X <= 0:
        enemy4X_change = 0.8
        enemy4Y += enemy4Y_change
    if enemy4X >= 770:
        enemy4X_change = -0.8
        enemy4Y += enemy4Y_change
    enemy4X += enemy4X_change
    if enemy4Y >=400:
        game_over()
        playerX_change = 0
        enemy2X_change = 0
        enemy3X_change = 0
        enemy4X_change = 0
        enemy5X_change = 0
        enemyX_change = 0
        bulletY_change = 0
        over_sound = pygame.mixer.Sound('sound/game over.wav')
        pygame.mixer.Sound.play(over_sound )

     #Movement of enemy 5
    if enemy5X <= 0:
        enemy5X_change = 0.7
        enemy5Y += enemy3Y_change
    if enemy5X >= 770:
        enemy5X_change = -0.7
        enemy5Y += enemy5Y_change
    enemy5X += enemy5X_change
    if enemy5Y >=400:
        game_over()
        playerX_change = 0
        enemy2X_change = 0
        enemy3X_change = 0
        enemy4X_change = 0
        enemy5X_change = 0
        enemyX_change = 0
        bulletY_change = 0
        over_sound = pygame.mixer.Sound('sound/game over.wav')
        pygame.mixer.Sound.play(over_sound )



    #Movement of bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change 

    # Collision
    collision = iscollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        point_sound = pygame.mixer.Sound('sound/point.wav')
        pygame.mixer.Sound.play(point_sound )
        enemyX = random.randint(50,750)
        enemyY = random.randint(50,200)
    
    # Collision 2 
    collision2 = iscollision2(enemy2X,enemy2Y,bulletX,bulletY)
    if collision2:
        
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        point_sound = pygame.mixer.Sound('sound/point.wav')
        pygame.mixer.Sound.play(point_sound )
        enemy2X = random.randint(50,750)
        enemy2Y = random.randint(50,200)

    # Collision 3
    collision3 = iscollision3(enemy3X,enemy3Y,bulletX,bulletY)
    if collision3:
       
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        point_sound = pygame.mixer.Sound('sound/point.wav')
        pygame.mixer.Sound.play(point_sound )
        enemy3X = random.randint(50,750)
        enemy3Y = random.randint(50,200)

    # Collision 4
    collision4 = iscollision4(enemy4X,enemy4Y,bulletX,bulletY)
    if collision4:
        
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        point_sound = pygame.mixer.Sound('sound/point.wav')
        pygame.mixer.Sound.play(point_sound )
        enemy4X = random.randint(50,750)
        enemy4Y = random.randint(50,200)

    # Collision 5
    collision5 = iscollision5(enemy5X,enemy5Y,bulletX,bulletY)
    if collision5:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        point_sound = pygame.mixer.Sound('sound/point.wav')
        pygame.mixer.Sound.play(point_sound )
        enemy5X = random.randint(50,750)
        enemy5Y = random.randint(50,200)


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    enemy2(enemy2X,enemy2Y)
    enemy3(enemy3X,enemy3Y)
    enemy4(enemy4X,enemy4Y)
    enemy5(enemy5X,enemy5Y)
    show_score(textX,textY)
    pygame.display.update()