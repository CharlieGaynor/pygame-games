import pygame 
import os

class button():
    def __init__(self, x,y,width,height, color=(38,38,38), text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=(255,255,255),draw_outline=True):
        '''
        Draws a button on the screen, with or without an outline depending on arguments
        '''
        if draw_outline:

            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        else:
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

    def draw_text(self,win, color=(255,255,255),size=50):

        '''
        Draws text on the button (button doesn't need to be drawn though).
        '''
        if self.text != '':
            font = pygame.font.SysFont('comicsans', size)
            text = font.render(self.text, 1, color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        '''
        Returns a bool, for whether the mouse is over the (rectangular) button.
        Pos is the mouse position or a tuple of (x,y) coordinates
        '''
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

    

def get_path(filename):
    '''
    Takes a file name, and returns its path - only for stuff in images folder.
    '''
    cwd = os.getcwd()
    images_folder = os.path.join(cwd, 'images')

    return os.path.join(images_folder, filename)