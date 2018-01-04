#Blake Johnson & Adam Gulliver
from cImage import *

def photoAlbum(n):  
    ind=0               #initialization
    acc=1
    myWin=ImageWin("CS8 Project 4: Photo Album",400,350)
    im=FileImage("/fs/student/brjohnson61/cs8/project4/p4images/picture"+str(ind)+".gif")
    im.draw(myWin)
    bar=FileImage("/fs/student/brjohnson61/cs8/project4/p4images/bottom_bar.gif")
    bar.setPosition(0,300)
    bar.draw(myWin)
    while acc==1: #while loop that runs while photo album window is active
        pos=myWin.getMouse()
        if pos[0]>20 and pos[0]<60: #back button
            if pos[1]>305 and pos[1]<345:
                if ind==0:
                    ind=n
                else:
                    ind=ind-1
                im=FileImage("/fs/student/brjohnson61/cs8/project4/p4images/picture"+str(ind)+".gif")
                im.draw(myWin)
        if pos[0]>340 and pos[0]<380: #Forward button
            if pos[1]>305 and pos[1]<345:
                if ind == n:
                    ind=0
                else:
                    ind=ind+1
                im=FileImage("/fs/student/brjohnson61/cs8/project4/p4images/picture"+str(ind)+".gif")
                im.draw(myWin)      
        if pos[0]>180 and pos[0]<220: #exit button
            if pos[1]>305 and pos[1]<345: 
                acc=0 #to stop the while loop
                myWin.exitOnClick()
                
                 
