# Resim birleştirme addWeighted ile
import cv2
import matplotlib.pyplot as plt
r1 = cv2.imread('bayrak1.png')
r2 = cv2.imread('resimler/sincap1.png')


birlesik = cv2.addWeighted(r1, 0.05, r2, 0.95, 0)


cv2.imshow('Resim birleştirme:', birlesik)


print("Resim1[10,20] renkleri:",r1[10,20])
print("Resim2[10,20] renkleri:",r2[10,20])
print("birlesik[10,20] renkleri:",birlesik[10,20])


cv2.waitKey(0)
cv2.destroyAllWindows()
