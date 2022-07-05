import pygame, sys
import os
from pygame.locals import *

GREEN = (0,225,0)
BLACK = (0,0,0)
DARK_GREEN = (208, 240, 192)

class Button:
    def __init__(self,text,width,height,pos):  #creating class button and listing arguments
        #core attributes
        self.pressed = False
        
        #top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (GREEN)

        #text
        self.text_surf = gui_font.render(text,True,BLACK)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(WIN,self.top_color,self.top_rect,border_radius = 12)
        WIN.blit(self.text_surf,self.text_rect)
        self.check_click()
        
    def check_click(self): 
        mouse_pos = pygame.mouse.get_pos()  
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = DARK_GREEN
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                return True
            else:
                if self.pressed == True:
                    print('click')
                    self.pressed = False
                    return True

        else:
            self.top_color = GREEN
        
                    
pygame.init()
WIDTH,HEIGHT = 1280,720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mechanics Simulator")
gui_font = pygame.font.Font(None,30)

button1 = Button('MOMENT AND FORCES',300,80,(490,320))
button2 = Button('KINEMATICS',300,80,(490,440))


VIOLET = (94, 23, 235) #Purple RGB

FPS = 60
a = True
b = False

def main():
        global a,b
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            if a: 
                for event in pygame.event.get():#Handling quit
                    if event.type == pygame.QUIT:
                        run = False

                WIN.fill(VIOLET)
                button1.draw()
                button2.draw()
                if button1.check_click():
                    a = False
                pygame.display.update()

            else:
                for event in pygame.event.get():#Handling quit
                    if event.type == pygame.QUIT:
                        run = False

                WIN.fill(VIOLET)
                button2.draw()
                if button2.check_click():
                    a = True
                pygame.display.update()


        pygame.quit()          



       


if __name__ == "__main__":
    main()


