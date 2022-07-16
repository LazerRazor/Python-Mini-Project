# Modules that are being imported
import pygame
import pymunk
import pymunk.pygame_util
import math
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from assets.buttonObjects import *

# Declaring rectangle object and surface objects for use.
s1 = Rectangle(720, 600, (60,60), col.white)
surf1 = pygame.Surface((740,620))
s = pygame.display.get_surface()

def create_walls(space):
    '''Function for creating static walls
    to enclose pymunk simulation'''
    rects1 = [
        [(60, 360), (14, 600)],
        [(780, 360), (14, 600)],
        [(420, 60), (720, 14)],
    ]
    rects2 = [
        [(420, 660), (720, 15)]
    ]

    for pos, size in rects1:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.0
        shape.friction = 50.0
        shape.color = (255,255,255,255)
        space.add(body, shape)
    for pos, size in rects2:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.0
        shape.friction = 50.0
        shape.color = (0,0,0,255)
        space.add(body, shape)

def draw(space, rect, draw_options):
    '''Function for updating each frame
    of the pymunk simulation'''
    s.fill("white", s1.top_rect)
    space.debug_draw(draw_options)
    pygame.display.update()

def create_ball(space, radius, mass, pos):
    '''Function for creating the object/ball
    that would be the projectile in the simulation'''
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)
    shape.elasticity = 0
    shape.friction = 50.0
    space.add(body, shape)
    return shape

def run(window,angleinput,velinput):
    '''Function for running the pymunk
    simulation, calling all other functions'''
    run = True
    clock = pygame.time.Clock()
    fps = 120
    dt = 1/fps

    space = pymunk.Space()
    space.gravity = (0, 981)

    walls = create_walls(space)

    draw_options = pymunk.pygame_util.DrawOptions(window)
    running = True
    newinput = 0

    while run:
        if BackButton.check_click():
            run = False
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if (running==True):
                radiusinput =  15
                massinput = 20
                ball = create_ball(space, radiusinput, massinput, (90,650))
                newinput = 1
                running = False

            elif newinput == 1:
                ball.body.apply_impulse_at_local_point(((massinput*velinput*100*math.cos(math.radians(angleinput))),-(massinput*velinput*100*math.sin(math.radians(angleinput)))),(0,0))
                newinput = 0

        draw(space, surf1, draw_options)
        space.step(dt)
        clock.tick(fps)
