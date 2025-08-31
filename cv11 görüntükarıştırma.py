# iki kameradan görüntü karıştırma
import cv2, random
alinan = cv2.VideoCapture(0)
alinan1 = cv2.VideoCapture(1)
while True:  
    _ , resim = alinan.read()
    _ , resim1 = alinan1.read()
    cv2.imshow("Videooo",resim)
    # print(resim.shape)
    for a in range(resim1.shape[0]):
        for b in range(resim1.shape[1]):
            if resim1[a,b][0]>200 and resim1[a,b][1]>200 and resim1[a,b][2]>200:
                resim1[a,b] = resim[a,b]
    cv2.imshow("Videooo1",resim1)


    tus = cv2.waitKey(1)
    if tus == ord('q'): break
