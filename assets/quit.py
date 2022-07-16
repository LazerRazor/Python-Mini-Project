# Modules that are being imported
import pygame

def exitButton():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()