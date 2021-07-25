import pygame
from pygame import display
from pygame import surface
from pygame import draw 
from pygame.locals import *
import os
import sys
from buttons import button
from pygame import mixer

def run_conundrom():

    pygame.init()
    mixer.init()
    clock = pygame.time.Clock()
    play_timer = False

    # Loading the song
    mixer.music.load("clock_sound.mp3")

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = pygame.Rect(0,0,1920,1080)
    menu_button = button(3,1080-50-3,200,50,color=(200,100,0),text='Menu')
    pause_button = button(1920/2 - 300/2,800,300,100,text='Toggle Pause')

    letters = ['P','E','N','I','S','T','A','L','E']
    solved = ['P','E','N','A','L','T','I','E','S']

    solve = button(1920/2 -200/2,700,200,50,text='Solve')
    ticker = -1

    draw_num = False
    

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
                if solve.isOver(mouse_pos):
                    letters = solved
                if menu_button.isOver(mouse_pos):
                    return
                if pause_button.isOver(mouse_pos):
                    if play_timer is False:
                        play_timer = True
                        mixer.music.play()
                    else:
                        play_timer = False
                        mixer.music.pause()
        if play_timer:
            draw_buttons = False
            ticker+=1
            x = 30
            '''Handling the countdown'''
            if ticker%60 == 0 and ticker < 60*x-1:
                if ticker == 0:
                    mixer.music.play()
                draw_num = True
                num_button = button(1920/2-50,500,100,100,text=f'{30 - ticker//60}')
            if ticker >= 60*x:
                draw_num = False
                finished = True

        ##Drawing##
        pygame.draw.rect(screen,color=(0,100,255),rect=background)
        solve.draw_wtext(screen)
        #Menu button#
        menu_button.draw_wtext(screen)
        pause_button.draw_wtext(screen)
        ##Countdown##
        if draw_num:
            num_button.draw_text(screen,size=300)
        ##Letter holders
        for i in range(9):
            pygame.draw.rect(screen,color=(150,150,255),rect=Rect(245+(1920-450)*i/9,245,170,170)) # The outline
            pygame.draw.rect(screen,color=(255,255,255),rect=Rect(250+(1920-450)*i/9,250,160,160))
            letter = button(250+(1920-450)*i/9,250,160,160,text=letters[i])
            letter.draw_text(screen,color=(0,0,0),size=100)

        clock.tick(60)
        pygame.display.update()