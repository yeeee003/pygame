import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, KEYUP
import term_module as tm
from time import sleep
import pygame.mixer

tm.initGame()
pygame.mixer.init()


onGame= False
stage3=False
stage4=False

pygame.mixer.music.load('bensound-smile.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1,0.0)


tm.screen.fill((255,255,255))

tm.drawObject(tm.background,0,0)
tm.pygame.display.update()

while not onGame:

    for event in pygame.event.get():
        if event.type in [pygame.QUIT]:
            pygame.quit()
            sys.exit()

        
        elif event.type == pygame.MOUSEBUTTONUP and stage3==False:

            tm.select_stage()
            stage3=True

 
        elif event.type == KEYUP and stage3==True:
            if event.key == pygame.K_1:

                tm.initGame()

                tm.background=pygame.image.load('stage3.png')
                tm.drawObject(tm.background,0,0)
                pygame.display.update()
              
                stage4=True
                stage3=False

        elif event.type== KEYUP and stage4==True:
            if event.key == pygame.K_1:
    
                tm.screen.fill((0,255,0))
                tm.background=pygame.image.load('background.png')
                tm.drawObject(tm.background,0,0)
                pygame.display.update()
            
                gameS=True
                stage4==False
            
                if event.type== KEYUP and gameS==True:
                    tm.runGame()


            elif event.key == pygame.K_2:
                tm.background=pygame.image.load('stage4.png')
                tm.drawObject(tm.background,0,0)
                pygame.display.update()

                if event.key == pygame.K_1:
                    tm.screen.fill((0,255,0))
                    tm.background=pygame.image.load('background.png')
                    tm.drawObject(tm.background,0,0)
                    pygame.display.update()
            
                    gameS=True
                    stage4==False

                    if event.type== KEYUP and gameS==True:
                        tm.runGame()
                    
                

