#Blake Johnson, Adam Gulliver
def reverse(s):
    acc=''
    for i in range(1,len(s)+1):
        acc=acc+s[-i]
    return(acc)

def breakString(s,ind):
    acc=''
    ret=''
    for i in range(1,len(s)+1-ind):
        acc=acc+s[-i]
    for i in range(0,ind):
        ret=ret+s[i]
    return(acc+ret)

def indexCh(ch):
    caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if ch in caps:
        return(caps.index(ch))
    
def caesark(s):
    caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc=''
    for ch in s:    
        index=indexCh(ch)
        newindex=(index-3)%26
        newch=caps[newindex]
        acc= acc+newch
    return(acc) #'DEMYIJXUMYDJUHEVEKHTYISEDJUDJ' decryption for k =3

def shuffle(s):
    acc=''
    import random
    for i in range(len(s)):
        ind=random.randint(0,len(s)-1)
        acc=s[ind]+acc
        s=s.replace(s[ind],"")
    return(acc)

def pileUp():
    s='A'
    while s!="":
        s=input("I will echo your input until you enter return only:")
        print(s)
    
