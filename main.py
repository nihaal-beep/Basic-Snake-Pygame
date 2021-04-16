import pygame
import time
import random
pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("SNAKE")
running = True
blockX=[]
blockY=[]
endimg=pygame.image.load('gameover.png')
blockX.append(380)
blockY.append(220)
blockimg=[]
count=1
def display_score():
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {count}",True,(0,0,0))
        screen.blit(score,(700,10))
def block(k,l,m):
    #Figuring out the direction in which the new block will be appended           
    if direction=='left':
        k=k+25*m
    if direction=='right':
        k=k-(25*m)
    if direction =='up':
        l=l+25*m
    if direction=='down':
        l=l-(25*m)
    screen.blit(blockimg[m],(k,l))
headimg=pygame.image.load('square1.png')    
direction=''
bg=pygame.image.load("grass1.png")
appleimg= pygame.image.load('apple1.png')
pygame.display.set_icon(appleimg)
X=random.randint(10,790)
Y=random.randint(10,490)
test=1
applerect=appleimg.get_rect(topleft=(X,Y))   
def isCollision(x1, y1, x2, y2):
    blockrect=headimg.get_rect(topleft=(x2,y2))
    applerect=appleimg.get_rect(topleft=(x1,y1))   
    if blockrect.colliderect(applerect):
        return True
def testcondX(x1):
    if x1>=795 or x1<=4:
        return True       
def testcondY(y1):
    if y1>=495 or y1<=4:
        return True
gameover=False
#Game Loop
while running:
             
    screen.blit(bg,(0,0))    
    screen.blit(appleimg,(X,Y))    
    for event in pygame.event.get():        
        if event.type==  pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                direction = 'left'
            if event.key==pygame.K_RIGHT:
                direction='right'
            if event.key==pygame.K_DOWN:
                direction='down'
            if event.key==pygame.K_UP:
                direction='up'
    for i in range(0,count):
        #Movement of head       
        if direction == 'right':
            blockX[0]+=0.3
        if direction == 'left':
            blockX[0]-=0.3
        if direction == 'up':
            blockY[0]-=0.3
        if direction == 'down':
            blockY[0]+=0.3
    
    

    for i in range(0, count):
        if isCollision(X, Y, blockX[0], blockY[0]):
            X=random.randint(10,790)
            Y=random.randint(10,490)
            count+=1
            blockX.append(0)
            blockY.append(0)   
    if count>=2:       
        for i in range(count-1,0,-1):
            blockX[i]=blockX[i-1]
            blockY[i]=blockY[i-1]
    for i in range(count):
        blockimg.append(pygame.image.load('square.png'))
        block(blockX[i],blockY[i],i)
    applerect=appleimg.get_rect(topleft=(X,Y))
    display_score()
    if (testcondX(blockX[0]) or testcondY(blockY[0])):
        font = pygame.font.SysFont('arial',70)
        endscreen = font.render("GAME OVER",True,(0,0,0))
        screen.blit(endscreen,(225,200))
        for event in pygame.event.get():        
            if event.type==  pygame.QUIT:
                running=False   
    pygame.display.update()
