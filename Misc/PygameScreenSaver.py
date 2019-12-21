import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))

blue = True
done = False
x= 30
y= 30
r=255
g=0
b=0
xmovement = 1
ymovement = 1
clock = pygame.time.Clock()
colorArray = []
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=5
    if pressed[pygame.K_DOWN]: y+=5
    if pressed[pygame.K_LEFT]: x-=5
    if pressed[pygame.K_RIGHT]:x+=5
    # pygame.Rect (x,y position, width, height)
    # 0,0 x y position is the top left corner
    # color = (r,g,b)

    if(r == 255):
        b=0
        g+=1
    if(g == 255):
        r=0
        b+=1
    if(b == 255):
        g=0
        b=0
        r+=1    
    
    color = (r,g,b)
    x+=xmovement
    y+=ymovement
    if(x == 800 or x ==0):
        xmovement *= -1
    if(y== 600 or y==0):
        ymovement *= -1
    
    pygame.draw.rect(screen, color,(x,y,20  ,20))
    clock.tick(60)
    pygame.display.flip()

