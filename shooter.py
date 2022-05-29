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

dx= 200
dy = 500
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    mouse = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    c = mouse
    click = pygame.mouse.get_pressed()
    if c[0]-70 >= dx+75 and c[0]-70 <= dx + 135 and c[1]-50 >= dy+25 and c[1]-50<= dy+120:
        if click[0] == 1:
            #gunSound.play()
            #clock.tick(100)
            aiya.play()
            dx = random.randrange(0,1000)
            dy = random.randrange(0,500)

    screen.fill((255,255,255))
    screen.blit(doge,(dx,dy))
    screen.blit(gun,c)
    pygame.draw.circle(screen,(255,0,0),(c[0]-70,c[1]-50),4)
    pygame.display.update()
    clock.tick()



