from anastruct import SystemElements
import matplotlib.pyplot as plt
ss = SystemElements()


def Solve():
    global ss;
    ss.solve()
    ss.show_structure()
    


def addElement():
    global ss;
    x1,y1 = map(int,input("Enter Starting Co-ordinate: ").split())
    x2,y2 = map(int,input("Enter Ending Co-ordinate: ").split())
    ss.add_element(location=[[x1, y1], [x2, y2]])
    
count = 1
def addHinge():
    global ss;
    i = int(input("Type 1 for Hinge, Select 2 for Fixed Joint: "))
    global count
    if(i==1): ss.add_support_hinged(node_id=count)
    else: ss.add_support_fixed(node_id=count)
    count+=1


id = 1;
def addLoad():
    global id,ss;
    force = int(input("Enter magnitude of force: "))
    ss.q_load(element_id=id, q=force)
    id+=1

check = True;
while(check):
    kk = int(input("Select an Option: \n1.Add Element \n2.Add Hinge \n3.Add Load \n4.Solve \n"))
    if(kk==1):
        addElement();
    elif(kk==2):
        addHinge();
    elif(kk==3):
        addLoad();
    elif(kk==4):
        check =False;
        Solve();

