import cv2
r1 = cv2.imread("resimler/sincapp.png")
r2 = cv2.imread("turkı.png")
sonuc = cv2.subtract(r2,r1)
cv2.imshow("Resim1", r1)
cv2.imshow("Resim2", r2)
cv2.imshow("sonuc resmi", sonuc)
cv2.waitKey(0)
cv2.destroyAllWindows()