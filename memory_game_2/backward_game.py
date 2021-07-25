import pygame
from pygame import display
from pygame import surface
from pygame import draw 
from pygame.locals import *
import os
import sys
from buttons import button
import random
from buttons import get_path
import copy 
import pandas as pd
from datetime import date,datetime
#from choose_N import run_choose_N

def run_backward_game(starting_number=0):

    
    
    #### This bit is for logging results
    try:
        df = pd.read_csv('memory_game_stats.csv',index_col = 'Entry')
    except:
        df = pd.DataFrame(columns=['Date','Sequence length','is_backwards','is_completed','streak_so_far','Time'])

    time = datetime.now().time()
    now = time.strftime("%H")
    
    today = date.today()

    d1 = today.strftime("%d/%m/%Y") ## dd/mm/YY

    ########## end of logging ########


    N = starting_number

    pygame.init()
    clock = pygame.time.Clock()

    WINDOW_SIZE = (1280,720)
    SURFACE_SIZE = (600,400)

    display = pygame.display.set_mode(WINDOW_SIZE)
    screen = pygame.Surface(SURFACE_SIZE)

    background_img = pygame.image.load('background_1.png')

    back_text_color = pAgain_color = wrong = show_feedback = need_input = draw_end_button = draw_button_1 = draw_input = draw_msg = show_pAgain = False
    tick = 0
    message_number = 0
    numbers_shown = 1 
    confirmed_input = None
    needs_logging = True
    sequence = []
    first_time = 1

    input = None

    def get_messages(N):
        msg1 = f'{N} numbers, backwards'
        msg2 = 'Here we go:'
        return [msg1,msg2]

    def Reverse(lst): 
        return [element for element in reversed(lst)] 

    number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]

    back_button = button(
        x= 50, y= 63, width = 250,height= 80, text= 'Back'
    )

    while True:

        tick += 1
        mouse_pos = pygame.mouse.get_pos()

        display.blit(background_img,(0,0))
        screen.fill((205,105,35)) #surface background color

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    df.to_csv('memory_game_stats.csv',index_label='Entry')
                    pygame.quit()
                    sys.exit()
            if event.type == QUIT:
                df.to_csv('memory_game_stats.csv',index_label='Entry')
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if need_input:

                    for num, key in enumerate(number_keys):
                        if event.key == key:
                            if input is None:
                                input = str(num)
                            else:
                                input += str(num)
                            input = str(input)

                    if event.key == K_RETURN:
                        if need_input and not wrong:
                            try:
                                confirmed_input = copy.copy(list(input))
                                sequence = Reverse(sequence[:-1])
                            except TypeError: #incase enter is pressed without input
                                pass              
                            tick = 0

                    if event.key == K_BACKSPACE:
                        input = input[:-1]
            
            if show_pAgain:
                if event.type == MOUSEBUTTONDOWN:
                    if pAgain_button.isOver(mouse_pos):
                        return
                        '''show_feedback = need_input = draw_end_button = draw_button_1 = draw_input = draw_msg = show_pAgain = False
                        tick = 0
                        message_number = 0
                        numbers_shown = 1 
                        is_right = confirmed_input = None
                        sequence = []
                        N = 3'''

                if event.type == MOUSEMOTION:
                    if pAgain_button.isOver(mouse_pos): 
                        pAgain_color = True
                    else:
                        pAgain_color = False
            
            if event.type == MOUSEBUTTONDOWN:
                if back_button.isOver(mouse_pos):
                    df.to_csv('memory_game_stats.csv',index_label='Entry')
                    return

            if event.type == MOUSEMOTION:
                if back_button.isOver(mouse_pos):
                    back_text_color = True    
                else:
                    back_text_color = False

        ##Calculating       


        if not need_input:

            if tick%80 ==1 and message_number <=1:

                msg = get_messages(N)[message_number]
                msg_button = button(x=SURFACE_SIZE[0]/2,
                            y=SURFACE_SIZE[1]/2,width=1,height=1,text=msg)
                draw_msg= True
                message_number +=1

            if tick%80 == 0 and message_number == 2:
                    draw_msg = False
                    tick = 80
                    message_number +=1

            if not draw_msg:

                if numbers_shown <= N+1:
                    if tick %100 == 1:
                        num = str(random.randint(0,9))
                        numbers_shown += 1
                        sequence.append(num)

                    if not(tick%100 >=80 or tick%100 <2):
                        button_1 = button(x=SURFACE_SIZE[0]/2,
                                    y=SURFACE_SIZE[1]/2,width=1,height=1,text=num)
                        draw_button_1 = True

                    if tick%100 >=80 or tick%100 <2:
                        draw_button_1 = False

                else:

                    end_button = button(x=SURFACE_SIZE[0]/2,
                            y=SURFACE_SIZE[1]/2-40,width=1,height=1,text='What did you see')
                    reverse_order_warning = button(x=SURFACE_SIZE[0]/2,
                            y=SURFACE_SIZE[1]/2+40,width=1,height=1,text='in reverse?')
                    draw_end_button = True
                    need_input = True

        if need_input:

            input_button = button(x = (1280-900)/2,
                        y= 550 ,width=900,height=100,text = input)
            draw_input = True

            if confirmed_input is not None:
                show_feedback = True
                draw_end_button = False

                if confirmed_input == sequence:
                    draw_input = False
                    feedback_button = button(x=SURFACE_SIZE[0]/2,
                        y=SURFACE_SIZE[1]/2,width=1,height=1,text='That\'s right!')
                    first_time = 0

                    if needs_logging:

                        df = df.append({'Date' : d1, 'Sequence length': N , 'is_backwards': 1,'is_completed' : 1,'streak_so_far' : N,'Time': now},ignore_index = True)
                        needs_logging = False

                    if tick%150 == 149:
                        N += 1
                        show_feedback = need_input = draw_end_button = draw_button_1 = draw_input = draw_msg = show_pAgain = False
                        tick = 0
                        message_number = 0
                        numbers_shown = 1 
                        confirmed_input = None
                        needs_logging = True
                        sequence = []
                        input = ''
                else:
                    wrong = True
                    feedback_button = button(x=SURFACE_SIZE[0]/2,
                        y=SURFACE_SIZE[1]/2-125,width=1,height=1,text='That\'s wrong, sorry u suck')

                    input_sequence = button(x=SURFACE_SIZE[0]/2,
                        y=SURFACE_SIZE[1]/2-40,width=1,height=1,text=f'{"".join(confirmed_input)}')
                    
                    true_sequence1 = button(x=SURFACE_SIZE[0]/2,
                        y=SURFACE_SIZE[1]/2 + 35,width=1,height=1,text='The reversed sequence was:')
                    true_sequence2 = button(x=SURFACE_SIZE[0]/2,
                        y=SURFACE_SIZE[1]/2+125,width=1,height=1,text=f'{"".join(sequence)}')
                    pAgain_button = button(x = (1280-900)/2,
                    y= 550 ,width=900,height=100,text = 'Play again?')
                    show_pAgain = True
                    draw_input = False
                    
                    if needs_logging:

                        if first_time == 1:
                            df = df.append({'Date' : d1, 'Sequence length': N , 'is_backwards': 1,'is_completed' : 0,'streak_so_far' : 0,'Time': now},ignore_index = True)
                            needs_logging = False
                        else:
                             df = df.append({'Date' : d1, 'Sequence length': N , 'is_backwards': 1,'is_completed' : 0,'streak_so_far' : N-1,'Time': now},ignore_index = True)
                             needs_logging = False
                
                    
        
        ##Drawing##

        back_button.draw(display)
        if back_text_color:
            back_button.draw_text(display,color=(10,150,255))
        else:
            back_button.draw_text(display)

        if show_pAgain:
            pAgain_button.draw(display)
            if pAgain_color:
                pAgain_button.draw_text(display,size=80,color=(10,150,255))
            else:
                pAgain_button.draw_text(display,size=80)


        if show_feedback:
            feedback_button.draw_text(screen)
            if wrong:
                input_sequence.draw_text(screen)
                true_sequence1.draw_text(screen,size=50)
                true_sequence2.draw_text(screen)

        if draw_msg:
            msg_button.draw_text(screen,size=60)

        if draw_end_button:
            end_button.draw_text(screen, size= 70)
            reverse_order_warning.draw_text(screen, size = 70)

        if draw_button_1:
            button_1.draw_text(screen,size=200)

        if draw_input:
            input_button.draw(display)
            input_button.draw_text(display)

        display.blit(screen,
            ((WINDOW_SIZE[0]-SURFACE_SIZE[0])/2,
            (WINDOW_SIZE[1]-SURFACE_SIZE[1])/2 - 100)
            )

        clock.tick(60)
        pygame.display.update()

#run_backward_game(3)