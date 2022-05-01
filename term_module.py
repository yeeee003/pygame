import pygame
import sys
from pygame.locals import QUIT, KEYDOWN
from time import sleep
import random

pygame.init()
screen_Width = 600
screen_Height = 900

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



def select_stage():

    global screen,background,fontObj,textSurfaceObj,textRectObj,textRectObj
    fontObj= pygame.font.Font('font\Typo_CrayonM.ttf',20)

    screen.fill((255,255,255))
   
    background= pygame.image.load('stage2.png')
    drawObject(background,0,0)
    
    pygame.display.update()



def initGame():

    global screen, clock, shuttle, missile, block, background, Char
    pygame.init()
    
    screen = pygame.display.set_mode((screen_Width, screen_Height))
    background= pygame.image.load("back1.png")
    Char = pygame.image.load('Char.png')
    block = pygame.image.load('block1.png')
    missile = pygame.image.load('missile.png')
    clock = pygame.time.Clock()

    


def drawObject(obj,x,y): #객체 생성
    global screen
    screen.blit(obj,(x,y))



def writetext(text): # 시스템 알림
    global screen

    font= pygame.font.Font('font\Typo_CrayonM.ttf',80)
    writeT=font.render(text,True,(0,0,0))
    tpos= writeT.get_rect()
    tpos.center=(screen_Width/2,screen_Height/2)
    screen.blit(writeT,tpos)
    pygame.display.update()
    sleep(10)
    
    runGame()


def writeScore(plus,minus): #점수 표시 + 게임 종료
    global screen
    font= pygame.font.Font('font\Typo_CrayonM.ttf',20)
    text=font.render(u'파이 재료:'+str(plus-minus),True,(0,0,0))
    screen.blit(text,(10,10))

    if minus>plus:
        writetext('게임 오버')


    if (plus-minus)>20:
        writetext('게임 클리어!')



def drawObject(obj,x,y):
    global screen
    screen.blit(obj,(x,y))


    
def runGame():

    global screen, clock, background, Char, CharX, missile, block

    CharSize= Char.get_rect().size
    CharWidth=CharSize[0]
    CharHeight=CharSize[1]

    #플레이어 좌표
    x = screen_Width * 0.45
    y = screen_Height * 0.8

    CharX=0
    missile_XY = []


    # 블럭 초기위치 설정
    block = pygame.image.load('block1.png')
    blockSize= block.get_rect().size
    blockWidth = blockSize[0]
    blockHeight = blockSize[1]

    blockX=random.randrange(0, screen_Width - blockWidth)
    blockY=0
    speed=4

    shotCount=0
    blockPassed=0
    
    shot=False
    over=False
    
    while not over:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                over=True
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    CharX -= 5

                elif event.key == pygame.K_RIGHT:
                    CharX += 5

                elif event.key == pygame.K_SPACE:
                    if len(missile_XY) < 2:
                        missileX = x + CharWidth/2
                        missileY = y - CharWidth/4
                        missile_XY.append([missileX,missileY])


            if event.type in [pygame.KEYUP]:
                if event.key==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    CharX=0

                
        drawObject(background,0,0)

        x+=CharX

        if x<0:
            x=0

        elif x > screen_Width - CharWidth:
            x=screen_Width - CharWidth



        if y < blockY + blockHeight:
            if blockX > x and blockX < x + CharWidth:
                writetext('게임오버')


        drawObject(Char, x, y)


        if len(missile_XY) != 0:
            for i, bxy in enumerate(missile_XY):
                bxy[1] -= 10
                missile_XY[i][1] = bxy[1]

              
                if bxy[1] < blockY:
                    if bxy[0]> blockX and bxy[0] < blockX + blockWidth:
                        missile_XY.remove(bxy)
                        shot=True
                        shotCount+=1

                    
                    if bxy[1] <=0:
                        try:
                            missile_XY.remove(bxy)

                        except:
                            pass
                    
        if len(missile_XY) != 0:
            for bx, by in missile_XY:
                drawObject(missile, bx, by)



        blockY+=speed
        

        if blockY > screen_Height:

            block=pygame.image.load('block1.png')
            blockSize= block.get_rect().size
            
            blockWidth = blockSize[0]
            blockHeight = blockSize[1]
            
            blockX=random.randrange(0, screen_Width - blockWidth)
            blockY=0
            blockPassed+=1
        
        writeScore(shotCount,blockPassed)


        if shot:
            
            block=pygame.image.load('block1.png')
            blockSize= block.get_rect().size
            
            blockWidth = blockSize[0]
            blockHeight = blockSize[1]
            
            blockX=random.randrange(0, screen_Width - blockWidth)
            blockY=0
            
            shot=False



        drawObject(block,blockX,blockY)
        pygame.display.update()

        clock.tick(60)


