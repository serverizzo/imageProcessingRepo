import imageProcessingLibrary as ipl


img = ipl.readImg("img.jpg")
ipl.myShowImg("input img", img)

logImg = ipl.logTransformation(img)

ipl.myShowImg("after log transformation", logImg)

