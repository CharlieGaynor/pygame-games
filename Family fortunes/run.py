import pygame
from pygame import display
from pygame import surface
from pygame import draw 
from pygame.locals import *
from buttons import button
from pygame import mixer
import os
import sys

def main():

    pygame.init()
    clock = pygame.time.Clock()
    mixer.init()



    WINDOW_SIZE = (1920,1080)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = Rect(0,0,1920,1080)
    cross = pygame.image.load('cross.png')
    reset_button = button(3,3,200,50,text='Reset')
    

    option_buttons = []
    letters = ['A','B','C','D','E']
    for i in range(5):
        temp_button = button(200 + 360*i,1000,150,50,text=f'{letters[i]}')
        option_buttons.append(temp_button)

    word_set = [['Bathroom','Baby','Bad dream','Noise','Temperature','Hunger','In the mood'],
    ['Soap','Vinegar','Cooking oil','Soy Sauce','Sink juice',' ',' '],
    ['Head','Stomach','Back','Tooth','Muscle','Knee','Ear'],
    ["She's a bad cook","Doesn't like in-laws","Doesn't like wife's friends","Adult content habits","In debt","Checked out another woman","Quit job","Kid is ugly"],
    ['Poo/Pee in public','Humping','Licking stangers','Barking','Head out of car window','',' ']]
    point_set =[[24,19,16,13,12,6,6],[46,30,16,4,2,0,0],[34,33,11,7,6,3,2],[26,22,27,10,5,4,4,3],[33,23,18,14,2,0,0]]

    which_game = 0 
    crosses_l = 0

    l_cross = [False,False,False]
    r_cross = [False,False,False]
    crosses_r = 0

    buzzer = pygame.mixer.Sound('buzzer.mp3')
    right = pygame.mixer.Sound('right.mp3')
    draw_words = [False for i in range(7)]
    
    global words
    global point_buttons

    words = [0 for i in range(7)]
    point_buttons = [0 for i in range(7)]


    def update_words(word_set=word_set,position=0,replace_all=False):
        if replace_all:
            for i in range(7):
                button1 = button(550, 73+90*i, 800, 60,text=f' ')
                words[i] = button1
        else:
            i = position
            try:
                button1 = button(550, 73+90*i, 800, 60,text=f'{word_set[which_game][i]}')
            except IndexError:
                pass
            words[i] = button1
        return

    def update_points(point_set = point_set,position=0,replace_all=False):
        if replace_all:
            for i in range(7):
                button1 = button(1400, 73+90*i, 60, 60,text=f' ')
                point_buttons[i] = button1
        else:
            i = position
            try:
                button1 = button(1400, 73+90*i, 60, 60,text=f'{point_set[which_game][i]}')
            except IndexError:
                pass
            point_buttons[i] = button1
        return

    update_words(word_set,replace_all=True)
    update_points(point_set,replace_all=True)

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
                for i in range(5):
                    if option_buttons[i].isOver(mouse_pos):
                        which_game = i
                        update_words(word_set,replace_all=True)
                        update_points(point_set,replace_all=True)
                        crosses_l = 0
                        l_cross = [False,False,False]
                        r_cross = [False,False,False]
                        crosses_r = 0

            if event.type == KEYDOWN:
                if event.key == K_x:
                    pygame.mixer.Channel(1).set_volume(1)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(buzzer))
                    if crosses_l == 3:
                        pass
                    else:
                        l_cross[ crosses_l] = True
                        crosses_l +=1
                if event.key == K_v:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(buzzer))
                    if crosses_r == 3:
                        pass
                    else:
                        r_cross[ crosses_r] = True
                        crosses_r+=1
                if event.key == K_1:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(right))
                    draw_words[0] = True
                    update_words(position=0)
                    update_points(position=0)
                if event.key == K_2:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(right))
                    draw_words[1] = True
                    update_words(position=1)
                    update_points(position=1)
                if event.key == K_3:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(right))
                    draw_words[2] = True
                    update_words(position=2)
                    update_points(position=2)
                if event.key == K_4:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(right))
                    draw_words[3] = True
                    update_words(position=3)
                    update_points(position=3)
                if event.key == K_5:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(right))
                    draw_words[4] = True
                    update_words(position=4)
                    update_points(position=4)
                if event.key == K_6:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(right))
                    draw_words[5] = True
                    update_words(position=5)
                    update_points(position=5)
                if event.key == K_7:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(right))
                    draw_words[6] = True
                    update_words(position=6)
                    update_points(position=6)
                    
                

        #####Calculations####
        

        ####Drawing####
        pygame.draw.rect(screen,(120,80,50),rect=background)

        for button_ in option_buttons:
            button_.draw_wtext(screen,draw_outline = False)

        #Numbers

        for i in range(7):
            pygame.draw.circle(screen, (255,255,255), (450,100+90*i), 32)
            pygame.draw.circle(screen, (100,178,255), (450,100+90*i), 30)
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(f'{i+1}', 1, (255,255,255))
            screen.blit(text,(441,85+90*i))

            pygame.draw.rect(screen, (255,255,255), pygame.Rect(547, 70+90*i, 806, 66),  0, 13) #outline
            pygame.draw.rect(screen, (100,178,255), pygame.Rect(550, 73+90*i, 800, 60),  0, 13)
            
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(1397, 70+90*i, 66, 66),  0, 13) #outline
            pygame.draw.rect(screen, (100,178,255), pygame.Rect(1400, 73+90*i, 60, 60),  0, 13) #real thing
        
        
        for i in range(len(l_cross)):
            if l_cross[i]:
                screen.blit(cross,(100,100+200*i))
            if r_cross[i]:
                screen.blit(cross,(1600,100+200*i))


        for j in range(7):
            words[j].draw_text(screen)
            point_buttons[j].draw_text(screen)


        clock.tick(60)
        pygame.display.update()

main()