import pygame
from pygame import display
from pygame import surface
from pygame import draw 
from pygame.locals import *
from buttons import button
import os
import sys
import random
from pygame import mixer

def run_numbers():

    pygame.init()
    clock = pygame.time.Clock()

    # Loading the song
    mixer.music.load("clock_sound.mp3")
  
    # Setting the volume
    mixer.music.set_volume(2)

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)

    background = pygame.Rect(0,0,1920,1080)
    refresh_button = button(3,3,200,50,color=(200,100,0),text='Refresh')
    scramble_button = button(1920-3-200,3,200,50,color=(200,100,0),text='Scramble')
    menu_button = button(3,1080-50-3,200,50,color=(200,100,0),text='Menu')

    numbers =[]
    hide_num_buttons = False
    can_scramble = True
    show_target_number = False
    draw_num = False
    pick_target_number = False
    ticker = -1
    start_countdown = False
    countdown_ticker = -1
    large_numbers = 10 #just some random number that's not 0-4
    ##Creating the 'how many large numbers' buttons##

    how_many_large_buttons = []
    for i in range(5):
            how_many_large_buttons.append(
                button(245+20+(1920-450)*i/5,885,170,170,color=(150,150,255),text=f'{i}')
            )
    
    #Function to pick numbers#
    def pick_numbers(num_large_numbers):
        large_numbers = [25,50,75,100]
        small_numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
        temp_numbers = []

        for i in range(num_large_numbers):
            i = random.randint(0,len(large_numbers)-1)
            temp_numbers.append(large_numbers[i])
            large_numbers.pop(i)
        num_small_numbers = 6- num_large_numbers
        for j in range(num_small_numbers):
            i = random.randint(0,len(small_numbers)-1)
            temp_numbers.append(small_numbers[i])
            small_numbers.pop(i)

        return temp_numbers

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
                if refresh_button.isOver(mouse_pos):
                    run_numbers()
                    return
                if menu_button.isOver(mouse_pos):
                    return
                for i in range(5):
                    button_ = how_many_large_buttons[i]
                    if button_.isOver(mouse_pos) and not hide_num_buttons:
                        large_numbers = i
                        numbers = pick_numbers(large_numbers)
                        hide_num_buttons = True
                if can_scramble and scramble_button.isOver(mouse_pos):
                    pick_target_number = True
                    can_scramble = False

        ##Calculating####
        #Scrambling#
        if pick_target_number:
            ticker +=1
            x = 97
            if ticker %3 == 0 and ticker <=x:
                show_target_number = True
                target_number = random.randint(101,999)
            if ticker == x+1:
                target_number = random.randint(101,999)
            if ticker == x+120:
                start_countdown = True

        #Handling the countdown#
        if start_countdown:
            countdown_ticker+=1

            '''Handling the countdown'''
            if countdown_ticker%60 == 0 and countdown_ticker < 60*30-1:
                if countdown_ticker == 0:
                    mixer.music.play()
                draw_num = True
                num_button = button(1600,350,100,100,text=f'{30 - countdown_ticker//60}')
            if countdown_ticker >= 60*30:
                draw_num = False
        else:
            countdown_ticker=-1

        #####Drawing######

        #Background#
        pygame.draw.rect(screen,color=(0,100,255),rect=background)
        #Draw the number thingee#
        pygame.draw.rect(screen,color=(0,0,0),rect=Rect(1920/2 -600/2,100,600,200))
        if show_target_number:
            font = pygame.font.SysFont('comicsans', size=200)
            text = font.render(str(target_number), 1, (255,255,255))
            screen.blit(text, (1920/2 -600/2 + (600/2 - text.get_width()/2), 100 + (200/2 - text.get_height()/2)))
        #Number holders

        for i in range(6):
            pygame.draw.rect(screen,color=(150,150,255),rect=Rect(245+(1920-450)*i/6,645,170,170)) # The outline
            pygame.draw.rect(screen,color=(255,255,255),rect=Rect(250+(1920-450)*i/6,650,160,160))

        #Now draw the selected numbers on
        if len(numbers) >= 1:
            for i in range(len(numbers)):
                number = button(250+(1920-450)*i/6,650,160,160,text=str(numbers[i]))
                number.draw_text(screen,color=(0,0,0),size=100)

        ### Drawing the 'how many large numbers' buttons ###
        if not hide_num_buttons:
            for button_ in how_many_large_buttons:
                button_.draw_wtext(screen,font_size=100)

        ##Drawing countdown##

        if draw_num:
            num_button.draw_text(screen,size=300)

        ##Refresh button##
        refresh_button.draw_wtext(screen)
        #Scramble button#
        scramble_button.draw_wtext(screen)
        #Menu button#
        menu_button.draw_wtext(screen)

        clock.tick(60)
        pygame.display.update()
