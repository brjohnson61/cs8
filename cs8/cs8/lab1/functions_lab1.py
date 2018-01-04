#Blake Johnson
#Section 2
def drawTriangleJerry(sideLength):
    for i in range(3):
        jerry.forward(sideLength)
        jerry.left(120)
def drawTriangle(myTurtle,sideLength):
    for i in range(3):
        myTurtle.forward(sideLength)
        myTurtle.left(120)
def drawFlower(myTurtle,sideLength,n):
    for i in range(n):
        drawTriangle(myTurtle,sideLength)
        myTurtle.left(360/n)
def circleWithCenter(myTurtle,radius,cx,cy):
    myTurtle.up()
    myTurtle.goto(cx,cy)
    myTurtle.down()
    for i in range(180):
        myTurtle.forward((3.1415926*radius)/90)
        myTurtle.left(2)
        
        
