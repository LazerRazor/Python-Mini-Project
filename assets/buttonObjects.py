from assets.modules import *
from assets.button import *
from assets.rectangle import *

button1 = Button('Moment & Forces',400,80,(440,320), col.darkpurple)
button2 = Button('Kinematics',400,80,(440,440) ,col.darkpurple)

ElementButton = Button('Add Element',400,80,(840,50), col.darkpurple)
MomentButton = Button('Add a Hinge',400,80,(840,180), col.darkpurple)
ForceButton = Button('Add a Force',400,80,(840,310), col.darkpurple)
SolutionButton = Button('Calculate Solution',400,80,(840,440), col.darkpurple)

CalcMomButton = Button('Plot Bending Force',400,80,(840,50), col.darkpurple)
CalcShearButton = Button('Plot Shear Forces',400,80,(840,180), col.darkpurple)
CalcReactButton = Button('Plot Reaction Forces',400,80,(840,310), col.darkpurple)
CalcDispButton = Button('Plot Axial Forces',400,80,(840,440), col.darkpurple)
BackButton = Button('Go Back',400,80,(840,570), col.darkpurple, col.red)

TextButton1 = Button('',150,50,(865,180),col.red,col.offwhite)
TextButtonLarge = Button('',350,50,(865,180),col.red,col.offwhite)
TextButtonLarge2 = Button('',350,50,(865,310),col.red,col.offwhite)
TextButton2 = Button('',150,50,(1065,180),col.red,col.offwhite)
TextButton3 = Button('',150,50,(865,310),col.red,col.offwhite)
TextButton4 = Button('',150,50,(1065,310),col.red, col.offwhite)

TextNew = Button('Add First Co-ordinate: ',400,80,(840,100),col.black,col.white, hover=False) 
TextNew2 = Button('Select Node Number:  ',400,80,(840,100),col.black,col.white, hover=False)
TextNew3 = Button('Add Magnitude of Force:  ',400,80,(840,230),col.black,col.white, hover=False)
TextNew1 = Button('Add Second Co-ordinate: ',400,80,(840,230),col.black,col.white, hover=False)
ProjectileText1 = Button('Enter Initial Velocity:  ',400,80,(840,100),col.black,col.white, hover=False)
ProjectileText2 = Button('Enter Angle of Inclination:  ',400,80,(840,230),col.black,col.white, hover=False)

VariableText1 = Button('A:  ',150,80,(840,130),col.black,col.white, hover=False)
VariableText2 = Button('B:  ',150,80,(840,210),col.black,col.white, hover=False)
VariableText3 = Button('C:  ',150,80,(840,290),col.black,col.white, hover=False)

VariableText4 = Button(' ',200,50,(950,145),col.black,col.offwhite )
VariableText5 = Button(' ',200,50,(950,225),col.black,col.offwhite )
VariableText6 = Button('  ',200,50,(950,305),col.black,col.offwhite )

SubmitCor = Button('Create Element ',300,80,(890,400),col.black);
SubmitCor2 = Button('Create Hinge',300,80,(890,400),col.black);
SubmitCor3 = Button('Create Load',300,80,(890,400),col.black);

KinematicsSubmit = Button('Analyse Motion',300,80,(890,400),col.black);


ProjectileButton = Button('Projectile Motion',400,80,(840,50), col.darkpurple)
VariableButton = Button('Variable Motion',400,80,(840,180), col.darkpurple)
ProjectileSimulateButton = Button('Simulate Projectile Motion',400,80,(840,310), col.darkpurple)


ProjectilePeriod = Button('The Period of Flight is:',400,80,(840,100),col.black,col.white, hover=False) 
ProjectileHigh = Button('The Highest Point is:',400,80,(840,230),col.black,col.white, hover=False)
ProjectileHorizontal = Button('The Horizontal Range is:',400,80,(840,360),col.black,col.white, hover=False)

ProjectilePeriod1 = Button('',400,50,(840,180),col.black,col.white, hover=False) 
ProjectileHigh1 = Button('',400,50,(840,310),col.black,col.white, hover=False)
ProjectileHorizontal1 = Button('',400,50,(840,440),col.black,col.white, hover=False)

equation = pygame.image.load(r'assets/equation.png')
equation = pygame.transform.scale(equation, (320, 60))

rect1 = Rectangle(740,620,(50,50),col.white)
rect2 = Rectangle(400,470,(840,50),col.white)

def MomentsDefaultDraw():
        ElementButton.draw()
        MomentButton.draw()
        ForceButton.draw()
        SolutionButton.draw()
        BackButton.draw()


def MomentsForceDraw():
            BackButton.draw()
            rect2.draw()
            TextButtonLarge.draw()
            TextButtonLarge2.draw()
            TextNew2.draw()
            TextNew3.draw()
            SubmitCor3.draw()

def MomentsMomentDraw():
            BackButton.draw()
            rect2.draw()
            TextButtonLarge.draw()
            TextNew2.draw()
            SubmitCor2.draw()


def MomentElementDraw():
            BackButton.draw()
            rect2.draw()
            TextButton1.draw()
            TextButton2.draw()
            TextButton3.draw()
            TextButton4.draw()
            TextNew.draw()
            TextNew1.draw()
            SubmitCor.draw()


def SolveDraw():
            CalcMomButton.draw()
            CalcShearButton.draw()
            CalcReactButton.draw()
            CalcDispButton.draw()
            BackButton.draw()

def KinDefaultDraw():
            ProjectileButton.draw()
            VariableButton.draw()
            ProjectileSimulateButton.draw()
            BackButton.draw()


def ProjectileSolutionDraw():

                rect2.draw()
                ProjectilePeriod.draw()
                ProjectileHigh.draw()
                ProjectileHorizontal.draw()
                ProjectilePeriod1.draw()
                ProjectileHigh1.draw()
                ProjectileHorizontal1.draw()


def ProjectileDefaultDraw():
                BackButton.draw()
                rect2.draw()
                TextButtonLarge.draw()
                TextButtonLarge2.draw()
                ProjectileText1.draw()
                ProjectileText2.draw()
                KinematicsSubmit.draw()


DisplacementButton = Button('Displacement',300,80,(890,100), col.darkpurple)
VelocityButton = Button('Velocity',300,80,(890,230), col.darkpurple)
AccelerationButton = Button('Acceleration',300,80,(890,360), col.darkpurple)

def VariableMotion():
    DisplacementButton.draw()
    VelocityButton.draw()
    AccelerationButton.draw()