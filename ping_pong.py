from pygame import *

win_width = 600
win_height = 500
display.set_caption("Ping - Pong")
window = display.set_mode((win_width, win_height))
background = ((200, 255, 255))
window.fill(background)
FPS = 60
clock = time.Clock()

# ======================= KELAS CHARACTER =======================
class Character(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Character):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

font.init()
font1 = font.SysFont("Arial", 30)

lose1 = font1.render("PLAYER 1 LOSE!!!", True, (180, 0, 0))
lose2 = font1.render("PLAYER 2 LOSE!!!", True, (180, 0, 0))

#win1 = font1.render("PLAYER 1 WIN!!!", True, (180, 0, 0))
#win2 = font1.render("PLAYER 2 WIN!!!", True, (180, 0, 0))


racket1 = Player('racket.png', 30, 200, 50, 150, 4) 
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = Character("ball.png", 200, 200, 50, 50, 50)

speed_x = 3
speed_y = 3


game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        speed_y *= 1

    #if the ball reaches screen edges, change its movement direction
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    #if ball flies behind this paddle, display loss condition for player 1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        game_over = True

    #if ball flies behind this paddle, display loss condition for player 2
    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2, (200, 200))
        game_over = True

    racket1.reset()
    racket2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)