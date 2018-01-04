# Blake Johnson and Adam Gulliver

def nameLengths(myList):
    for name in myList:
        print(name, len(name))
        
def nameLengthsRestricted(myList,firstLetters):
    myList.sort()
    for item in myList:
        if item[0] in firstLetters:
            print(item, len(item))
        
def mixedList(myList):
    count=0
    count1=''
    newList=[]
    for item in myList:
        if type(item)==float or type(item)== int:
            newList.append(item)
            count=count+1
        if type(item)==str:
            count1=count1+item
    print("Average is "+str(sum(newList)/count),"\nString portion is: "+str(count1))
