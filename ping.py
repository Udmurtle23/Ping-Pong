
from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('fon.png'),(700,500))
clock = time.Clock()
font.init()
speed_x = 7
speed_y = 7

font1 = font.Font(None,30)
font2 = font.Font(None,70)

win1 = font2.render('Победил Первый игрок!',True,(0,0,0))
win2 = font2.render('Победил Второй игрок!',True,(0,0,0))





class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,w,h,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.y = player_y
        self.rect.x = player_x
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y <=420:
            self.rect.y += 10
        if keys_pressed[K_w] and self.rect.y >=0:
            self.rect.y -= 10
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y <=420:
            self.rect.y += 10
        if keys_pressed[K_UP] and self.rect.y >=0:
            self.rect.y -= 10
   

fps = 60

player1 = Player('raketa.png',0,200,40,80,2)
player2 = Player('raketa.png',660,200,40,80,2)
ball = GameSprite('newchu.png',250,200,60,60,2)






game = True
finish = False
while game:
    for e in event.get(): #ловит события
        if e.type == QUIT:
            game = False
        
        


    if finish != True:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        ball.reset()
        if ball.rect.y >= 440 or ball.rect.y <= 0:
            speed_y *= -1

        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1

        if ball.rect.x <= 0:
            window.blit(win2,(50,50))
            finish = True
        if ball.rect.x >= 700:
            window.blit(win1,(50,50))
            finish = True
            


    clock.tick(fps)
    display.update()

