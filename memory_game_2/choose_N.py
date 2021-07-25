
import pygame
from pygame.locals import *
import sys
from buttons import button
from buttons import get_path
from forward_game import run_forward_game
from backward_game import run_backward_game
import os




#######Parameters before loop#####
def run_choose_N():
    ##Colors


    pygame.init()
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1280,720)
    screen = pygame.display.set_mode(WINDOW_SIZE)

    REV_BUTTON_COLOR = (220,220,220)
    REV_TEXT_COLOR = (30,30,30)

    background = pygame.image.load('background_1.png')
    tick_pic = pygame.image.load('tick.png')

    button_x = WINDOW_SIZE[0]/2 - 700/2
    button_positions = [(button_x,360)]

    button_1 = button(button_x,260,700,80,text='How many starting numbers?')

    reverse_button1 = button(645, 597, width= 400, height = 50, text='Reverse Order?', color= REV_BUTTON_COLOR)
    reverse_button2 = button(1100,580,width = 80, height= 80)

    reverse_button_filled = -1
    reverse_button_hovered = False

    button_header = button((1280-1000)/2, 50,1000,120, text ='Memory game - By Charlie Gaynor')

    def make_sliders(start_N = 2, end_N = 12):
        
        start_x = (1280-1100)/2 -50
        end_x = (1280+1100)/2
        slider_buttons = []
        number_of_buttons = (end_N - start_N + 1)

        width = (end_x-start_x)/(number_of_buttons*2)
        for i in range(number_of_buttons):
            slider_buttons.append(
                button(
                    x= start_x + i*(end_x-start_x)/(number_of_buttons-1),
                    y=400, width = width,
                    height= 120,text=f'{i+start_N}'
                ))

        return slider_buttons

    def make_is_over_sliders(start_N=2, end_N = 12):
        '''
        Returns a list of True/False, which will eventually depend on whether mouse is over
        and hence controls the color of the text
        '''

        return [False for i in range(end_N - start_N+1)]

    slider_buttons = make_sliders()
    is_over_sliders = make_is_over_sliders()

    tick = 0

    just_unticked = 0

    while True:
        tick +=1
        screen.blit(background,(0,0))
        mouse_pos = pygame.mouse.get_pos()
        
        #### Event loop ###
        for event in pygame.event.get():
            

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

                

            if event.type == MOUSEMOTION:
                for j,slider in enumerate(slider_buttons):
                    if slider.isOver(mouse_pos):
                        is_over_sliders[j] = True
                    else:
                        is_over_sliders[j] = False
                
                if reverse_button2.isOver(mouse_pos):
                    if just_unticked == 1:
                        reverse_button_hovered = False
                    else:
                        reverse_button_hovered = True
                else:
                    reverse_button_hovered = False
                    just_unticked = 0

            if event.type == MOUSEBUTTONDOWN:
                for j,slider in enumerate(slider_buttons):
                    if slider.isOver(mouse_pos):
                        if reverse_button_filled == -1:
                            run_forward_game(j+2)
                        else:
                            run_backward_game(j+2)

                if reverse_button2.isOver(mouse_pos):
                    if reverse_button_filled == 1:
                        reverse_button_filled = -1
                        reverse_button_hovered = False
                        just_unticked = 1
                    else:
                        reverse_button_filled = 1

        ### Calculations ###

        ## Drawing ###

        button_1.draw(screen)
        button_1.draw_text(screen)

        for slider in slider_buttons:
            slider.draw(screen)

        for j,bool in enumerate(is_over_sliders):
            if bool:
                slider_buttons[j].draw_text(screen,color=((10,150,255)))
            else:
                slider_buttons[j].draw_text(screen)

        

        reverse_button1.draw(screen)
        reverse_button1.draw_text(screen,color= REV_TEXT_COLOR)

        reverse_button2.draw(screen)

        if reverse_button_hovered or reverse_button_filled == 1:
            screen.blit(tick_pic, (1100,580))
        
        
        button_header.draw(screen)
        button_header.draw_text(screen,color=(10,200,255),size = 70)



        ### Rendering ###
        clock.tick(60)
        pygame.display.update()

#run_choose_N()