
def randomDots(myTurtle,noOfTimes):
    for i in range(noOfTimes):
        myTurtle.up()
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        myTurtle.goto(x,y)
        thickness=random.randint(1,100)
        color=random.randint(0,2)
        if color==0:
            turtleColor='red'
        else:
            if color==1:
                turtleColor='green'
            else:
                turtleColor='blue'
        myTurtle.color(turtleColor)
        myTurtle.dot(thickness)

def fibonacci(n):
    if n==1 or n==2:
        return(1)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    
def fibonacci2(n):
    import math
    fib2=int((1/math.sqrt(5))*((1+math.sqrt(5))/2)**n+0.5)
    return(fib2)

def mysterySum(numTerms):
    acc=0
    import math
    for i in range(1,numTerms+1):
        fib2=fibonacci2(i)/2**i
        acc=fib2+acc
    return(acc)

        
