import cv2
r = cv2.imread("resimler/ardaad.png")
m, y, k = cv2.split(r)

cv2.imshow("Orjinal   ", r)

birlesik = cv2.merge((y,m,k)) # bgr
cv2.imshow("Birlesik  ", birlesik)

cv2.waitKey(0)
cv2.destroyAllWindows()