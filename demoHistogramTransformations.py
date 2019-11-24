import imageProcessingLibrary as ipl


img = ipl.readImg("under.jpg")
ipl.myShowImg("input img", img)
r,g,b = ipl.returnColors(img)
redHist = ipl.myMakeHist(r)
greenHist = ipl.myMakeHist(g)
blueHist = ipl.myMakeHist(b)
ipl.myPlotHist("orgRed",redHist)
ipl.myPlotHist("orgGreen",greenHist)
ipl.myPlotHist("orgBlue",blueHist)

logImg = ipl.logTransformation(img)
ipl.myShowImg("after log transformation", logImg)
r,g,b = ipl.returnColors(logImg)
redHist = ipl.myMakeHist(r)
greenHist = ipl.myMakeHist(g)
blueHist = ipl.myMakeHist(b)
ipl.myPlotHist("orgRed",redHist)
ipl.myPlotHist("orgGreen",greenHist)
ipl.myPlotHist("orgBlue",blueHist)