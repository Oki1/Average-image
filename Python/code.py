from PIL import Image
from math import fabs
import os
blurry = r"Images/man.jpeg"
im_blurry = Image.open(blurry)
size = (100,100)
clear = lambda: os.system('cls')

def returnAverage(one, two):

    averager = (one[0] + two[0]) / 2
    averageg = (one[1] + two[1]) / 2
    averageb = (one[2] + two[2]) / 2
    return(round(averager), round(averageg), round(averageb))

def show(image):
    image.show()

def similar(one, two, num = 20):
    if(round(fabs(one[0] - two[0])) >= num):
        return(False)
    if(round(fabs(one[1] - two[1])) >= num):
        return(False)
    if(round(fabs(one[1] - two[1])) >= num):
        return(False)
    return (True)

def BiggyfyColor(size, color): #dat spelling
    data = []
    for x in range(0, size[0]*size[1]):
        data.append(color)
    return(tuple(data))

def showColor():
    color = returnAverage(list(im_blurry.getdata()))
    averageNew  = Image.new("RGB", size)
    averageNew.putdata(BiggyfyColor(size, color))
    averageNew.show();

def getTeams(image, similarity):

    teams = [[0]]
    data = image.getdata()
    teamsAverage = [data[0]]

    size = image.size
    print(len(data))
    for z in range(0, len(data)):
        pixel = data[z]
        added = False
        for x in range(0, len(teams)):
            if(similar(teamsAverage[x], pixel, similarity)):
                teams[x].append(z)
                teamsAverage[x] = returnAverage(teamsAverage[x], pixel)
                added = True
        if(not added):
            teams.append([z])
            teamsAverage.append(pixel)
    print(len(teams))
getTeams(im_blurry, 20)
