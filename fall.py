import pygame,random
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1400,900))
pygame.display.set_caption('shoot')

gun = pygame.image.load('gun.png')
gun = pygame.transform.scale(gun,(250,250))
gun_rect = gun.get_rect()
c =  gun_rect.center
clock = pygame.time.Clock()
doge = pygame.image.load('doge.png')
doge = pygame.transform.scale(doge,(200,200))

aiya = pygame.mixer.Sound('aiya.wav')
gunSound = pygame.mixer.Sound('Gun+1.wav')


score = 0

dx1 = random.randrange(0,1200)
dy1 = 0
dx2 = random.randrange(0,1200)
dy2 = 0
dx3 = random.randrange(0,1200)
dy3 = 0
dx4 = random.randrange(0,1200)
dy4 = 0
dx5 = random.randrange(0,1200)
dy5 = 0


def dogef():
    global dy1,dx1,dx2,dx3,dx4,dx5,dy2,dy3,dy4,dy5
    if score < 5:
        screen.blit(doge,(dx1,dy1))
        dy1 += 1
    elif score >=5 and score<10:
        screen.blit(doge,(dx1,dy1))
        screen.blit(doge,(dx2,dy2))
        dy1 += 2
        dy2 += 2

    elif score >=10 and score<15:
        screen.blit(doge,(dx1,dy1))
        screen.blit(doge,(dx2,dy2))
        screen.blit(doge,(dx3,dy3))
        dy1 += 2
        dy2 += 2
        dy3 += 2

    elif score >= 15:
        screen.blit(doge,(dx1,dy1))
        screen.blit(doge,(dx2,dy2))
        screen.blit(doge,(dx3,dy3))
        screen.blit(doge,(dx4,dy4))
        #screen.blit(doge,(dx5,dy5))
        dy1 += 2
        dy2 += 2
        dy3 += 2
        dy4 += 2
        #dy5 += 4
 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    mouse = pygame.mouse.get_pos()
    #pygame.mouse.set_visible(False)
    c = mouse
    click = pygame.mouse.get_pressed()

    screen.fill((255,255,255))
    #screen.blit(doge,(dx1,dy1))
    dogef()
    screen.blit(gun,c)
    p = pygame.draw.circle(screen,(255,0,0),(c[0]-70,c[1]-50),4)

    if c[0]-70 >= dx1+75 and c[0]-70 <= dx1 + 135 and c[1]-50 >= dy1+25 and c[1]-50<= dy1+120:

        if click[0] == 1:
            #gunSound.play()
            #clock.tick(100)
            #aiya.play()
            dx1 = random.randrange(0,1000)
            dy1 = -100
            score += 1
            print(score,dy3)

    if c[0]-70 >= dx2+75 and c[0]-70 <= dx2 + 135 and c[1]-50 >= dy2+25 and c[1]-50<= dy2+120:

        if click[0] == 1:
            #gunSound.play()
            #clock.tick(100)
            #aiya.play()
            dx2 = random.randrange(0,1000)
            dy2 = -100
            score += 1
            print(score,dy3)

    if c[0]-70 >= dx3+75 and c[0]-70 <= dx3 + 135 and c[1]-50 >= dy3+25 and c[1]-50<= dy3+120:

        if click[0] == 1:
            #gunSound.play()
            #clock.tick(100)
            #aiya.play()
            dx3 = random.randrange(0,1000)
            dy3 = -100
            score += 1
            print(score,dy3)

    if c[0]-70 >= dx4+75 and c[0]-70 <= dx4 + 135 and c[1]-50 >= dy4+25 and c[1]-50<= dy4+120:

        if click[0] == 1:
            #gunSound.play()
            #clock.tick(100)
            #aiya.play()
            dx4 = random.randrange(0,1000)
            dy4 = -100
            score += 1
            print(score,dy3)

    if c[0]-70 >= dx5+75 and c[0]-70 <= dx5 + 135 and c[1]-50 >= dy5+25 and c[1]-50<= dy5+120:

        if click[0] == 1:
            #gunSound.play()
            #clock.tick(100)
            #aiya.play()
            dx5 = random.randrange(0,1000)
            dy5 = -100
            score += 1
            print(score,dy3)
    
    
    pygame.display.update()
    clock.tick(200)