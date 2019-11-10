import imageProcessingLibrary as ipl

img = ipl.readImg("invert.jpg")
negImg = ipl.imageNegative(img)
ipl.myShowImg("original img", img)
ipl.myShowImg("negative img", negImg)
