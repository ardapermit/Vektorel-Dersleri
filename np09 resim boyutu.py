# resim boyutlarını öğrenme
import numpy as np, cv2
veri = cv2.imread("images.jpg") # numpy dizi nesnesi döndürür/verir
print("\n\nDizi verisi1:\n",veri)


cv2.imshow("Yeni resim",veri)
print(veri.shape)
print(veri.shape[0])


cv2.waitKey(0)
cv2.destroyAllWindows()