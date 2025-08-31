# numpy.full ile resim verisi oluşturma


import cv2, numpy as np
xx = np.full((200, 300, 3), [255,255,255],np.uint8)
xx[97,150]=[0,0,255]
xx[98,150]=[0,0,255]
xx[99,150]=[0,0,255]
cv2.imshow("Resim",xx)
cv2.waitKey(0)
