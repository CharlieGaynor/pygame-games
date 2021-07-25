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
from main_game import main_game_1, main_game_2
from the_wall import the_grid_1, the_grid_2
from final_round import end_game_1

def menu():

    pygame.init()
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = pygame.Rect(0,0,1920,1080)

    main_game_button1 = button(1920/2-500,100,250,200,text='Theme')
    main_game_button2 = button(1920/2+300,100,250,200,text='Sequence')
    the_wallA = button(1920/2-300/2,600,250,200,text='The wall: A')
    the_wallB = button(1920/2-250/2,900,200,100,text='The wall: B')
    end_game_button = button(300,900,200,100,text='Final game')
    

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
                if main_game_button1.isOver(mouse_pos):
                    main_game_1()
                if main_game_button2.isOver(mouse_pos):
                    main_game_2()
                if the_wallA.isOver(mouse_pos):
                    the_grid_1()
                if the_wallB.isOver(mouse_pos):
                    the_grid_2()
                if end_game_button.isOver(mouse_pos):
                    end_game_1()

        #Drawing#
        pygame.draw.rect(screen,color=(0,100,255),rect=background)
        main_game_button1.draw_wtext(screen)
        main_game_button2.draw_wtext(screen)
        the_wallA.draw_wtext(screen)
        the_wallB.draw_wtext(screen)
        end_game_button.draw_wtext(screen)

        clock.tick(60)
        pygame.display.update()

menu()