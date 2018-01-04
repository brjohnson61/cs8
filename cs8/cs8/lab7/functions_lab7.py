#Blake Johnson & Adam Gulliver
infile = open('/cs/student/brjohnson61/cs8/lab7/UCSB_URLs.txt','r')
URLs=infile.readlines()
infile.close()

def cleanURLs(URLs):
    cleanList=[]
    for item in list(URLs):
        new=item.strip()
        cleanList.append(new)
    return(cleanList)

import urllib.request
wp=urllib.request.urlopen('http://www.cs.ucsb.edu')
webpage=wp.read()
webpage=webpage.decode('utf-8')

def title(string):
    a=string.find('<title>')
    b=string.find('</title>')
    if '<title>' in string:
        return(string[a+7:b])
    else:
        print('error')
          
def UCSBTitles(myList):
    for item in myList:
        wp=urllib.request.urlopen(item)
        webpage=wp.read()
        webpage=webpage.decode('utf-8')
        print(title(webpage))
    
        
