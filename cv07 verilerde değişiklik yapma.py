import cv2
import numpy as np
import random

# 200x300 boyutunda beyaz resim (3 kanal, uint8 tipinde)
xx = np.full((200, 300, 3), [255, 255, 255], np.uint8)

# 100 tane rastgele pikseli kırmızı yap
for a in range(100):
    x = random.randint(0, xx.shape[0]-1)  # satır
    y = random.randint(0, xx.shape[1]-1)  # sütun
    xx[x, y] = [0, 0, 255]  # BGR formatında kırmızı

# Görüntüyü göster ve kaydet
cv2.imshow("Resim", xx)
cv2.imwrite("resim.png", xx)
cv2.waitKey(0)
cv2.destroyAllWindows()

                       

