'''
Notes: 
    [1] matrix must be represented as a unsigned 8bit interger (uint8) to display with plt.plot() and cv2.imshow()
    [2] myMakeHist vs myPlotHist:
        Its the difference between making a data representation of a histogram vs plotting the histogram in a GUI (repectfully).
    [3] myCreateImg takes input chanenels of r,g,b (in that order) and plugs them into their proper place. Useful for creating false color images
    where, for example, NIR may be subsituted for red.
    [4] NDVI Matrix is a single matrix where all elements range between -1 and 1. Do not insert an image.

    General notes:
        You will notice that all color matricies are cast to be unsigned 8 bit integers. This is required when showing an image using myShowImg.

'''


import numpy as np
import cv2
from matplotlib import pyplot as plt

def myShowImg(title,matrix):
    plt.title(title)
    plt.imshow(matrix)
    plt.show()
    return

# Note [2]
def myMakeHist(arr):
    hist = np.zeros(256, int)
    for i in arr:
        for j in i:
            hist[j] += 1
    return hist

# Actually plots a bar graph
def myPlotHist(title, matrix):
    ax = np.arange(256)
    plt.bar(ax, matrix)
    plt.title(title)
    plt.show()
    return

def returnColors(img):
    red     = img[:,:,2].astype('uint8')
    green   = img[:,:,1].astype('uint8')
    blue    = img[:,:,0].astype('uint8')
    return red, green, blue

# Note [3]
def myCreateImg(r,g,b):
    l,w = np.shape(r)
    emptyarr = np.zeros((l,w,3), dtype = 'uint8')
    # plt.plot() shows color in b g r
    emptyarr [: , : , 2] = b.astype('uint8')
    emptyarr [: , : , 1] = g.astype('uint8')
    emptyarr [: , : , 0] = r.astype('uint8')
    return emptyarr

def makeGrayImg(img):
    r,g,b = returnColors(img)
    # Note [1]
    avgarr = np.array((r+g+b)/3).astype('uint8')
    return myCreateImg(avgarr,avgarr,avgarr)

# May be buggy -- not adjusted to scale negative values, if they occur.
def mySubtract(img1, img2):
    l,w,z = np.shape(img1)
    emptyarr = np.zeros((l,w,3), dtype = 'uint8')
    emptyarr = np.abs(img1 - img2)
    return emptyarr


def myBinary(threshhold, grayScaleImg):
    l,w,z = np.shape(img)
    emptyarr = np.zeros((l,w,3), dtype = 'uint8')
    
    for i in range(l):
        for j in range(w):
            # passed img is grayscale, intensity values of all three matiricies are the same.
            if img[i][j][0] > threshhold:
                emptyarr[i][j][0] = 255
    
    gray = emptyarr[:,:,0]
    emptyarr[:,:,1] = gray
    emptyarr[:,:,2] = gray
    
    return emptyarr

def createNDVI(RedMatrix, NIRMatrix):
    return ((NIRMatrix - RedMatrix) / (NIRMatrix + RedMatrix))

# Note [4]
def myCreateColorNDVI(NDVIMatrix):
    # Note [1]
    NDVIRed = (abs(np.sin(NDVI*2*pi))*255).astype('uint8')
    # shift blue by pi over 3
    NDVIBlue = (abs(np.sin(NDVI*2*pi + (pi/3)))*255).astype('uint8')
    # shift by 2pi over 3
    NDVIGreen = (abs(np.sin(NDVI*2*pi + (2*pi/3)))*255).astype('uint8')    
    return myCreateImg((NDVIRed,NDVIGreen,NDVIBlue))


def myShowEachColorMatrix(Matrix):
    xSize, ySize, zSize = np.shape(Matrix)
    r,g,b = returnColors(Matrix)
    blackarr = np.zeros((xSize,ySize)).astype('uint8')
    
    #show the red in a pic
    br = myCreateImg(r,blackarr,blackarr)
    myShowImg("Red",br)
    #show the green in a pic
    bg = myCreateImg(blackarr,g,blackarr)
    myShowImg("Green",bg)
    #show the blue in a pic
    bb = myCreateImg(blackarr,blackarr,b)
    myShowImg("Blue",bb)