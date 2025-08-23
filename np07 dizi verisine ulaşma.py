import numpy as np
import cv2 # pip install opencv-python
veri = cv2.imread("images.jpg") # numpy dizi nesnesi döndürür/verir
print("\n\nDizi verisi1:\n",veri)


# alinan = veri[::,1::2]
alinan = veri[68:78,140:150]
print("\n\nDizi verisi2:\n",alinan)


cv2.imwrite("alinanlar.png", alinan)
