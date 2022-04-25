from pygame import *
from time import time as timer
from time import sleep


class GameSprite(sprite.Sprite):


    def __init__(self,player_image,x,y,p_s,px,py):
        super().__init__()
        

        self.image = transform.scale(image.load(player_image),(px,py))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Players(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 105:
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 105:
            self.rect.y += self.speed
    



win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('PING-PONG')
bg = transform.scale(image.load('bg.jpg'),(win_width,win_height))

pl = Players('fff2.png',50,150,5,90,90)
pl2 = Players('fff.png',550,150,5,70,90)
ball = GameSprite('ng.png',win_width//2,150,5,50,50)





font.init()
font = font.SysFont('Times New Roman',50)
lose1 = font.render('PLAYER 1 LOSE!!!',True,(255,50,50))
lose2 = font.render('PLAYER 2 LOSE!!!',True,(255,50,50))

finish = False
game = True
FPS = 60
clock = time.Clock()

speedx = 4
speedy = 4
time1 = timer()
cur_time = False
tt_time = 1

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        
        cur_time = True
        


        window.blit(bg,(0,0))

        

        pl.reset()
        pl.update()

        pl2.reset()
        pl2.update2()
        ball.reset()

        ball.rect.x += speedx
        ball.rect.y += speedy        


            

        if sprite.collide_rect(pl , ball) or sprite.collide_rect(pl2 , ball):
            speedx *= -1
            speedy *= 1

        if ball.rect.y > win_width-250 or ball.rect.y < 0:
            speedy *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))

        if ball.rect.x > 700:
            finish = True
            window.blit(lose2,(200,200))

        if cur_time == True:
            tt_time = timer()







    

    




        

            








    display.update()
    clock.tick(FPS)

        


