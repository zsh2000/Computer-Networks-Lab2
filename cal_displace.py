import cv2
import numpy as np

def my2str(i):
	if i<10:
		return "00"+str(i)
	elif i<100:
		return "0"+str(i)
	else:
		return str(i)
        
start_end = []
for i in range(2, 417):
    img_prev = cv2.imread("./test/"+my2str(i-1)+".jpg").astype(float)
    img = cv2.imread("./test/"+my2str(i)+".jpg").astype(float)
    mean_displace = np.mean(np.abs(img_prev - img))
    if mean_displace > 50:
        start_end.append((i-1, i))