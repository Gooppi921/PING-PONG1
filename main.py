from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, p_img, p_x, p_y, p_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(p_img),(w, h))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

window = display.set_mode((600,500))

back = (200, 255, 255)
win_width = 600
win_height = 500
window=display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60
total = 0
total2 = 0
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))


speed_x = 3
speed_y = 3

background2 = transform.scale(image.load('img.png'),(win_width, win_height))
finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                run = False
        window.blit(background2,(0,0))
        z = font.render('Игра PING-PONG', True, (255, 69, 0))
        zz = z.get_rect(center = (280,50))
        window.blit(z,zz)
        display.update()
        time.delay(50)






while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        score = font.render('Отбитий 1 игрока: ' + str(total), True, (255, 69, 0))
        score2 = font.render('Отбитий 2 игрока: ' + str(total2), True, (255, 69, 0))
        window.fill((200, 255, 255))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball):
            speed_x = speed_x*(-1)
            speed_y *= 1
            total+=1

        if sprite.collide_rect(racket2, ball):
            speed_x = speed_x*(-1)
            speed_y *= 1
            total2+=1    

        if ball.rect.y > 500-50 or ball.rect.y <0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
            game_over = True
        if ball.rect.x > 550:
            finish = True
            window.blit(lose2, (200,200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
        window.blit(score, (30,30))
        window.blit(score2, (300,30))
    display.update()
    time.Clock().tick(60)