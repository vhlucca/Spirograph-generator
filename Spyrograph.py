from random import *
from graphics import *
import math


    #Name: Vitor Hugo Teixeira de Lucca Filho
    #Student Number: 21540166
    #pirograph is a geometric drawing toy that produces mathematical roulette curves of the variety technically known as hypotrochoids and epitrochoids.
    #
    #
    #http://en.wikipedia.org/wiki/Spirograph



    
    
#----------------------------------------------------------------------------

    
def getInputs():
    R = eval(input("Enter the radius of the fixed circle: "))
    r = eval(input("Enter the radius of the rolling circle: "))
    d = eval(input("Enter the distance of the pen from the center of the rolling circle: "))
    k = eval(input("Enter either 0 to draw hypotrochoid or 1 to draw an epitrochoid: "))
    return R,r,d,k


#----------------------------------------------------------------------------


def mdc(R,r):
    
    a = R
    b = r
    while b > 0:
        a, b = b, a % b

    
    return a


#----------------------------------------------------------------------------


def getNumberOfPoints(R,r,d,prec):

    a = mdc(R,r)
    prec = 3600
    
    n = prec*a
    return n

    
#----------------------------------------------------------------------------


def getPoints(R,r,d,prec):

    n = getNumberOfPoints(R,r,d,prec)

    
    xlist = []
    ylist = []
    clist = []
    
    t = 0
    u = 0
    v = 0
    
    for t in range(0,int(n)):
        
        x = (R-r)* math.cos(t*math.pi/180) + d*math.cos (t*(math.pi/180)*(R-r)/r)
        xlist.append(x)
        y = (R-r)* math.sin(t*math.pi/180) - d*math.sin (t*(math.pi/180)*(R-r)/r)
        ylist.append(y)
        clist.append((x,y))
        t = t+20
        

    newList = []
    newList1 = []
    maxx = max(xlist+ylist)

    if maxx>7:
        for u in xlist:
            newList.append(u*7/maxx)
        for v in ylist:
            newList1.append(v*7/maxx)
        xlist = newList
        ylist = newList1

        return xlist,ylist
    
    else:     
        return xlist,ylist


#-------------------------------------------------------------------------------

def getpoints(R,r,d,prec):

    n = getNumberOfPoints(R,r,d,prec)

    
    alist = []
    blist = []
    dlist = []
    
    t = 0
    u = 0
    v = 0

    for t in range(0,int(n)):

        a = (R+r)* math.cos(t*math.pi/180) - d*math.cos (t*(math.pi/180)*(R+r)/r)
        alist.append(a)
        b = (R+r)* math.sin(t*math.pi/180) - d*math.sin (t*(math.pi/180)*(R+r)/r)
        blist.append(b)
        dlist.append((a,b))
        t = t+5

    newList = []
    newList1 = []
    maxx = max(alist+blist)

    if maxx>7:
        for u in alist:
            newList.append(u*7/maxx)
        for v in ylist:
            newList1.append(v*7/maxx)
        alist = newList
        blist = newList1

        return alist,blist
    
    else:     
        return alist,blist
        
    

#----------------------------------------------------------------------
def draw(xlist,ylist):

    win = GraphWin('Spyro',600,600)
    win.setCoords(-10,-10,10,10)
    win.setBackground("light blue")

    
    Text(Point(-3.5, -9.0), "R = ").draw(win)
    Text(Point(0.5,-9.0), "r = ").draw(win)
    Text(Point(4.5,-9.0), "d = ").draw(win)
    
    input1 = Entry(Point(-2.0,-9.0),5)
    
    input1.draw(win)
    input1.setFill("yellow")
    input2 = Entry(Point(2.0,-9.0),5)
    
    input2.draw(win)
    input2.setFill("yellow")
    input3 = Entry(Point(6.0,-9.0),5)
   
    input3.draw(win)
    input3.setFill("yellow")

    
    rect1 = Rectangle(Point(-9.9,-8.5),Point(-8.0,-9.5))
    rect1.setFill('green')
    rect1.draw(win)
    button1 = Text(Point(-9.0,-9.0),"Hypo")
    button1.draw(win)

    rect2 = Rectangle(Point(-7.0,-8.5),Point(-5.0,-9.5))
    rect2.setFill("orange")
    rect2.draw(win)
    button2 = Text(Point(-6.0,-9.0),"Epi")
    button2.draw(win)
   
    rect = Rectangle(Point(10.0,-8.5),Point(8.0,-9.5))
    rect.setFill('red')
    rect.draw(win)
    button = Text(Point(9.0,-9.0),"Quit")
    button.draw(win)
    
    i = 0    

    for i in range (len(xlist)-1):
        line = Line(Point(xlist[i],ylist[i]),Point(xlist[i+1],ylist[i+1]))

        rand1 = randint(0,255)
        rand2 = randint(0,255)
        rand3 = randint(0,255)
        line.setOutline(color_rgb(rand1,rand2,rand3))
        line.setWidth(4)
        line.draw(win)
        i = i+1

        
    for k in range(100):
        p1 = win.getMouse()

        if p1.getX()<10.0 and p1.getX()>8.0 and p1.getY()<-8.5 and p1.getY()>-9.5:
            win.close()

        if p1.getX()>-9.9 and p1.getX()<-8.0 and p1.getY()<-8.5 and p1.getY()>-9.5:

            R = eval(input1.getText())
            r = eval(input2.getText())
            d = eval(input3.getText())

            prec = mdc(R,r)
            xlist,ylist = getPoints(R,r,d,prec)

            i = 0    

            for i in range (len(xlist)-1):
                line = Line(Point(xlist[i],ylist[i]),Point(xlist[i+1],ylist[i+1]))

                rand1 = randint(0,255)
                rand2 = randint(0,255)
                rand3 = randint(0,255)
                line.setOutline(color_rgb(rand1,rand2,rand3))
                line.setWidth(4)
                line.draw(win)
                i = i+1

            
        if p1.getX()>-7.0 and p1.getX()<-5.0 and p1.getY()<-8.5 and p1.getY()>-9.5:

              R = eval(input1.getText())
              r = eval(input2.getText())
              d = eval(input3.getText())

              prec = mdc(R,r)
              alist,blist = getpoints(R,r,d,prec)
             
              i = 0    

              for i in range (len(alist)-1):

                    line = Line(Point(alist[i],blist[i]),Point(alist[i+1],blist[i+1]))

                    rand1 = randint(0,255)
                    rand2 = randint(0,255)
                    rand3 = randint(0,255)
                    line.setOutline(color_rgb(rand1,rand2,rand3))
                    line.setWidth(4)
                    line.draw(win)
                    i = i+1

    
def main():
    
    R,r,d,k = getInputs()
    prec = mdc(R,r)
    if k ==0:
        
        xlist,ylist = getPoints(R,r,d,prec)

        draw(xlist,ylist)

    if k ==1:

        alist,blist = getpoints(R,r,d,prec)
        
        draw(alist,blist)

main()



