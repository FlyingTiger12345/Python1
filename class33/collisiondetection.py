import pygame

pygame.init()
x = 500
y = 500
screen = pygame.display.set_mode((x,y))

speed = 1

background_image = pygame.transform.scale(pygame.image.load("bigwin.png"),(x,y))
font = pygame.font.SysFont("Times New Roman",72)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, h,w):
        super().__init__()
        self.image = pygame.Surface([h,w])
        self.image.fill(color)

        self.rect = self.image.get_rect()
    def move(self,xchange,ychange):
        self.rect.x = max(min(self.rect.x + xchange , x - self.rect.w),0)
        self.rect.y = max(min(self.rect.y + ychange , y - self.rect.h),0)

clock = pygame.time.Clock()
all_sprite = pygame.sprite.Group()
sprite1 = Sprite("green",20,20)
sprite1.rect.x = 200
sprite1.rect.y = 200
all_sprite.add(sprite1)


sprite2 = Sprite("blue",20,20)
sprite2.rect.x = 200
sprite2.rect.y = 200
all_sprite.add(sprite2)

while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event == pygame.quit():
            quit()

    keys = pygame.key.get_pressed()

    xchange = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])*speed
    ychange = (keys[pygame.K_UP] - keys[pygame.K_DOWN])*speed
    Sprite.move(xchange,ychange)
    screen.blit(background_image(0,0))
    all_sprite.draw(screen)
    if sprite1.rect.colliderect(sprite2.rect):
        win_text = font.render("You win",True,pygame.color("purple"))
        screen.blit(win_text(200,200))
        all_sprite.remove(sprite2)


    pygame.display.flip()
    clock.tick(90)