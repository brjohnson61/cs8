#Blake Johnson and Adam Gulliver

def starSetup():
    starfile=open('starfile.txt', 'r')
    dictStar={}
    for line in starfile:
        cleanline=line.split()
        key=cleanline[0]
        values=cleanline[1:]
        dictStar[key]=values
    return(dictStar)

dictStar=starSetup()

def starData(starName,dictStar):
    dictStar=starSetup()
    if starName in dictStar:
        return dictStar[starName]
    else:
        return 'Not Found in dictStar'

def starDistance(low,high):
    for key in dictStar:
        if float(dictStar[key][0])>low and float(dictStar[key][0])<high:
          print(key)

def starAPPVM(low,high):
    for key in dictStar:
        if float(dictStar[key][1])>low and float(dictStar[key][1])<high:
            print(key)

def starAvs(myDict):
    divG0=0
    divG1=0
    divG2=0
    divG3=0
    divG4=0
    divG5=0
    G0=0
    G1=0
    G2=0
    G3=0
    G4=0
    G5=0
    for key in myDict:
        if float(myDict[key][1])>0 and float(myDict[key][1])<=0.5:
            G0=G0+float(myDict[key][0])
            divG0=divG0+1
        elif float(myDict[key][1])>0.5 and float(myDict[key][1])<=1.0:
            G1=G1+float(myDict[key][0])
            divG1=divG1+1
        elif float(myDict[key][1])>1.0 and float(myDict[key][1])<=1.5:
            G2=G2+float(myDict[key][0])
            divG2=divG2+1
        elif float(myDict[key][1])>1.5 and float(myDict[key][1])<=2.0:
            G3=G3+float(myDict[key][0])
            divG3=divG3+1
        elif float(myDict[key][1])>2.0 and float(myDict[key][1])<=2.5:
            G4=G4+float(myDict[key][0])
            divG4=divG4+1
        else:
            G5=G5+float(myDict[key][0])
            divG5=divG5+1
    print('The mean distance of stars in '+'dictStar '+'with 0.0 < APPVM <= 0.5 is ',round(G0/divG0,1))
    print('The mean distance of stars in '+'dictStar '+'with 0.5 < APPVM <= 1.0 is ',round(G1/divG1,1))
    print('The mean distance of stars in '+'dictStar '+'with 1.0 < APPVM <= 1.5 is ',round(G2/divG2,1))
    print('The mean distance of stars in '+'dictStar '+'with 1.5 < APPVM <= 2.0 is ',round(G3/divG3,1))
    print('The mean distance of stars in '+'dictStar '+'with 2.0 < APPVM <= 2.5 is ',round(G4/divG4,1))
    print('The mean distance of stars in '+'dictStar '+'with 2.5 < APPVM <= 3.0 is ',round(G5/divG5,1))

            
