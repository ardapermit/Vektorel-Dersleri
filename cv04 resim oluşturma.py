import cv2
import numpy as np

# 3x3 piksel örnek bayrak
xx = [
    [[0, 0, 0], [255, 255, 255], [0, 0, 0]],       # Siyah - Beyaz - Siyah
    [[255, 255, 255], [0, 0, 0], [255, 255, 255]], # Beyaz - Siyah - Beyaz
    [[0, 0, 0], [255, 255, 255], [0, 0, 0]]        # Siyah - Beyaz - Siyah
]

# NumPy array'e çevir (uint8 olmalı)
xx_cevirilen = np.array(xx, dtype=np.uint8)

# Dosyaya kaydet
cv2.imwrite("bjk_bayrak.png", xx_cevirilen)

# Dosyadan oku
okunan = cv2.imread("bjk_bayrak.png")
print(okunan)

# Görselleştir
cv2.imshow("Resim", okunan)
cv2.waitKey(0)
cv2.destroyAllWindows()
