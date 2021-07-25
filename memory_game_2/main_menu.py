from choose_N import run_choose_N
import pygame
from pygame.locals import *
import sys
from buttons import button
from buttons import get_path
import os




#######Parameters before loop#####
def main_menu():
    ##Colors


    pygame.init()
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1280,720)
    screen = pygame.display.set_mode(WINDOW_SIZE)


    print('cwd:', os.getcwd())



    background = pygame.image.load('background_1.png')
    linkedin_img = pygame.image.load('linked_in_button.png')

    button_x = WINDOW_SIZE[0]/2 - 500/2
    button_positions = [(button_x,360)]

    button_1 = button(button_x,360,500,80,text='Play')

    button_header = button((1280-1000)/2, 50,1000,120, text ='Memory game - By Charlie Gaynor')
    linkedin_button = button(1245-250,650,250,50,text='linkedin.com/in/CharlieGaynor')

    button_1_over = False

    tick = 0

    while True:
        tick +=1
        screen.blit(background,(0,0))

        #### Event loop ###
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if button_1.isOver(mouse_pos):
                    run_choose_N()
                    return

            if event.type == MOUSEMOTION:
                if button_1.isOver(mouse_pos):
                    button_1_over = True
                else:
                    button_1_over = False
                    

        ### Calculations ###

        ## Drawing ###

        button_1.draw(screen)

        if button_1_over:
            button_1.draw_text(screen,color=(10,150,255))
        else:
            button_1.draw_text(screen)


        button_header.draw(screen)
        linkedin_button.draw(screen)

        button_header.draw_text(screen,color=(10,200,255),size = 70)
        linkedin_button.draw_text(screen, size=23)

    
        ### Rendering ###
        clock.tick(60)
        pygame.display.update()


