import cv2
r1 = cv2.imread("resimler/Adsiz.png")
r2 = cv2.imread("resimler/Adsiz2.png")
sonuc = cv2.subtract(r1,r2)
cv2.imshow("Resim1",r1)
cv2.imshow("Resim2",r2)
cv2.imshow("sonuc resmi", sonuc)
cv2.waitKey(0)
cv2.destroyallWindows