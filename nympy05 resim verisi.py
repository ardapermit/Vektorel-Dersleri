import numpy as np
# veri = [8,5,9]
# veri = np.array(veri)


import cv2 # pip install opencv-python
veri = cv2.imread("Adsiz.png") # numpy dizi nesnesi döndürür/verir
# print(veri)
print(veri)
print("\n\n",veri[0])
print("\n\n",veri[0][0])
print("\n\n",veri[0][1])


veri[0][0] = [0,255,0] # BGR Blue,Green,Red
print(veri)


cv2.imwrite("adsiz2.png", veri)
