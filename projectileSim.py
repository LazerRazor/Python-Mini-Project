import pygame
import pymunk
import pymunk.pygame_util
import math
# Importing required modules.

pygame.init()

WIDTH, HEIGHT = 1000, 750   # Setting window width and height.
window = pygame.display.set_mode((WIDTH, HEIGHT))   # Creating window.

def draw(space, window, draw_options):
    '''Defines draw function which updates
    pygame display repetitively.'''
    window.fill("white")    # Makes complete window white in colour.
    space.debug_draw(draw_options)
    pygame.display.update()

def calculate_distance(p1, p2):
    '''Defines function to calculate distance
    between initial and final mouse positions.'''
    return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)

def calculate_angle(p1, p2):
    '''Defines function to calculate angle
    between initial and final mouse positions.'''
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def create_walls(space, width, height):
    '''Function to create walls that keep the 
    pymunk object from crossing out of the window.'''
    rects = [
        [(width/2, height-10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width-10, height/2), (20, height)]
    ]   # Wall rects widths and heights.

    for pos, size in rects: # Making wall rect objects static.
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

def create_ball(space, radius, mass, pos):
    '''Function to create ball of given mass
    and radius at mouse position.'''
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)
    shape.elasticity = 0.9
    shape.friction = 0.4
    space.add(body, shape)
    return shape

def run(window, width, height):
    '''Run function to run the pymunk simulation
    until pygame.quit event is encountered.'''
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps

    space = pymunk.Space()
    space.gravity = (0, 981)    # Declaring gravity value

    walls = create_walls(space, WIDTH, HEIGHT)  # Creating walls

    draw_options = pymunk.pygame_util.DrawOptions(window)

    pressed_pos = None
    ball = None

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Quitting while loop if 'X' clicked.
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pressed_pos = pygame.mouse.get_pos()
                    ball = create_ball(space, 30, 10, pressed_pos)  # Creating ball at given position.
                elif pressed_pos:
                    ball.body.apply_impulse_at_local_point((10000,0),(0,0)) # Applying force to center of ball created.
                    pressed_pos = None
                else:
                    space.remove(ball, ball.body)
                    ball = None 

        draw(space, window, draw_options)   # Updating pygame window 60 times each second.
        space.step(dt)
        clock.tick(fps)

    pygame.quit()   # Quitting pygame program

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)