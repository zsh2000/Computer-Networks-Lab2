import os
import cv2
import numpy as np

path = './cropped/'
filelist = os.listdir(path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

fps = 10
size = (500, 900)

video = cv2.VideoWriter("clip2.mp4", fourcc, fps, size)

filelist.sort()
for item in filelist:

    if item.endswith('.jpg'):
        item = path + item
        img = cv2.imdecode(np.fromfile(item,dtype=np.uint8),-1)
        video.write(img)
    print(item + '.jpg')

video.release()
cv2.destroyAllWindows()