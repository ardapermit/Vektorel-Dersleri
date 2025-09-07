import cv2

r1 = cv2.imread("resimler/what.png")
print("r1.shape: ",r1.shape)

for a in range(r1.shape[0]):
    for b in range(r1.shape[1]):
        if r1[a,b][0]>50 and r1[a,b][1]<50 and r1[a,b][2]<50:
            r1[a,b] = [0,0,255]

cv2.imshow("Resim ", r1)
# cv2.imshow("Logo ", r1)

cv2.waitKey(0)
cv2.destroyAllWindows()
