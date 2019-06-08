import cv2
import math

file = open("train.txt")

jpglist = []
txtlist = []
anotionlist = []

for line in file:

    line = line.strip('\n')
    line = line.strip('\n').replace('data/','')
    # 去除换行符
    jpglist.append(line)
    txtlist.append(line.replace("jpg", "txt"))

for i in range(len(jpglist)):
    jpgfile = cv2.imread(jpglist[i])
    # print(jpgfile.shape)
    
    txtfile = open(txtlist[i])
    for txtfileline in txtfile:
    
        txtfileline = txtfileline.strip('\n')
        descriptor = txtfileline.split(" ")
        kind = descriptor[0]
        a = float(descriptor[1])
        b = float(descriptor[2])
        c = float(descriptor[3])
        d = float(descriptor[4])
        w = jpgfile.shape[0]
        h = jpgfile.shape[1]
        x1 = math.ceil((a*2*h - c*h)/2)
        x2 = math.ceil((a*2*h + c*h)/2)
        y1 = math.ceil((b*2*w - d*w)/2)
        y2 = math.ceil((b*2*w + d*w)/2)
    
        if x1 < 0:
            x1 = 0
        if x1 > w:
            w1 = int(w - 1)
        if x2 < 0:
            x1 = 0
        if x2 > w:
            w1 = int(w - 1)
        if y1 < 0:
            y1 = 0
        if y1 > h:
            y1 = int(h - 1)
        if y2 < 0:
            y2 = 0
        if y2 > h:
            y2 = int(h - 1)
        jpglist[i] = jpglist[i] + " " + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + "," + kind
        
    anotionlist.append(jpglist[i] + "\n")
    txtfile.close()
 
file.close()
file = open("train.txt","w")
for line in jpglist:
    file.write(line + "\n")
file.close()