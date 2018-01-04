#Blake Johnson
#Adam Gulliver

def stringToPermutation(s):
    caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc=''
    for ch in s:
        a=0
        for c in s:
            if c<ch:
                a=a+1
        acc=acc+str(a+1)
    return(acc)

def printList(myList):
    for i in range(0, len(myList)):
        print(i,myList[i])

    
def maxList(myList):
    biggest=0
    for i in range(0, len(myList)):
        if myList[i]>myList[biggest]:
            biggest=i
    print("Maximum is "+str(myList[biggest]),"at index "+str(biggest))
