import pygame
from pygame import mouse
from pygame.locals import *
import sys
from buttons import button
from tic_tac_toe_board import board
from ai import q_strategy
import json
import os

pygame.init()
clock = pygame.time.Clock()




def play_ai_vs_human():

    with open('table_first.txt') as fobj:
        table1 = json.load(fobj)

    L_WIDTH = 14 #LINE WIDTH
    L_COLOR = (25,115,105) # LINE COLOR

    BUTTON_COLOR = (255,0,150)
    BG_COLOR = (20,170,155) # BACKGROUND COLOR
    BOX_COLOR = (130,0,155)

    WINDOW_SIZE = (1280,720)
    BG_SIZE = (600,600)

    BG_x = (WINDOW_SIZE[0]-BG_SIZE[0])/2
    BG_y = (WINDOW_SIZE[1]-BG_SIZE[1])/2

    cwd = os.getcwd()
    images_folder = os.path.join(cwd, 'images')

    def get_path(filename, images_folder = images_folder):
        '''
        Takes a file name, and returns its path.
        '''

        return os.path.join(images_folder, filename)


    background_1 = pygame.image.load(get_path('background_1.png'))
    naught = pygame.image.load(get_path('naught_2.png'))
    cross = pygame.image.load(get_path('cross.png'))
    button_2 = pygame.image.load(get_path('button_2.png'))

    screen = pygame.display.set_mode(WINDOW_SIZE)
    BG = pygame.Surface(BG_SIZE)
    BG.fill(BG_COLOR)
    def draw_lines(): #No arguments as everything is defined globally above

        #Horizontal lines
        pygame.draw.line(BG, L_COLOR, (200,0),(200,600), L_WIDTH)
        pygame.draw.line(BG, L_COLOR, (400,0),(400,600), L_WIDTH)

        #Vertical lines
        pygame.draw.line(BG, L_COLOR, (0,200),(600, 200), L_WIDTH)
        pygame.draw.line(BG, L_COLOR, (0,400), (600,400), L_WIDTH)
        
    button_positions = []
    for i in range(3):
        for j in range(3):
            button_positions.append((200*i + BG_x, 200*j + BG_y))

    def generate_buttons():

        buttons = []
        for pos in button_positions:
            buttons.append(button(color=BG_COLOR, x=pos[0], y=pos[1], width=199, height=199))

        return buttons

    buttons = generate_buttons()
    play_again_button = button(BUTTON_COLOR,x=990,y=430,height=200, width= 250,text='Play again?')
    main_menu_button = button(BUTTON_COLOR, x=50, y=130, height= 200, width=250,text='Main menu')
    quit_button = button(BUTTON_COLOR, x=50, y=430, height= 200, width=250,text='Quit')
    winner_button = button(BOX_COLOR, x=50, y=130, height= 200, width=250,text='Player 1 wins')

    menu_button_positions = ((50,130),(50,430),(990,130),(990,430))

    show_naughts = [False for i in range(9)]
    show_crosses = [False for i in range(9)]

    is_filled = [0 for i in range(9)] #0 means empty, 1 means naught, -1 means cross

    player_turn = -1

    game_board = board()

    is_draw = False
    game_state = 0
    show_play_again = 0

    ai_turn = 1

    bot = q_strategy(table1)
    ai_timer = 0

    button_1_over = False
    button_2_over = False
    button_3_over = False

    while True:

        mouse_pos = pygame.mouse.get_pos()
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if game_state == 0 and not is_draw and ai_turn != 1:
                if event.type == MOUSEBUTTONDOWN:
                    for j,butt in enumerate(buttons):
                        if butt.isOver(mouse_pos):
                            if is_filled[j] == 0:
                                is_filled[j] = player_turn
                                game_board.update_board(j%3,j//3,player_turn)
                                ai_turn *= -1

                                game_state = game_board.get_winner(j%3,j//3)
                                if not game_board.still_playing() and game_state ==0:
                                    is_draw = True

                    
                    
                
                if event.type == MOUSEMOTION: #problem
                    for j,butt in enumerate(buttons):
                        if butt.isOver(mouse_pos):
                            if player_turn == 1:
                                show_naughts[j] = True   
                            else:
                                show_crosses[j]= True
                        else:
                            show_crosses[j] = False
                            show_naughts[j] = False
                
            if ai_turn == 1 and game_state==0 and is_draw != 1:
                actions = game_board.get_valid_actions()
                move = bot.SelectMove(game_board, actions, 1)
                game_board.update_board(*move,1)
                pos_selected = move[0] +move[1]*3
                is_filled[pos_selected] = 1
                ai_turn *=-1

                game_state = game_board.get_winner(pos_selected %3,pos_selected //3)

                if not game_board.still_playing() and game_state ==0:
                    is_draw = True

            if game_state !=0 or is_draw == 1:
                show_play_again = 1
                if game_state == 1:
                    winner_button = button(BOX_COLOR, x=990,y=130,height=200, width= 250,text='Player 1 wins!')
                if game_state == -1:
                    winner_button = button(BOX_COLOR, x=990, y=130, height= 200, width=250,text='Player 2 wins!')
                if is_draw:
                    winner_button = button(BOX_COLOR, x=990, y=130, height= 200, width=250,text='It\'s a draw!')
                if event.type == MOUSEBUTTONDOWN:
                    if play_again_button.isOver(mouse_pos):
                        game_state = 0
                        game_board.ResetBoard()
                        show_naughts = [False for i in range(9)]
                        show_crosses = [False for i in range(9)]
                        is_filled = [0 for i in range(9)]
                        show_play_again = 0
                        is_draw = False
                        ai_turn = 1
            
            if event.type == MOUSEBUTTONDOWN:
                if main_menu_button.isOver(mouse_pos):
                    return #could try changing this
                if quit_button.isOver(mouse_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEMOTION:
                if main_menu_button.isOver(mouse_pos):
                    button_1_over = True
                else:
                    button_1_over = False
                if quit_button.isOver(mouse_pos):
                    button_2_over = True
                else:
                    button_2_over = False
                if play_again_button.isOver(mouse_pos):
                    button_3_over = True
                else:
                    button_3_over = False

        ###Drawing###
        
        screen.blit(background_1,(0,0))
        for butt in buttons:
            butt.draw(screen)
        screen.blit(BG,(BG_x,BG_y))

        for j in range(9):
            if show_naughts[j] and not is_filled[j]:
                screen.blit(naught, button_positions[j])
            if show_crosses[j] and not is_filled[j]:
                screen.blit(cross, button_positions[j])

        for j,value in enumerate(is_filled):
            if value == 1:
                screen.blit(naught, button_positions[j])
            elif value == -1:
                screen.blit(cross, button_positions[j])


        draw_lines()

        if show_play_again:
            play_again_button.draw(screen)
            screen.blit(button_2, menu_button_positions[-1])
            if button_3_over:
                play_again_button.draw_text(screen,color=(10,150,255))
            else:
                play_again_button.draw_text(screen)
            winner_button.draw(screen)
            screen.blit(button_2, menu_button_positions[2])
            winner_button.draw_text(screen)
        
        ###Final updates

        ###Final updates
        main_menu_button.draw(screen) #Only useful for outline now
        quit_button.draw(screen)

        for pos in menu_button_positions[:2]:
            screen.blit(button_2, pos)

        if button_2_over:
            quit_button.draw_text(screen,color=(10,150,255))
        else:
            quit_button.draw_text(screen)
        if button_1_over:
            main_menu_button.draw_text(screen,color=(10,150,255))
        else:
            main_menu_button.draw_text(screen)

        clock.tick(60)
        pygame.display.update()