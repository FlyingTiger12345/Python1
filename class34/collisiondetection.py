import pygame
import random
import math

Screen_Width = 800
Screen_Height = 500
Player_Start_X = 370
Player_Start_Y = 380
Player_Start_Y_Min = 50
Player_Start_Y_Max = 150
Enemy_Speed_X = 4
Enemy_Speed_Y = 20
Bullet_Speed_Y = 10
Collison_Distance = 27



pygame.init()



screen = pygame.display.set_mode((Screen_Width,Screen_Height))

background = pygame.transform.scale(pygame.image.load("bigwin.jpg").convert(),(400,400))


playerImg = pygame.image.load("bigwin.jpg")
playerx = Player_Start_X
playery = Player_Start_Y
playerx_change = 0


def player(x,y):
   screen.blit(playerImg,(x,y))
EnemyImg = []
Enemyx = []
Enemyy = []
Enemy_change_x = []
Enemy_change_y = []
num_of_enemy = 6

for i in range(num_of_enemy):
   EnemyImg.append(pygame.image.load("bigwin.jpg"))
   Enemyx.append(random.randint(0,Screen_Width - 64))
   Enemyy.append(random.randint(Player_Start_X,Player_Start_Y))
   Enemy_change_y.append((Enemy_change_y))
   Enemy_change_x.append((Enemy_change_x))

score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textx =  10
texty = 10

over_font = pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
   score = font.render("Score : " + str(score_value), True, (255,255,255))
   screen.blit(score,(x,y))

def game_over_text():
   over_text = font.render("Game Over " + str(score_value), True, (255,255,255))
   screen.blit(over_text,(200,250))

def enemy(x,y,i):
   screen.blit(EnemyImg[i],(x,y))
def playeer(x,y,):
   screen.blit(playerImg[i],(x,y))

def firebullet(x,y):
   global bullet_state
   bullet_state = "fire"
   screen.blit(bulletImg,(x+1666,y+16))




bulletImg = pygame.image.load("bigwin.jpg")

bulletx = 0
bullety = Player_Start_Y
bulletx_change = 0
bullety_change = Bullet_Speed_Y
bullet_state = "ready"

def fire_bullet(x,y):
   
   bullet_state = "fire"
   screen.blit(bulletImg,(x + 16,y + 10))

def isCollison(enemyX,enemyY,bulletX,bulletY):
   distance = math.sqrt((enemyX-bulletX)** 2 + (enemyY - bulletY)** 2)
   return distance < Collison_Distance


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
             playerX_change = -5

             if event.key == pygame.K_RIGHT:
                playerX_change = 5

             if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerx
                bullet_state = "fire"

                fire_bullet(bulletx,bullety)

             if event.type == pygame.KEYUP and event.key in [pygame.K_RIGHT , pygame.K_LEFT]:
                playerx_change = 0

            playerx += playerx_change
            playerx = max(0, min(playerx, Screen_Width - 64))
            for i in range(num_of_enemy):
               if Enemyy[i] > 340:
                  for j in range(num_of_enemy):
                     Enemyy[i] = 2000
                     game_over_text()
                     break
               Enemyy[i] += Enemy_change_x[i]
               if Enemyx[i] <= 0 or Enemyx[i] >= Screen_Width - 64:
                  Enemy_change_x[i] *= -1
                  Enemyy[i] += Enemy_change_y[i]
               if isCollison(Enemyx[i],Enemyy[i],bulletx,bullety):
                  bulletY = Player_Start_Y
                  bullet_state = "ready"
                  score_value += 1
                  Enemyx[i] = random.randint(0,Screen_Width - 64)
                  Enemyy[i] = random.randint(Player_Start_Y_Max,Player_Start_Y_Max)
               enemy(Enemyx[i],Enemyy[i], i)

               
            if Enemyy[i]:
               if bullety <= 0:
                  bullety = Player_Start_Y
               bullet_state = "ready"
            elif bullet_state == "fire":
                fire_bullet(bulletx,bullety)
                bullety -= bullety_change
            player(playerx,playery)
            