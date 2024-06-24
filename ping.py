
from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('fon.png'),(700,500))
clock = time.Clock()
font.init()

font1 = font.Font(None,30)
font2 = font.Font(None,70)

win = font2.render('Ты победил!',True,(0,255,0))
lose = font2.render('Ты проиграл!',True,(250,0,0))





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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x <=650:
            self.rect.x += 10
        if keys_pressed[K_a] and self.rect.x >=0:
            self.rect.x -= 10
   

fps = 60

#player = Player('tet.png',122,420,40,80,2)





game = True
finish = False
while game:
    for e in event.get(): #ловит события
        if e.type == QUIT:
            game = False
        


    if finish != True:
        window.blit(background,(0,0))
    clock.tick(fps)
    display.update()
