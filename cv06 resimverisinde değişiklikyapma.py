import cv2, numpy as np
xx = np.full((200, 300, 3), [255,255,255],np.uint8)
for a in range(xx.shape[0]):
    xx[a,xx.shape[1]//2]=[0,0,255]


for b in range(xx.shape[1]):
    if b % 4 == 0: xx[xx.shape[0]//2,b]=[255,0,0]


cv2.imshow("Resim",xx)
cv2.waitKey(0)

