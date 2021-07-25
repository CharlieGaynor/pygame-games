import pygame
from pygame import display
from pygame import surface
from pygame import draw 
from pygame.locals import *
from buttons import button
import os
import sys

def main_game_2():

    pygame.init()
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = Rect(0,0,1920,1080)
    start_button = button(5,5,150,50,text='Start')
    stop_button = button(1920-5- 150,5,150,50,text='Stop')
    menu_button = button(5,1080-5-50,150,50,text='menu')
    draw_num = False

    tiles_0 = ['21st: i','20th: The Sun','19th: The Daily\nTelegraph','18th:\nThe Observer']
    tiles_1 = ['6\nHydrogen','5\nHydrogen','4\nCarbon Dioxide','3\nNitrogen']
    tiles_2 = ['Park','Reverse','Neutral','Drive']
    tiles_3 = ['Coral','Arabian','South China','Mediterranean']
    tiles_4 = ['4\ntriangles','6\nsquares','8\nTriangles','12\nPentagons']
    tiles_5 = ['6 = Green','7 = Maroon','8 = Black','9 = Yellow stripe']

    tiles_set = [tiles_0,tiles_1,tiles_2,tiles_3,tiles_4,tiles_5]

    option_buttons = []
    letters = ['A','B','C','D','E','F']
    for i in range(6):
        temp_button = button(200 + 300*i,1000,150,50,text=f'{letters[i]}')
        option_buttons.append(temp_button)

    global squares
    squares = []
    number_buttons = []
    points = [5,3,2,1]
    start_countdown = False

    tiles = tiles_0.copy()

    for i in range(4):
            button1 = button(30+i*470,370,440,300,text='?')
            button2 = button(30+i*470,90,440,300,text=f'{points[i]}')
            squares.append(button1)
            number_buttons.append(button2)

    def update_buttons(tiles,position=0,replace_all=False):
        if replace_all:
            for i in range(4):
                button1 = button(30+i*470,370,440,300,text=f'?')
                squares[i] = button1
        else:
            i = position
            button1 = button(30+i*470,370,440,300,text=f'{tiles[i]}')
            squares[i] = button1
        return

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
                for i in range(4):
                    if squares[i].isOver(mouse_pos):
                        update_buttons(tiles,i)
                if start_button.isOver(mouse_pos):
                    start_countdown = True
                if stop_button.isOver(mouse_pos):
                    start_countdown = False
                    pygame.mixer.Channel(2).pause()
                for j in range(6):
                    if option_buttons[j].isOver(mouse_pos):
                        tiles = tiles_set[j].copy()
                        update_buttons(tiles,replace_all=True)
                if menu_button.isOver(mouse_pos):
                    pygame.mixer.stop()
                    return

        #####Calculations####


        '''Timer'''

        if start_countdown:

            ticker+=1
            x = 50 #amount of time
            '''Handling the countdown'''
            if ticker%60 == 0 and ticker < 60*x-1:
                if ticker == 0:
                    pygame.mixer.Channel(2).set_volume(0.3)
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound('mw2-soundtrack.mp3'))
                draw_num = True
                num_button = button(1920/2-50,30,100,100,text=f'{x - ticker//60}')
            if ticker >= 60*x:
                if ticker == 60*x:
                    pygame.mixer.Channel(2).stop()
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('times_up2.mp3'))
                draw_num = False
                finished = True
        else:
            ticker=-1
        ####Drawing####
        pygame.draw.rect(screen,(190,80,50),rect=background)
        
        ##Middle cards
        for button_ in squares:
            button_.draw_wtext(screen,font_size=75)

        for button_2 in number_buttons:
            button_2.draw_text(screen)
        #start button
        start_button.draw_wtext(screen)
        stop_button.draw_wtext(screen)
        #Buttons at bottom
        for button_ in option_buttons:
            button_.draw_wtext(screen,draw_outline = False)
        if draw_num:
            num_button.draw_text(screen,size=100)
        menu_button.draw_wtext(screen)

        clock.tick(60)
        pygame.display.update()

def main_game_1():

    pygame.init()
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = Rect(0,0,1920,1080)
    start_button = button(5,5,150,50,text='Start')
    stop_button = button(1920-5-150,5,150,50,text='Stop')
    menu_button = button(5,1080-5-50,150,50,text='menu')
    draw_num = False

    tiles_0 = ['Inward','Roting','Onflows','Ginks']
    tiles_1 = ['No \nNo','This \nWar','Brexit\nBrexit','Love\nNever needing to\nsay sorry']
    tiles_2 = ['On a\ntightrope\n44.63','Inside a\npantonmime\nhorse: 12.05','Giving a\npiggyback:\n16.97','Moonwalking\n32.06']
    tiles_3 = ['Not specific','Significant','Hook','Secret']
    tiles_4 = ['Cream','Quotation\nmarks','Tennis\nmatches','Yellow\nlines']
    tiles_5 = ['Italy:\n17','China:\n4','UK: 13','Triskaideka-\nphobics:\n13']

    tiles_set = [tiles_0,tiles_1,tiles_2,tiles_3,tiles_4,tiles_5]

    option_buttons = []
    letters = ['A','B','C','D','E','F']
    for i in range(6):
        temp_button = button(200 + 300*i,1000,150,50,text=f'{letters[i]}')
        option_buttons.append(temp_button)

    global squares
    squares = []
    number_buttons = []
    start_countdown = False
    points = [5,3,2,1]

    tiles = tiles_0.copy()

    for i in range(4):
            button1 = button(30+i*470,370,440,300,text='?')
            button2 = button(30+i*470,90,440,300,text=f'{points[i]}')
            squares.append(button1)
            number_buttons.append(button2)
    def update_buttons(tiles,position=0,replace_all=False):
        if replace_all:
            for i in range(4):
                button1 = button(30+i*470,370,440,300,text=f'?')
                squares[i] = button1
        else:
            i = position
            button1 = button(30+i*470,370,440,300,text=f'{tiles[i]}')
            squares[i] = button1
        return

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
                for i in range(4):
                    if squares[i].isOver(mouse_pos):
                        update_buttons(tiles,i)
                if start_button.isOver(mouse_pos):
                    start_countdown = True
                if stop_button.isOver(mouse_pos):
                    start_countdown = False
                    pygame.mixer.Channel(2).pause()
                for j in range(6):
                    if option_buttons[j].isOver(mouse_pos):
                        tiles = tiles_set[j].copy()
                        update_buttons(tiles,replace_all=True)
                if menu_button.isOver(mouse_pos):
                    pygame.mixer.stop()
                    return

        #####Calculations####


        '''Timer'''

        if start_countdown:

            ticker+=1
            x = 50 #amount of time
            '''Handling the countdown'''
            if ticker%60 == 0 and ticker < 60*x-1:
                if ticker == 0:
                    pygame.mixer.Channel(2).set_volume(0.1)
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound('mw2-soundtrack.mp3'))
                draw_num = True
                num_button = button(1920/2-50,30,100,100,text=f'{x - ticker//60}')
            if ticker >= 60*x:
                if ticker == 60*x:
                    pygame.mixer.Channel(2).stop()
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('times_up2.mp3'))
                draw_num = False
                finished = True
        else:
            ticker=-1
        ####Drawing####
        pygame.draw.rect(screen,(190,80,50),rect=background)
        
        ##Middle cards
        for button_ in squares:
            button_.draw_wtext(screen,font_size=75)
        for button_2 in number_buttons:
            button_2.draw_text(screen)
        #start button
        start_button.draw_wtext(screen)
        stop_button.draw_wtext(screen)
        #Buttons at bottom
        for button_ in option_buttons:
            button_.draw_wtext(screen,draw_outline = False)
        if draw_num:
            num_button.draw_text(screen,size=100)
        menu_button.draw_wtext(screen)

        clock.tick(60)
        pygame.display.update()
