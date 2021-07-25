from countdown_numbers import run_numbers
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
from countdown_letters import run_letters
from countdown_numbers import run_numbers
from conundrom import run_conundrom

def menu():

    pygame.init()
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = pygame.Rect(0,0,1920,1080)

    letter_game_button = button(1920/2-300/2,100,250,200,text='Letter Game')
    number_game_button = button(1920/2-300/2,600,250,200,text='Number Game')
    conundrom_button = button(1920/2-250/2,900,200,100,text='Conundrom')
    

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
                if letter_game_button.isOver(mouse_pos):
                    run_letters()
                if number_game_button.isOver(mouse_pos):
                    run_numbers()
                if conundrom_button.isOver(mouse_pos):
                    run_conundrom()

        #Drawing#
        pygame.draw.rect(screen,color=(0,100,255),rect=background)
        letter_game_button.draw_wtext(screen)
        number_game_button.draw_wtext(screen)
        conundrom_button.draw_wtext(screen)

        clock.tick(60)
        pygame.display.update()

menu()