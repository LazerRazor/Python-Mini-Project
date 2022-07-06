import os, pygame, sys, assets.colors as c
from pygame.locals import *
pygame.init()

gui_font = pygame.font.SysFont('ubuntu',30)
WIN = pygame.display.set_mode((1280, 720))

class Button:
    def __init__(self,text,width,height,pos ,textcolor, buttoncolor = c.green, hover = True):  #creating class button and listing arguments
        #core attributes
        self.pressed = False
        self.hover = hover
        #top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = buttoncolor
        self.bg_color = buttoncolor
        #text
        self.text = text
        self.text_col = textcolor
        self.text_surf = gui_font.render(self.text,True,textcolor)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(WIN,self.top_color,self.top_rect,border_radius = 12)
        WIN.blit(self.text_surf,self.text_rect)
        self.check_click()

    def updateText(self,text):
        self.text = text
        self.text_surf = gui_font.render(text,True,self.text_col)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

        
    def check_click(self): 
  
        mouse_pos = pygame.mouse.get_pos()  
        if self.top_rect.collidepoint(mouse_pos):
            if self.hover:
                self.top_color = c.hovergreen
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            self.top_color = self.bg_color


    def hover(self):
         mouse_pos = pygame.mouse.get_pos()  
         if self.top_rect.collidepoint(mouse_pos):
             return True
         else: return False
