import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))

blue = True
done = False
x= 30
y= 30
xmovement = 1
ymovement = 1
image = pygame.image.load("JerryOnDrugs.jpg")
clock = pygame.time.Clock()
colorArray = []
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            
            blue = not blue
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=5
    if pressed[pygame.K_DOWN]: y+=5
    if pressed[pygame.K_LEFT]: x-=5
    if pressed[pygame.K_RIGHT]:x+=5
    # pygame.Rect (x,y position, width, height)
    # 0,0 x y position is the top left corner
    if(blue): 
        color = (0,128,255)
    else : color = (255,100,0)
    
    x+=xmovement
    y+=ymovement
    if(x == 500 or x ==0):
        xmovement *= -1
    if(y== 300 or y==0):
        ymovement *= -1
    

    screen.blit(image,(x,y))
    clock.tick(60)
    pygame.display.flip()

