#Blake Johnson
#Adam Gulliver

def cleanGpaList(gpaList):
    cleanList=[]
    for item in list(gpaList):
        new=item.split()
        cleanList.append(new)
    return(cleanList)

def dictGpa(cleanList):
    myDict={}
    for item in cleanList:
        if item[0] in myDict:
            key=item[0]
            value=float(item[1])
            myDict[key]=value+myDict[key]
        else:
            key=item[0]
            myDict[key]=float(item[1])
    return myDict

def printCumulative(myDict):
    for item in myDict:
        print(item,myDict[item])
