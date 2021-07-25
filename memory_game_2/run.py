import main_menu
from buttons import button
import pygame
import sys
from pygame.locals import *
import logging
pygame.init()

try:    
    main_menu.main_menu()
except Exception as ex:
    logging.exception('caught an error')
    x = input('Press enter to close')