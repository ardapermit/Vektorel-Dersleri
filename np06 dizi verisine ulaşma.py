import numpy as np
import cv2 # pip install opencv-python
veri = cv2.imread("Adsiz.png") # numpy dizi nesnesi döndürür/verir
print("\n\nDizi verisi1:\n",veri)


alinan = veri[::,1::2]
print("\n\nDizi verisi2:\n",alinan)


cv2.imwrite("alinanlar.png", alinan)