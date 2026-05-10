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
Bullet_Collison = 27



pygame.init()



screen = pygame.display.set_mode((Screen_Width,Screen_Height))

background = pygame.transform.scale(pygame.image.load("bigwin.jpg").convert(),(400,400))


playerImg = pygame.image.load("bigwin.jpg")
playerx = Player_Start_X
playery = Player_Start_Y
playerx_change = 0


def player(x,y):
   screen.blit(playerImg,(x,y))



bulletImg = pygame.image.load("bigwin.jpg")

bulletx = 0
bullety = Player_Start_Y
bulletx_change = 0
bullety_change = Bullet_Speed_Y
bullet_state = "ready"

def fire_bullet(x,y):
   
   bullet_state = "fire"
   screen.blit(bulletImg,(x + 16,y + 10))


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
            if bullety <= 0:
               bullety = Player_Start_Y
               bullet_state = "ready"
            elif bullet_state == "fire":
                fire_bullet(bulletx,bullety)
                bullety -= bullety_change