#modules that are being imported
from assets.buttonObjects import *
from assets.modules import *
from assets.variables import *
from backend.projectileSim import *
from assets.rectangle import *

matplotlib.use("Agg")
ss = SystemElements()
pygame.init()

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('The Ultimate Mechanics Simulator')

font = pygame.font.SysFont('rockwell', 64)
text = font.render('Mechanics Simulator', True, col.green)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 4)

rectbox1 = Rectangle(workspacelength+10,10,(45,40),col.purple)
rectbox2 = Rectangle(workspacelength+10,10,(45,50+workspacewidth),col.purple)
rectbox3 = Rectangle(10,workspacewidth+10,(40,45),col.purple)
rectbox4 = Rectangle(10,workspacewidth+10,(50+workspacelength,45),col.purple)

fig = pylab.figure(figsize=[4, 4],dpi=1000)
ax = fig.gca()

def StructureUpdate(RR):
            global Count

            if RR == 0:
                fig = ss.show_structure(show=False)
            elif RR == 1:
                fig = ss.show_bending_moment(show=False)
                pass
            elif RR == 2:
                 fig = ss.show_shear_force(show=False)
            elif RR == 3:
                 fig = ss.show_reaction_force(show=False)
            elif RR == 4:
                fig = ss.show_displacement(show=False)

            canvas = agg.FigureCanvasAgg(fig)
            canvas.draw()
            renderer = canvas.get_renderer()
            raw_data = renderer.tostring_rgb()
            size = canvas.get_width_height()
            surf = pygame.image.fromstring(raw_data, size, "RGB")
            surf = pygame.transform.scale(surf, (700, 600))
            Count+=1


def KinematicsUpdate():
    pass


while True:
    screen.fill(col.purple)
    Q.exitButton()

    if Menu:
        screen.blit(text, textRect)
        button1.draw()
        button2.draw()
        if button1.check_click(): Menu, Moment = False, True
        if button2.check_click(): Menu, Kinematics = False, True