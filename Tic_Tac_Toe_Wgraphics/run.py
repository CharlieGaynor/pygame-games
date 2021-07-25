import menu
from buttons import button
import pygame
import sys
from pygame.locals import *
import logging
import time
pygame.init()

try:    
    menu.main_menu()
except Exception as ex:
    logging.exception('caught an error')
    x = input('press Enter to close')