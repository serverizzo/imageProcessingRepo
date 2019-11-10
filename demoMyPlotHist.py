import imageProcessingLibrary as ipl

# grafiti
img = ipl.readImg("img.jpg")
# mostly white
# img = ipl.readImg("img2.jpg")
# Low Contrast
# img = ipl.readImg("img3.jpg")

#break into 1d arrays
r,g,b = ipl.returnColors(img)

# can only take 1 color matrix
rhist = ipl.myMakeHist(r)
ghist = ipl.myMakeHist(g)
bhist = ipl.myMakeHist(b)

# pass histograms to be plotted
ipl.myPlotHist("red histogram", rhist)
ipl.myPlotHist("green histogram", ghist)
ipl.myPlotHist("blue histogram", bhist)
