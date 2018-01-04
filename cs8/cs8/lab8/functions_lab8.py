#Blake Johnson & Adam Gulliver

def rgbNoGreen(oldPixel):
    r=oldPixel.getRed()
    b=oldPixel.getBlue()
    newPixel=Pixel(r,0,b)
    return(newPixel)

def rgbBW(oldPixel):
    r=oldPixel.getRed()
    b=oldPixel.getBlue()
    g=oldPixel.getGreen()
    average=r+g+b//3
    if average > 128:
        newPixel=Pixel(255,255,255)
        return newPixel
    else:
        pixel=Pixel(0,0,0)
        return pixel

def rgbSepia(oldPixel):
    R=oldPixel.getRed()
    B=oldPixel.getBlue()
    G=oldPixel.getGreen()
    nR=int((R*0.393+G*.769+B*.189))
    nG=int((R*.349+G*.686+B*.168))
    nB=int((R*.272+G*.534+B*.131))
    newPixel=Pixel(min(nR,255),min(nG,255),min(nB,255))
    return newPixel

def rgbGBR(oldPixel):
    R=oldPixel.getRed()
    B=oldPixel.getBlue()
    G=oldPixel.getGreen()
    newPixel=Pixel(G,B,R)
    return newPixel

def filterImage(NW,SE,rgbFunction):
    for x in range(NW[0],SE[0]):
        for y in range(NW[1],SE[1]):
            oldPixel=myImage.getPixel(x,y)
            newPixel=rgbFunction(oldPixel)
            myImage.setPixel(x,y,newPixel)
            
            

    
    
