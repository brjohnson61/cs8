# Blake Johnson and Adam Gulliver
import random
def generateKey(raw_key):
    acc=''
    ref=''
    key='' 
    for i in range(len(raw_key),0,-1):
        if raw_key[i-1] not in acc:
            acc=acc+raw_key[i-1]
    for i in range(1,len(acc)+1):
        ref=ref+acc[-i]
    key=''
    for r in ref:
        a=0
        for c in ref:
            if c<r:
                a=a+1
        key=key+str(a+1)
    return key

def toPlaintext(s,keyLength):
    intermediate=''
    acc=''
    caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for ch in s:
        if ch in caps:
            intermediate=intermediate+ch
    if len(intermediate)%keyLength!=0:
        for i in range(keyLength-(len(intermediate)%keyLength)):
            idx=random.randint(0,25)
            acc=acc+caps[idx]
    plaintext=intermediate+acc
    return plaintext

def columnar(plaintext,key):
    even=''
    odd=''
    count=0
    plaintext=toPlaintext(plaintext,len(str(key)))
    for ch in plaintext:
        if count%2==0:
            even=even+ch
        else:
            odd=odd+ch
        count=count+1
    cipher=odd+even
    print(key)
    for i in range(0,len(cipher),len(str(key))):
        print(cipher[i:i+len(str(key))])

def encryptColumnar():
    s=input("Enter the message: ")
    raw_key=input("Enter the raw key for columnar transposition: ")
    k=generateKey(raw_key)
    newString=toPlaintext(s,len(key))
    columnar(newString,key)
