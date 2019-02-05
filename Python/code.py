from PIL import Image
from math import fabs


imageName = "matise.jfif"
threshold = 20



image = Image.open("Images/"+imageName)
size = image.size
data = list(image.getdata()) 
#AVERAGES---DONE                     CODE
def similar( color1,color2,threshold = 20):
    for x in range(0,3):
        if(not fabs(color1[x] - color2[x]) <= threshold):
            return False
    return True

def average_func(colors1,colors2):
    ret = []
    def yld():
        x = zip(colors1,colors2)
        for y in x:
            yield int(sum(y)/2)
    for i in yld():
        ret.append(i)
    return(tuple(ret))

def giveData(data, num = 20):
    averages = []
    code = []
    def generator_data():
        for pix in data:
            yield pix

    gen_data = generator_data()
    for pix in gen_data:
        foundMate = False
        for x in range(0,len(averages)):
            if(similar(pix, averages[x], threshold=num)):  #IF SIMILAR
                averages[x] = average_func(pix, averages[x]) #AVERAGE
                code.append(x)
                foundMate = True
                break
        if(not foundMate):  #IF NO SIMILAR AVERAGE WAS FOUND
            foundMate = True
            averages.append(pix)
            code.append(averages.index(averages[-1]))
    return([code,averages])

def makeImage(code, averages):
    im = Image.new("RGB", size)
    data = []
    for i in code:
        data.append(averages[i])
    im.putdata(data)
    im.show()

dat = giveData(data,threshold)
makeImage(dat[0], dat[1])