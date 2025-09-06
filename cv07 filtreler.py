# kameradaki görüntüyü açma
import cv2, random, numpy as np
alinan = cv2.VideoCapture
g = alinan.get(3)
y = alinan.get(4)
print(g,y)
while True:
    _ , resim = alinan.read()
    resim[:100,:,0] = 100 
    resim[:100,:,1] = 100
    resim[:,:100,1] = 100
    resim[:,:100,0] = 100
    # resim [:,:,2] = 100
    cv2.imshow("Video5",resim) 
    tus = cv2.waitkey(1)  
    
    İf tus == ord('q'): break