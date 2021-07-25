from ai_vs_human import play_ai_vs_human
import pygame
from pygame.locals import *
import sys
from buttons import button 
from human_vs_human import run_game
from human_vs_ai import play_human_vs_ai
import os



#######Parameters before loop#####
def main_menu():
    ##Colors
    cwd = os.getcwd()
    images_folder = os.path.join(cwd, 'images')

    def get_path(filename, images_folder = images_folder):
        '''
        Takes a file name, and returns its path.
        '''

        path = os.path.join(images_folder, filename)
        print(path)
        return path

    pygame.init()
    
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)

    clock = pygame.time.Clock()

    WINDOW_SIZE = (1280,720)
    screen = pygame.display.set_mode(WINDOW_SIZE)

    

    test_rect = pygame.Rect(300,300,100,100)


    background = pygame.image.load(get_path('background_1.png'))
    button_img = pygame.image.load(get_path('Button.png'))
    text_header = pygame.image.load(get_path('Button_header.png'))
    linkedin_img = pygame.image.load(get_path('linked_in_button.png'))

    button_x = WINDOW_SIZE[0]/2 - 500/2
    button_positions = [(button_x,240),(button_x,390),(button_x,540)]

    button_1 = button((0,0,0),button_x,240,500,80,text='Human vs AI')
    button_2 = button((0,0,0),button_x,390,500,80, text=' AI vs Human')
    button_3 = button((0,0,0),button_x,540,500,80, text = 'Human vs Human')
    button_header = button((0,0,0),(1280-1000)/2, 50,1000,120, text ='Tic Tac Toe - By Charlie Gaynor')
    linkedin_button = button((0,0,0),1245-250,650,250,50,text='linkedin.com/in/CharlieGaynor')

    button_1_over = False
    button_2_over = False
    button_3_over = False


    while True:

        screen.blit(background,(0,0))

        #### Event loop ###
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if button_1.isOver(mouse_pos):
                    #print('why am i running') error not here
                    play_human_vs_ai()
                if button_2.isOver(mouse_pos):
                    play_ai_vs_human()
                if button_3.isOver(mouse_pos):
                    run_game()
            if event.type == MOUSEMOTION:
                if button_1.isOver(mouse_pos):
                    button_1_over = True
                else:
                    button_1_over = False
                if button_2.isOver(mouse_pos):
                    button_2_over = True
                else:
                    button_2_over = False
                if button_3.isOver(mouse_pos):
                    button_3_over = True
                else:
                    button_3_over = False
        ### Calculations ###

        ## Drawing ###

        button_1.draw(screen)
        button_2.draw(screen)
        button_3.draw(screen)

        for i in range(3):
            screen.blit(button_img,(button_positions[i]))

        if button_1_over:
            button_1.draw_text(screen,color=(10,150,255))
        else:
            button_1.draw_text(screen)
        if button_2_over:
            button_2.draw_text(screen,color=(10,150,255))
        else:
            button_2.draw_text(screen)
        if button_3_over:
            button_3.draw_text(screen,color=(10,150,255))
        else:
            button_3.draw_text(screen)
        

        button_header.draw(screen)
        linkedin_button.draw(screen)
        screen.blit(text_header,((1280-1000)//2,50))
        screen.blit(linkedin_img, (1245-250,650))

        button_header.draw_text(screen,color=(10,200,255),size = 70)
        linkedin_button.draw_text(screen, size=23)

    
        ### Rendering ###
        clock.tick(60)
        pygame.display.update()





