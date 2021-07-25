import pygame
from pygame import display
from pygame import surface
from pygame import draw
from pygame import mouse 
from pygame.locals import *
from buttons import button
import os
import sys

def end_game_1():

    pygame.init()
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = Rect(0,0,1920,1080)
    solve_button = button(1920-5-200,450,200,100,text='solve')
    next_button = button(1920-5-200,650,200,100,text='Next')
    menu_button = button(5,1080-5-50,150,50,text='menu')
    
    draw_num = False

    i = 0
    j = 0

    clues = ['Same but different','Things people say when shaking hands',
    'New years resolutions','Events and their months']

    clue_button = button(1920/2 - 900/2,200,800,50,text=f'{clues[0]}')

    texts = ['DP PLG NG RS','DNT CLTW NS','MR R RMG','LL TR PS',
    'HWD YD','PLS DTM TY','WL LPL YD','CNGR TL TNS',
    'S TPSM KN G','XRC SM R','D RN KL SSL CH L','LR N NWEL NG G',
    'HLL WNN DCT BR','STR SND YND MRC HRP RL','GRN DH GD YN DF BRRY','GRN DH GD YN DF BRRY']

    real_texts = ['DOPPELGANGERS','IDENTICAL TWINS','MIRROR IMAGE','ALLOTROPES',
    "HOW'D YA DO",'PLEASED TO MEET YOU','WELL PLAYED','CONGRATULATIONS',
    'STOP SMOKING','Exericse More','Drink less Alcohol','Learn a new language',
    'Halloween and October','Easter Sunday and March or April','Groundhog day and February','Groundhog day and February']

    text_button = button(500,600,600,50,text=f'{texts[0]}')

    global squares
    squares = []
    start_countdown = False

    while True:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if solve_button.isOver(mouse_pos):
                   text_button = button(550,600,600,50,text=f'{real_texts[i]}')       
                if next_button.isOver(mouse_pos):
                    if i == len(texts)-1:
                        text_button = button(550,600,600,50,text='End')
                    else:
                        if i in [3,7,11]:
                            j+=1
                            clue_button = button(1920/2 - 900/2,200,800,50,text=f'{clues[j]}')
                        i+=1
                        text_button = button(550,600,600,50,text=f'{texts[i]}')
                if menu_button.isOver(mouse_pos):
                    return
        #####Calculations####

        ####Drawing####
        pygame.draw.rect(screen,(190,80,50),rect=background)
        
        text_button.draw_text(screen,size=150)
        clue_button.draw_wtext(screen)

        ##Middle cards
        for button_ in squares:
            button_.draw_wtext(screen,font_size=75)

        solve_button.draw_wtext(screen)
        next_button.draw_wtext(screen)
        menu_button.draw_wtext(screen)

        clock.tick(60)
        pygame.display.update()
