import pygame
from pygame import display
from pygame import surface
from pygame import draw
from pygame import color
from pygame import constants
from pygame import mouse 
from pygame.locals import *
from buttons import button
from buttons import get_path
import os
import sys
import random
import numpy as np
from pygame import mixer
  
# Starting the mixer
mixer.init()
  



def run_letters():

    pygame.init()
    mixer.init()
    clock = pygame.time.Clock()

    # Loading the song
    mixer.music.load("clock_sound.mp3")
  
    # Setting the volume
    mixer.music.set_volume(2)

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)

    background = pygame.Rect(0,0,1920,1080)

    vowel_button = button(0.18*1920,0.75*1080,450,150,color=(140,140,140),text='Vowel')
    consonant_button = button(1920-0.18*1920-450,0.75*1080,450,150,color=(140,140,140),text='Consonant')
    refresh_button = button(3,3,200,50,color=(200,100,0),text='Refresh')
    start_button = button(1920/2 - 450/2,0.75*1080,450,150,color=(140,140,140),text='Stand by')
    menu_button = button(3,1080-50-3,200,50,color=(200,100,0),text='Menu')

    def pick_vowel():

        '''bad way of picking vowels, but my first effort and makes ~0 difference changing it'''
        num = random.uniform(0,1)
        if num < 15/67:
            return 'A'
        elif num < (15+21)/67:
            return 'E'
        elif num < (15+21+13)/67:
            return 'I'
        elif num < (15+21+13+13)/67:
            return 'O'
        elif num < 1:
            return 'U'

    consonants = {'B':2,'C':3,'D':6,'F':2,'G':3,'H':2,'J':1,'K':1,'L':5,
    'M':4,'N':8,'P':4,'Q':1,'R':9,'S':9,'T':9,'V':1,'W':1,'X':1,'Y':1,'Z':1}


    letters = []
    num_vowels = 0
    ticker = -1
    num_cons =0 
    draw_buttons = True
    draw_num = False
    finished = False
    start_countdown = False
    show_start_button = False
    post_letters = [] #letters to put up on board after game done


    while True:

        #Events
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if finished and (event.key != K_ESCAPE):
                    if event.key == K_BACKSPACE:
                        if post_letters != []:
                            post_letters.pop()
                    else:
                        try:
                            post_letters.append(chr(event.key).upper())
                        except ValueError:
                            pass

            if event.type == MOUSEBUTTONDOWN:
                if vowel_button.isOver(mouse_pos):
                    if num_vowels != 5 and num_cons+num_vowels != 9:
                        letters.append(pick_vowel())
                        num_vowels +=1
                        
                if consonant_button.isOver(mouse_pos):
                    if num_cons != 6 and num_cons+num_vowels != 9:
                    ###Picking a consonant , then updating dictionary so we can't have 2 x's etc###
                        cons_sum = sum(consonants.values())
                        cons_probs = {letter: occurences/float(cons_sum) for letter, occurences in consonants.items()}
                        cons = np.random.choice(list(cons_probs.keys()), 1, p=list(cons_probs.values()))
                        letters.append(cons[0])

                        consonants[cons[0]] -=1

                        num_cons +=1


                if refresh_button.isOver(mouse_pos):
                    run_letters()
                    return
                if menu_button.isOver(mouse_pos):
                    return
                if start_button.isOver(mouse_pos) and (num_vowels+num_cons == 9):
                    start_countdown = True
        
        ###############Calculations#############
        if start_countdown:
            draw_buttons = False
            ticker+=1
            x = 30
            '''Handling the countdown'''
            if ticker%60 == 0 and ticker < 60*x-1:
                if ticker == 0:
                    mixer.music.play()
                draw_num = True
                num_button = button(1920/2-50,700,100,100,text=f'{30 - ticker//60}')
            if ticker >= 60*x:
                draw_num = False
                finished = True
        else:
            ticker=-1

        if num_vowels + num_cons == 9 and not start_countdown:
            show_start_button = True
            draw_buttons = False
        else:
            show_start_button = False
        #############Drawing###################

        #First the background and letter holders
        pygame.draw.rect(screen,color=(0,100,255),rect=background)
        for i in range(9):
            pygame.draw.rect(screen,color=(150,150,255),rect=Rect(245+(1920-450)*i/9,245,170,170)) # The outline
            pygame.draw.rect(screen,color=(255,255,255),rect=Rect(250+(1920-450)*i/9,250,160,160))

            if finished:
                pygame.draw.rect(screen,color=(150,150,255),rect=Rect(245+(1920-450)*i/9,645,170,170)) # The outline
                pygame.draw.rect(screen,color=(255,255,255),rect=Rect(250+(1920-450)*i/9,650,160,160))

                if len(post_letters) >= 1:
                    for i in range(len(post_letters)):
                        letter = button(250+(1920-450)*i/9,650,160,160,text=post_letters[i])
                        letter.draw_text(screen,color=(0,0,0),size=100)

        #Now draw the selected letters on
        if len(letters) >= 1:
            for i in range(len(letters)):
                letter = button(250+(1920-450)*i/9,250,160,160,text=letters[i])
                letter.draw_text(screen,color=(0,0,0),size=100)

        #Now draw vowel / consonant buttons
        if draw_buttons:
            vowel_button.draw_wtext(screen)
            consonant_button.draw_wtext(screen)
        if show_start_button:
            start_button.draw_wtext(screen)

        #If countdown started, draw numbers on
        if draw_num:
            num_button.draw_text(screen,size=300)

        refresh_button.draw_wtext(screen)
        #Menu button#
        menu_button.draw_wtext(screen)


        ##Misc 
        clock.tick(60)
        pygame.display.update()
