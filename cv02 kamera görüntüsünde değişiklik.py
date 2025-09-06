# kameradaki görüntü üzerinde işlem yapma
import cv2, random
alinan = cv2.VideoCapture(0)
# print(alinan.get(0))
g = alinan.get(3)
y = alinan.get(4)
print(g,y)
while True:
    _ , resim = alinan.read()
    # cv2.line(resim,(0,0),(640,360),(0,0,255),2)
    x1 = random.randint(0,50)
    y1 = random.randint(0,50)
    x2 = random.randint(60,int(g))
    y2 = random.randint(60,int(y))
    cv2.line(resim,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.imshow("Videooo",resim)
    tus = cv2.waitKey(1)


    if tus == ord('q'): break
