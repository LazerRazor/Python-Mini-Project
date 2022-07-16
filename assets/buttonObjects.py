# Modules that are being imported
from assets.modules import *
from assets.button import *
from assets.rectangle import *

# Main Menu buttons.
button1 = Button('Moment & Forces',400,80,(440,320), col.darkpurple)
button2 = Button('Kinematics',400,80,(440,440) ,col.darkpurple)

# Moment default screen buttons.
ElementButton = Button('Add Element',400,80,(840,50), col.darkpurple)
MomentButton = Button('Add a Hinge',400,80,(840,180), col.darkpurple)
ForceButton = Button('Add a Force',400,80,(840,310), col.darkpurple)
SolutionButton = Button('Calculate Solution',400,80,(840,440), col.darkpurple)

# Moment solution screen buttons.
CalcMomButton = Button('Plot Moment',400,80,(840,50), col.darkpurple)
CalcShearButton = Button('Plot Shear Forces',400,80,(840,180), col.darkpurple)
CalcReactButton = Button('Plot Reaction Forces',400,80,(840,310), col.darkpurple)
CalcDispButton = Button('Plot Axial Forces',400,80,(840,440), col.darkpurple)
BackButton = Button('Go Back',400,80,(840,570), col.darkpurple, col.red)

'''Buttons created as variable text boxes.'''
# Moments section input boxes.
TextButton1 = Button('',150,50,(865,180),col.red,col.offwhite)
TextButton2 = Button('',150,50,(1065,180),col.red,col.offwhite)
TextButton3 = Button('',150,50,(865,310),col.red,col.offwhite)
TextButton4 = Button('',150,50,(1065,310),col.red, col.offwhite)
# Kinematics section input boxes.
TextButtonLarge = Button('',350,50,(865,180),col.red,col.offwhite)
TextButtonLarge2 = Button('',350,50,(865,310),col.red,col.offwhite)
# Kinematics section output boxes.
ProjectilePeriod1 = Button('',400,50,(840,180),col.black,col.white, hover=False) 
ProjectileHigh1 = Button('',400,50,(840,310),col.black,col.white, hover=False)
ProjectileHorizontal1 = Button('',400,50,(840,440),col.black,col.white, hover=False)
# Variable motion section input boxes.
VariableText4 = Button(' ',200,50,(950,145),col.black,col.offwhite )
VariableText5 = Button(' ',200,50,(950,225),col.black,col.offwhite )
VariableText6 = Button('  ',200,50,(950,305),col.black,col.offwhite )

'''Buttons created as static text boxes for directions.'''
# Moments section text boxes.
TextNew = Button('Add First Co-ordinate: ',400,80,(840,100),col.black,col.white, hover=False) 
TextNew2 = Button('Select Node Number:  ',400,80,(840,100),col.black,col.white, hover=False)
TextNew3 = Button('Add Magnitude of Force:  ',400,80,(840,230),col.black,col.white, hover=False)
TextNew1 = Button('Add Second Co-ordinate: ',400,80,(840,230),col.black,col.white, hover=False)
# Kinematics section text boxes.
ProjectileText1 = Button('Enter Initial Velocity:  ',400,80,(840,100),col.black,col.white, hover=False)
ProjectileText2 = Button('Enter Angle of Inclination:  ',400,80,(840,230),col.black,col.white, hover=False)
ProjectilePeriod = Button('The Period of Flight is:',400,80,(840,100),col.black,col.white, hover=False) 
ProjectileHigh = Button('The Highest Point is:',400,80,(840,230),col.black,col.white, hover=False)
ProjectileHorizontal = Button('The Horizontal Range is:',400,80,(840,360),col.black,col.white, hover=False)
# Variable motion section text boxes.
VariableText1 = Button('A:  ',150,80,(840,130),col.black,col.white, hover=False)
VariableText2 = Button('B:  ',150,80,(840,210),col.black,col.white, hover=False)
VariableText3 = Button('C:  ',150,80,(840,290),col.black,col.white, hover=False)

# Submit buttons.
SubmitCor = Button('Create Element ',300,80,(890,400),col.black);
SubmitCor2 = Button('Create Hinge',300,80,(890,400),col.black);
SubmitCor3 = Button('Create Load',300,80,(890,400),col.black);
KinematicsSubmit = Button('Analyse Motion',300,80,(890,400),col.black);

# Kinematics default screen buttons.
ProjectileButton = Button('Projectile Motion',400,80,(840,50), col.darkpurple)
VariableButton = Button('Variable Motion',400,80,(840,180), col.darkpurple)
ProjectileSimulateButton = Button('Simulate Projectile Motion',400,80,(840,310), col.darkpurple)


# Loading image of graph plotted using anastruct.
equation = pygame.image.load(r'assets/equation.png')
equation = pygame.transform.scale(equation, (320, 60))

# Rectangle objects created.
rect1 = Rectangle(740,620,(50,50),col.white)
rect2 = Rectangle(400,470,(840,50),col.white)

'''Function Defining Section'''

def MomentsDefaultDraw():
    '''Creating all buttons needed
    for Moments section default screen'''
    ElementButton.draw()
    MomentButton.draw()
    ForceButton.draw()
    SolutionButton.draw()
    BackButton.draw()


def MomentsForceDraw():
    '''Creating all buttons needed
    for Moments section Force screen'''
    BackButton.draw()
    rect2.draw()
    TextButtonLarge.draw()
    TextButtonLarge2.draw()
    TextNew2.draw()
    TextNew3.draw()
    SubmitCor3.draw()

def MomentsMomentDraw():
    '''Creating all buttons needed
    for Moments section Hinge screen'''
    BackButton.draw()
    rect2.draw()
    TextButtonLarge.draw()
    TextNew2.draw()
    SubmitCor2.draw()


def MomentElementDraw():
    '''Creating all buttons needed
    for Moments section Element screen'''
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
    '''Creating all buttons needed
    for Moments section Solve screen'''
    CalcMomButton.draw()
    CalcShearButton.draw()
    CalcReactButton.draw()
    CalcDispButton.draw()
    BackButton.draw()

def KinDefaultDraw():
    '''Creating all buttons needed for
    Kinematics section default screen'''
    ProjectileButton.draw()
    VariableButton.draw()
    ProjectileSimulateButton.draw()
    BackButton.draw()


def ProjectileSolutionDraw():
    '''Creating all buttons needed for Kinematics
    section Projectile graph solution screen'''
    rect2.draw()
    ProjectilePeriod.draw()
    ProjectileHigh.draw()
    ProjectileHorizontal.draw()
    ProjectilePeriod1.draw()
    ProjectileHigh1.draw()
    ProjectileHorizontal1.draw()


def ProjectileDefaultDraw():
    '''Creating all buttons needed for Kinematics
    section Projectile graph default screen'''
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
    '''Creating all buttons needed for Variable
    motion section solution screen'''
    DisplacementButton.draw()
    VelocityButton.draw()
    AccelerationButton.draw()