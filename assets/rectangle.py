# Modules that are being imported
import os, pygame, sys, assets.colors as c
from pygame.locals import *
pygame.init()

gui_font = pygame.font.SysFont('ubuntu',30)
WIN = pygame.display.set_mode((1280, 720))

class Rectangle:
    '''Class for creating rectangles
    with border radius throughout program'''
    def __init__(self,width,height,pos ,bgcolor):  #creating class button and listing arguments
        #top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (bgcolor)     

    def draw(self):
        '''draw function of class button'''
        pygame.draw.rect(WIN,self.top_color,self.top_rect,border_radius = 20)
        