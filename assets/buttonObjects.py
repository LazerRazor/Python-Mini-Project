from assets.modules import *

button1 = Button('Moment & Forces',400,80,(440,320), col.darkpurple)
button2 = Button('Kinematics',400,80,(440,440) ,col.darkpurple)

ElementButton = Button('Add Element',400,80,(840,50), col.darkpurple)
MomentButton = Button('Add a Hinge',400,80,(840,180), col.darkpurple)
ForceButton = Button('Add a Force',400,80,(840,310), col.darkpurple)
SolutionButton = Button('Calculate Solution',400,80,(840,440), col.darkpurple)

CalcMomButton = Button('Plot Moment',400,80,(840,50), col.darkpurple)
CalcShearButton = Button('Plot Shear Forces',400,80,(840,180), col.darkpurple)
CalcReactButton = Button('Plot Reaction Forces',400,80,(840,310), col.darkpurple)
CalcDispButton = Button('Plot Displacement',400,80,(840,440), col.darkpurple)
BackButton = Button('Go Back',400,80,(840,570), col.darkpurple, col.red)

TextButton1 = Button('',150,50,(865,180),col.red,col.offwhite)
TextButtonLarge = Button('',350,50,(865,180),col.red,col.offwhite)
TextButtonLarge2 = Button('',350,50,(865,310),col.red,col.offwhite)
TextButton2 = Button('',150,50,(1065,180),col.red,col.offwhite)
TextButton3 = Button('',150,50,(865,310),col.red,col.offwhite)
TextButton4 = Button('',150,50,(1065,310),col.red, col.offwhite)