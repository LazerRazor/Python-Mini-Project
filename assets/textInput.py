import pygame
from assets.variables import *
def TextInput():
            global user_text

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode

            return user_text

def update():
    global user_text
    user_text = ''

