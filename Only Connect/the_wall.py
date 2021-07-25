import pygame
from pygame import display
from pygame import surface
from pygame import draw
from pygame import mouse 
from pygame.locals import *
from buttons import button
from pygame import mixer
import os
import sys

def the_grid_1():



    pygame.init()
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = Rect(0,0,1920,1080)

    mixer.init()
    mixer.music.load("wrong_bychabs.mp3")
    mixer.music.set_volume(3)

    ###Making the buttons####

    grid_buttons = []
    are_buttons_highligted = [False for i in range(16)]
    are_buttons_toggled = [False for i in range(16)]
    is_button_live = [True for i in range(16)]
    pause_button = button(3,1080-50-3,150,50,text='pause')
    solve_button = button(1920-200-4,1080-100-4,200,100,color=(255,100,50),text='Solve')
    menu_button = button(4,4,150,50,color=(255,100,50),text='Menu')
    

    correct_groups=[[0,2,7,12],[8,10,13,14],[1,6,9,11],[3,4,5,15]] #this must be in ascending order, within the groups

    tile_texts = ['Aversion','Fringe','\nElectro-\nShock','Radiation',
    'Asteriod','Green','Braid','Gestalt',
    'Rough','Ruffle', 'Out of\nBounds','Gimp',
    'Gene','Bunker','Fairway','Trouser']

    for i in range(4):
        for j in range(4):
            button1 = button(230+370*j,175+190*i,340,165,color=(50,100,250),text=f'{tile_texts[j+4*i]}')
            grid_buttons.append(button1)

    def create_solved_buttons():
        solved_buttons = []
        for i in range(4):
            for j in range(4):
                button1 = button(230+370*j,175+190*i,340,165,color=(50,100,250),text=f'{tile_texts[correct_groups[i][j]]}')
                solved_buttons.append(button1)
        return solved_buttons

    can_toggle = True 
    draw_grid = True
    countdown_finished = False
    countdown = True
    draw_solve = False
    timer = -1
    can_solve = False
    solved_groups = 0
    draw_rect = False
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
            if event.type == MOUSEMOTION:
                for button_number in range(len(grid_buttons)):
                    if is_button_live[button_number]:
                        if grid_buttons[button_number].isOver(mouse_pos):
                            are_buttons_highligted[button_number] = True
                        else:
                            are_buttons_highligted[button_number] = False

            if event.type == MOUSEBUTTONDOWN:
                for button_number in range(len(grid_buttons)):
                    if grid_buttons[button_number].isOver(mouse_pos):
                        if is_button_live[button_number]:
                            if are_buttons_toggled[button_number] == True:
                                are_buttons_toggled[button_number] = False
                                continue # so we don't just toggle back
                            if are_buttons_toggled[button_number] == False and can_toggle:
                                are_buttons_toggled[button_number] = True
                if solve_button.isOver(mouse_pos):
                    if can_solve:
                        grid_buttons = create_solved_buttons()
                        is_button_live = [True for i in range (16)]
                
                if pause_button.isOver(mouse_pos):
                    if countdown == True:
                        countdown = False
                        pygame.mixer.Channel(0).pause()
                        draw_rect = True
                    else:
                        countdown = True
                        pygame.mixer.Channel(0).unpause()
                        draw_rect = False
                if menu_button.isOver(mouse_pos):
                    pygame.mixer.stop()
                    return
                    

                
                    

        #####Calculations####
        num_of_selected_tiles = are_buttons_toggled.count(True)
        if num_of_selected_tiles >=4:
            can_toggle = False
            highlighted_list = []
            for index in range(16):

                if are_buttons_toggled[index] == True:
                    highlighted_list.append(index)

            if highlighted_list == correct_groups[0]:
                print('bingo1')
                highlighted_list.reverse()
                for grid_number in highlighted_list:
                    is_button_live[grid_number] = False
                    are_buttons_toggled = [False for i in range(16)]
                    are_buttons_highligted = [False for i in range(16)]
                solved_groups +=1
            elif highlighted_list == correct_groups[1]:
                print('bingo2')
                highlighted_list.reverse()
                for grid_number in highlighted_list:
                    is_button_live[grid_number] = False
                    are_buttons_toggled = [False for i in range(16)]
                    are_buttons_highligted = [False for i in range(16)]
                solved_groups +=1
            elif highlighted_list == correct_groups[2]:
                print('bingo3')
                highlighted_list.reverse()
                for grid_number in highlighted_list:
                    is_button_live[grid_number] = False
                    are_buttons_toggled = [False for i in range(16)]
                    are_buttons_highligted = [False for i in range(16)]
                solved_groups +=1
            elif highlighted_list == correct_groups[3]:
                highlighted_list.reverse()
                for grid_number in highlighted_list:
                    is_button_live[grid_number] = False
                    are_buttons_toggled = [False for i in range(16)]
                    are_buttons_highligted = [False for i in range(16)]
                print('bingo4')
                solved_groups +=1
            else:
                are_buttons_toggled = [False for i in range(16)]
                sound = pygame.mixer.Sound('wrong_bychabs.mp3')
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(sound))
        else:
            can_toggle = True

        if solved_groups == 4:
            draw_solve = True
            can_solve = True
        ###Countdown
        if countdown:
            draw_buttons = False
            timer+=1
            x = 181 #number of seconds for countdown
            '''Handling the countdown'''
            if timer == 0:
                pygame.mixer.Channel(0).set_volume(0.3)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('timer.mp3'))
            if timer%60 == 0 and timer < 60*x-1:
                draw_num = True
                num_button = button(1920/2-50,10,100,100,text=f'{x - timer//60}')
            if timer >= 60*x:
                draw_num = False
                countdown_finished = True
                can_solve = True


        ##Solve button###

        if countdown_finished:
            countdown_finished = False
            draw_solve = True
            can_solve = True
        ####Drawing####
        if draw_solve:
            solve_button.draw_wtext(screen)


        #Background
        pygame.draw.rect(screen,color=(120,120,120),rect=background) # The outline

        #Drawing buttons, and colors
        if draw_solve:
            solve_button.draw_wtext(screen)
        

        if draw_grid:
            for index,button_ in enumerate(grid_buttons):
                if is_button_live[index]:
                    if are_buttons_highligted[index] == False and are_buttons_toggled[index] == False:
                        button_.color = (50,100,250)
                        button_.draw_wtext(screen)
                    elif are_buttons_toggled[index] == False:
                        button_.color = (175,100,150)
                        button_.draw_wtext(screen)
                    else:
                        button_.color = (200,50,50)
                        button_.draw_wtext(screen)


        if draw_rect:
            pygame.draw.rect(screen,color=(120,120,120),rect=background) # The outline
        pause_button.draw_wtext(screen)
        if draw_num:
            num_button.draw_text(screen,size=100)
        menu_button.draw_wtext(screen)

        clock.tick(60)
        pygame.display.update()

def the_grid_2():


    pygame.init()
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = Rect(0,0,1920,1080)

    mixer.init()
    mixer.music.load("wrong_bychabs.mp3")
    mixer.music.set_volume(3)

    ###Making the buttons####

    grid_buttons = []
    are_buttons_highligted = [False for i in range(16)]
    are_buttons_toggled = [False for i in range(16)]
    is_button_live = [True for i in range(16)]
    pause_button = button(3,1080-50-3,150,50,text='pause')
    solve_button = button(1920-200-4,1080-100-4,200,100,color=(255,100,50),text='Solve')
    menu_button = button(4,4,150,50,color=(255,100,50),text='Menu')
    

    correct_groups=[[6,7,10,14],[1,5,11,15],[0,3,9,12],[2,4,8,13]] #this must be in ascending order, within the groups

    tile_texts = ['Marble','Shonky','Risk','Dundee','Bath','Barbie','Busby',
    'Tankard','Race','Angel','Cabbage','Pash','Madeira','Errand','Vandal','Drongo']

    for i in range(4):
        for j in range(4):
            button1 = button(230+370*j,175+190*i,340,165,color=(50,100,250),text=f'{tile_texts[j+4*i]}')
            grid_buttons.append(button1)

    def create_solved_buttons():
        solved_buttons = []
        for i in range(4):
            for j in range(4):
                button1 = button(230+370*j,175+190*i,340,165,color=(50,100,250),text=f'{tile_texts[correct_groups[i][j]]}')
                solved_buttons.append(button1)
        return solved_buttons

    can_toggle = True 
    draw_grid = True
    countdown_finished = False
    countdown = True
    draw_solve = False
    timer = -1
    can_solve = False
    solved_groups = 0
    draw_rect = False
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
            if event.type == MOUSEMOTION:
                for button_number in range(len(grid_buttons)):
                    if is_button_live[button_number]:
                        if grid_buttons[button_number].isOver(mouse_pos):
                            are_buttons_highligted[button_number] = True
                        else:
                            are_buttons_highligted[button_number] = False

            if event.type == MOUSEBUTTONDOWN:
                for button_number in range(len(grid_buttons)):
                    if grid_buttons[button_number].isOver(mouse_pos):
                        if is_button_live[button_number]:
                            if are_buttons_toggled[button_number] == True:
                                are_buttons_toggled[button_number] = False
                                continue # so we don't just toggle back
                            if are_buttons_toggled[button_number] == False and can_toggle:
                                are_buttons_toggled[button_number] = True
                if solve_button.isOver(mouse_pos):
                    if can_solve:
                        grid_buttons = create_solved_buttons()
                        is_button_live = [True for i in range (16)]
                
                if pause_button.isOver(mouse_pos):
                    if countdown == True:
                        countdown = False
                        pygame.mixer.Channel(0).pause()
                        draw_rect = True
                    else:
                        countdown = True
                        pygame.mixer.Channel(0).unpause()
                        draw_rect = False
                if menu_button.isOver(mouse_pos):
                    pygame.mixer.stop()
                    return
                    

                
                    

        #####Calculations####
        num_of_selected_tiles = are_buttons_toggled.count(True)
        if num_of_selected_tiles >=4:
            can_toggle = False
            highlighted_list = []
            for index in range(16):

                if are_buttons_toggled[index] == True:
                    highlighted_list.append(index)

            if highlighted_list == correct_groups[0]:
                print('bingo1')
                highlighted_list.reverse()
                for grid_number in highlighted_list:
                    is_button_live[grid_number] = False
                    are_buttons_toggled = [False for i in range(16)]
                    are_buttons_highligted = [False for i in range(16)]
                solved_groups +=1
            elif highlighted_list == correct_groups[1]:
                print('bingo2')
                highlighted_list.reverse()
                for grid_number in highlighted_list:
                    is_button_live[grid_number] = False
                    are_buttons_toggled = [False for i in range(16)]
                    are_buttons_highligted = [False for i in range(16)]
                solved_groups +=1
            elif highlighted_list == correct_groups[2]:
                print('bingo3')
                highlighted_list.reverse()
                for grid_number in highlighted_list:
                    is_button_live[grid_number] = False
                    are_buttons_toggled = [False for i in range(16)]
                    are_buttons_highligted = [False for i in range(16)]
                solved_groups +=1
            elif highlighted_list == correct_groups[3]:
                highlighted_list.reverse()
                for grid_number in highlighted_list:
                    is_button_live[grid_number] = False
                    are_buttons_toggled = [False for i in range(16)]
                    are_buttons_highligted = [False for i in range(16)]
                print('bingo4')
                solved_groups +=1
            else:
                are_buttons_toggled = [False for i in range(16)]
                sound = pygame.mixer.Sound('wrong_bychabs.mp3')
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(sound))
        else:
            can_toggle = True

        if solved_groups == 4:
            draw_solve = True
            can_solve = True
        ###Countdown
        if countdown:
            draw_buttons = False
            timer+=1
            x = 181 #number of seconds for countdown
            '''Handling the countdown'''
            if timer == 0:
                pygame.mixer.Channel(0).set_volume(0.3)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('timer.mp3'))
            if timer%60 == 0 and timer < 60*x-1:
                draw_num = True
                num_button = button(1920/2-50,10,100,100,text=f'{x - timer//60}')
            if timer >= 60*x:
                draw_num = False
                countdown_finished = True
                can_solve = True


        ##Solve button###

        if countdown_finished:
            countdown_finished = False
            draw_solve = True
            can_solve = True
        ####Drawing####
        if draw_solve:
            solve_button.draw_wtext(screen)


        #Background
        pygame.draw.rect(screen,color=(120,120,120),rect=background) # The outline

        #Drawing buttons, and colors
        if draw_solve:
            solve_button.draw_wtext(screen)
        

        if draw_grid:
            for index,button_ in enumerate(grid_buttons):
                if is_button_live[index]:
                    if are_buttons_highligted[index] == False and are_buttons_toggled[index] == False:
                        button_.color = (50,100,250)
                        button_.draw_wtext(screen)
                    elif are_buttons_toggled[index] == False:
                        button_.color = (175,100,150)
                        button_.draw_wtext(screen)
                    else:
                        button_.color = (200,50,50)
                        button_.draw_wtext(screen)


        if draw_rect:
            pygame.draw.rect(screen,color=(120,120,120),rect=background) # The outline
        pause_button.draw_wtext(screen)
        if draw_num:
            num_button.draw_text(screen,size=100)
        menu_button.draw_wtext(screen)

        clock.tick(60)
        pygame.display.update()