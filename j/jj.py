from pygame import *

speed_x = 4
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


win_width = 800
win_height = 500

img_back = "bg.png"

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 720, 200, 50, 150, 4)
ball = GameSprite('tennis.png', 350, 200, 50, 50, 4)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 l', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 l', True, (180, 0, 0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        racket1.updateL()
        racket2.updateR()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1.1
            speed_y *= 1.1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1.1
            speed_x *= 1.1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True


        racket1.reset()
        racket2.reset()
        ball.reset()

        display.update()
        clock.tick(FPS)
        

