# Modules that are being imported
import pygame
from assets.variables import *
def TextInput():
    '''Function for taking in text input
    by a custom method throughout program'''
    global user_text

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    return user_text

def update():
    '''Function to update input to text
    entered through TextInput function'''
    global user_text
    user_text = ''

