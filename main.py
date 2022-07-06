#modules that are being imported
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


workspacelength = 740
workspacewidth = 620
rect1 = Rectangle(740,620,(50,50),col.white)
rect2 = Rectangle(400,470,(840,50),col.white)
rectbox1 = Rectangle(workspacelength+10,10,(45,40),col.purple)
rectbox2 = Rectangle(workspacelength+10,10,(45,50+workspacewidth),col.purple)
rectbox3 = Rectangle(10,workspacewidth+10,(40,45),col.purple)
rectbox4 = Rectangle(10,workspacewidth+10,(50+workspacelength,45),col.purple)
li = ['Go Back','X']


while True:
    screen.fill(col.purple)
    Q.exitButton()

    if Menu:
        screen.blit(text, textRect)
        button1.draw()
        button2.draw()

        if button1.check_click(): Menu, Moment = False, True
        if button2.check_click(): Menu, Kinematics = False, True

    if Moment:

        rect1.draw();
  
        if StructureExists: 
            fig = pylab.figure(figsize=[4, 4], # Inches
                   dpi=1000,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
            ax = fig.gca()
            if RR == 0:
                fig = ss.show_structure(show=False)
            elif RR == 1:
                # fig = ss.show_bending_moment(show=False)
                pass
            elif RR == 2:
                 fig = ss.show_shear_force(show=False)
            elif RR == 3:
                 fig = ss.show_reaction_force(show=False)
            elif RR == 4:
                # fig = ss.show_displacement(show=False)
                pass


            canvas = agg.FigureCanvasAgg(fig)
            canvas.draw()
            renderer = canvas.get_renderer()
            raw_data = renderer.tostring_rgb()
            size = canvas.get_width_height()
            surf = pygame.image.fromstring(raw_data, size, "RGB")
            surf = pygame.transform.scale(surf, (700, 600))
            screen.blit(surf, (60,60))
            StructureExists = False
            Count+=1
            RR = 0

        if(Count):
            screen.blit(surf, (60,60))

        if MomDefault:
            count+=1
            ElementButton.draw()
            MomentButton.draw()
            ForceButton.draw()
            SolutionButton.draw()
            BackButton.draw()

            if BackButton.check_click() and BackButton.text == 'Go Back' and count>30:
                Menu, Moment = True, False
        
            if ElementButton.check_click(): 
                MomElement, MomMoment, MomDefault, MomForce, Solve = True,  False, False, False, False
                ind^=1
                BackButton.updateText(li[ind])

            if MomentButton.check_click(): 
                ind^=1
                BackButton.updateText(li[ind])
                MomMoment, MomDefault, MomElement, MomForce, Solve = True, False, False, False, False

            if ForceButton.check_click(): 
                ind^=1
                BackButton.updateText(li[ind])
                MomForce, MomDefault, MomElement, MomMoment, Solve = True, False, False, False, False

            if SolutionButton.check_click():
                ind^=1
                BackButton.updateText(li[ind])
                MomForce, MomDefault, MomElement, MomMoment,Solve = False, False, False, False, True

        if MomForce:

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode
            
            BackButton.draw()
            rect2.draw()
            TextButtonLarge.draw()
            TextButtonLarge2.draw()
            TextNew2.draw()
            TextNew3.draw()
            SubmitCor3.draw()

            if TextButtonLarge.check_click():
                user_text = ''
                NodeCheck = True

            if TextButtonLarge2.check_click():
                user_text = ''
                NodeCheck = False

            if NodeCheck:
                TextButtonLarge.updateText(user_text)

            else:
                TextButtonLarge2.updateText(user_text)

            if SubmitCor3.check_click():
                node = int(TextButtonLarge.text)
                force = int(TextButtonLarge2.text)
                ss.q_load(element_id=node,q=force)
                StructureExists = True



            if BackButton.check_click():
                count = 0
                ind^=1
                BackButton.updateText(li[ind])
                MomForce, MomDefault = False, True

        if MomMoment:

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode
            
            BackButton.draw()
            rect2.draw()
            TextButtonLarge.draw()
            TextNew2.draw()
            SubmitCor2.draw()

            if TextButtonLarge.check_click():
                user_text = ''
            
            TextButtonLarge.updateText(user_text)

            if SubmitCor2.check_click():
                node = int(TextButtonLarge.text)
                ss.add_support_hinged(node_id=node)
                StructureExists = True


            if BackButton.check_click():
                count = 0
                ind^=1
                BackButton.updateText(li[ind])
                MomMoment, MomDefault = False, True
                user_text = ''

        if MomElement: 

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode

                    if x1:
                        TextButton1.updateText(user_text)

                    if y1:
                        TextButton2.updateText(user_text)

                    if x2:
                         TextButton3.updateText(user_text)

                    if y2:
                        TextButton4.updateText(user_text)

            BackButton.draw()
            rect2.draw()
            TextButton1.draw()
            TextButton2.draw()
            TextButton3.draw()
            TextButton4.draw()
            TextNew.draw()
            TextNew1.draw()
            SubmitCor.draw()

            if TextButton1.check_click():
                user_text = ''
                x1,x2,y1,y2 = True, False, False, False

            if TextButton2.check_click():
                user_text = ''
                x1,x2,y1,y2 = False, False, True, False


            if TextButton3.check_click():
                user_text = ''
                x1,x2,y1,y2 = False, True, False, False

            if TextButton4.check_click():
                user_text = ''
                x1,x2,y1,y2 = False, False, False, True

            if BackButton.check_click():
                count = 0
                ind^=1
                BackButton.updateText(li[ind])
                MomElement, MomDefault = False, True



            if SubmitCor.check_click():
                X1 = int(TextButton1.text)
                Y1 = int(TextButton2.text)
                X2 = int(TextButton3.text)
                Y2 = int(TextButton4.text)
                ss.add_element(location=[[X1, Y1], [X2, Y2]])
                StructureExists = True

        if Solve:
            CalcMomButton.draw()
            CalcShearButton.draw()
            CalcReactButton.draw()
            CalcDispButton.draw()
            BackButton.draw()

            if CalcMomButton.check_click():
                RR = 1
                StructureExists = True


            if CalcShearButton.check_click():
                RR = 2
                StructureExists = True

            if CalcReactButton.check_click():
                RR = 3
                StructureExists = True
                
            if CalcDispButton.check_click():
                RR = 4
                StructureExists = True
                
            if BackButton.check_click():
                count = 0
                ind^=1
                BackButton.updateText(li[ind])
                Solve, MomDefault = False, True

    if Kinematics:

        rect1.draw();
  
        if KinDefault:
            count+=1
            ProjectileButton.draw()
            VariableButton.draw()
            ProjectileSimulateButton.draw()
            BackButton.draw()

            if BackButton.check_click() and BackButton.text == 'Go Back' and count>30:
                Menu, Kinematics = True, False

            if ProjectileButton.check_click():
                ind^=1
                BackButton.updateText(li[ind])
                KinDefault,KinProjectile,KinVariable,KinProjectileSim = False, True, False, False

            if VariableButton.check_click():
                ind^=1
                BackButton.updateText(li[ind])
                KinDefault,KinProjectile,KinVariable,KinProjectileSim = False, False, True, False

            if ProjectileSimulateButton.check_click():
                ind^=1
                BackButton.updateText(li[ind])
                KinDefault,KinProjectile,KinVariable,KinProjectileSim = False, False, False, True

        if KinProjectile:

            if ShowProjectile:
                BackButton.draw()

                fig = pylab.figure(figsize=[4, 4], # Inches
                   dpi=1000,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
                ax = fig.gca()
                projectile.Path()
                ProjectilePeriod1.updateText(f'{round(projectile.Period(),2)} seconds')
                ProjectileHigh1.updateText(f'{round(projectile.HighestPoint(),2)} metres')
                ProjectileHorizontal1.updateText(f'{round(projectile.Distance(),2)} metres')
                canvas = agg.FigureCanvasAgg(fig)
                canvas.draw()
                renderer = canvas.get_renderer()
                raw_data = renderer.tostring_rgb()
                size = canvas.get_width_height()
                surf = pygame.image.fromstring(raw_data, size, "RGB")
                surf = pygame.transform.scale(surf, (700, 600))
                Solution = True
                Count+=1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                if BackButton.check_click():
                    count = 0
                    Solution = False
                    ShowProjectile = False
                    user_text = ''


            if Solution:
                rect2.draw()
                ProjectilePeriod.draw()
                ProjectileHigh.draw()
                ProjectileHorizontal.draw()
                ProjectilePeriod1.draw()
                ProjectileHigh1.draw()
                ProjectileHorizontal1.draw()

            else:
                BackButton.draw()
                rect2.draw()
                TextButtonLarge.draw()
                TextButtonLarge2.draw()
                ProjectileText1.draw()
                ProjectileText2.draw()
                KinematicsSubmit.draw()

            if(Count):
                screen.blit(surf, (80,60))


            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode

                    if NodeCheck:
                        TextButtonLarge.updateText(user_text)

                    else:
                        TextButtonLarge2.updateText(user_text)
            

            if TextButtonLarge.check_click():
                user_text = ''
                NodeCheck = True

            if TextButtonLarge2.check_click():
                user_text = ''
                NodeCheck = False

            if KinematicsSubmit.check_click():
                Theta = TextButtonLarge2.text
                Initial = TextButtonLarge.text
                projectile = Projectile(Theta, Initial)
                ShowProjectile = True


            if BackButton.check_click():
                count = 0
                ind^=1
                BackButton.updateText(li[ind])
                ShowProjectile = False
                Solution = False
                rect1.draw()
                KinProjectile, KinDefault = False, True
                user_text = ''

        if KinVariable:

            if ShowMotion:
                BackButton.draw()
                fig = pylab.figure(figsize=[4, 4], dpi=1000)
                ax = fig.gca()
                motion.acceleration(1,100)
                canvas = agg.FigureCanvasAgg(fig)
                canvas.draw()
                renderer = canvas.get_renderer()
                raw_data = renderer.tostring_rgb()
                size = canvas.get_width_height()
                surf = pygame.image.fromstring(raw_data, size, "RGB")
                surf = pygame.transform.scale(surf, (700, 600))
                Solution = True
                Count+=1

            else:
                BackButton.draw()
                rect2.draw()
                VariableText1.draw()
                VariableText2.draw()
                VariableText3.draw()
                VariableText4.draw()
                VariableText5.draw()
                VariableText6.draw()
                KinematicsSubmit.draw()
                screen.blit(equation,(870,60))

            if Count:
                screen.blit(surf, (80,60))


            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                             user_text += event.unicode

                    if a:
                        VariableText4.updateText(user_text)

                    elif b:
                        VariableText5.updateText(user_text)

                    elif c:
                        VariableText6.updateText(user_text)

            if VariableText4.check_click():
                user_text = ''
                a,b,c = True, False, False

            if VariableText5.check_click():
                user_text= ''
                a,b,c = False, True, False

            if VariableText6.check_click():
                user_text = ''
                a,b,c = False, False, True


            if KinematicsSubmit.check_click():
                a = VariableText4.text
                b = VariableText5.text
                c = VariableText6.text
                motion = Equation(a,b,c)
                ShowMotion = True

            if BackButton.check_click():
                count = 0
                ind^=1
                BackButton.updateText(li[ind])
                ShowProjectile = False
                KinVariable, KinDefault = False, True
                user_text = ''
    
        if KinProjectileSim:
            if Solution:
                rect2.draw()
                ProjectilePeriod.draw()
                ProjectileHigh.draw()
                ProjectileHorizontal.draw()
                ProjectilePeriod1.updateText(f'{round(projectile.Period(),2)} seconds')
                ProjectileHigh1.updateText(f'{round(projectile.HighestPoint(),2)} metres')
                ProjectileHorizontal1.updateText(f'{round(projectile.Distance(),2)} metres')
                ProjectilePeriod1.draw()
                ProjectileHigh1.draw()
                ProjectileHorizontal1.draw()
                BackButton.draw()
                run(screen,angleinput,velinput)

            else:
                BackButton.draw()
                rect2.draw()
                TextButtonLarge.draw()
                TextButtonLarge2.draw()
                ProjectileText1.draw()
                ProjectileText2.draw()
                KinematicsSubmit.draw()
            space = pymunk.Space()
            rect1.draw()

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode

                    if NodeCheck:
                        TextButtonLarge.updateText(user_text)

                    else:
                        TextButtonLarge2.updateText(user_text)
            

            if TextButtonLarge.check_click():
                user_text = ''
                NodeCheck = True

            if TextButtonLarge2.check_click():
                user_text = ''
                NodeCheck = False

            if KinematicsSubmit.check_click():
                angleinput = float(TextButtonLarge2.text)
                velinput = float(TextButtonLarge.text)
                projectile = Projectile(angleinput, velinput)
                Solution = True
                # run(screen,angleinput,velinput)
                


            if BackButton.check_click():
                count = 0
                ind^=1
                BackButton.updateText(li[ind])
                Solution = False
                KinProjectileSim, KinDefault = False, True
                user_text = ''
            
    pygame.display.update()