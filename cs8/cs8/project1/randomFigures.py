#Blake Johnson and Adam Gulliver


def drawPolygon(myTurtle, sideLength, numSides): 
    turnAngle=360/numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.left(turnAngle)
        
def drawCircle(myTurtle,radius):
    numSides=50
    sideLength=((3.1415926)*radius/25)
    drawPolygon(myTurtle,sideLength,numSides)

def drawCircleWithCenter(myTurtle,radius,x,y):
    myTurtle.up()
    myTurtle.goto(x,y)
    myTurtle.down()
    drawCircle(myTurtle,radius)

def drawSquareWithCenter(myTurtle,radius,x,y):
    myTurtle.up()
    myTurtle.goto(x,y)
    myTurtle.down()
    sideLength=2*radius
    numSides=4
    drawPolygon(myTurtle,sideLength,numSides)

def initialize(myTurtle):
    turtle.setworldcoordinates(-1,-1,5,5)
    myTurtle.up()
    myTurtle.goto(6,6)
    myTurtle.down()
    
def generateCircle(myTurtle):   
    x=random.uniform(0,4)
    y=random.uniform(0,4)
    radius=random.uniform(0,1)
    c=random.randint(0,9)
    if c==0:
        color="white"
    elif c==1:
        color="yellow"
    elif c==2:
        color="green"
    elif c==3:
        color="blue"
    elif c==4:
        color="purple"
    elif c==5:
        color="red"
    elif c==6:
        color="black"
    elif c==7:
        color="magenta"
    elif c==8:
        color="pink"
    else:
        color="brown"
    myTurtle.color(color)
    myTurtle.begin_fill()
    drawCircleWithCenter(myTurtle,radius,x,y)
    myTurtle.end_fill()

def generateSquare(myTurtle):    
    x=random.uniform(0,4)
    y=random.uniform(0,4)
    radius=random.uniform(0,1)
    c=random.randint(0,9)
    if c==0:
        color="white"
    elif c==1:
        color="yellow"
    elif c==2:
        color="green"
    elif c==3:
        color="blue"
    elif c==4:
        color="purple"
    elif c==5:
        color="red"
    elif c==6:
        color="black"
    elif c==7:
        color="magenta"
    elif c==8:
        color="pink"
    else:
        color="brown"
    myTurtle.color(color)
    myTurtle.begin_fill()
    drawSquareWithCenter(myTurtle,radius,x,y)
    myTurtle.end_fill()

def generateFigures(myTurtle,numFig):
    for i in range(numFig):
        f=random.randint(0,1)
        if f==0:
            generateCircle(myTurtle)
        else:
            generateSquare(myTurtle)

# To create a color picking function,
#def generateColor():
#       c=random.randint(0,9)
#    if c==0:
#        color="white"
#    elif c==1:
#        color="yellow"
#    elif c==2:
#        color="green"
#    elif c==3:
#        color="blue"
#    elif c==4:
#        color="purple"
#    elif c==5:
#        color="red"
#    elif c==6:
#        color="black"
#    elif c==7:
#        color="magenta"
#    elif c==8:
#        color="pink"
#    else:
#        color="brown"
#    myTurtle.color(color)

# Then place generateColor() before myTurtle.begin_fill() and after radius=random.uniform(0,1)
# in both generateCircle() and generateSquare()
