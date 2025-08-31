import cv2, random
alinan = cv2.VideoCapture(0)
while True:
    resim1 = cv2.imread("bayrak1.png")
   
    _ , resim = alinan.read()
    cv2.imshow("Videooo",resim)
    # print(resim.shape)
    for a in range(resim1.shape[0]):
        for b in range(resim1.shape[1]):
            if resim1[a,b][0]>200 and resim1[a,b][1]>200 and resim1[a,b][2]>200:
                resim1[a,b] = resim[a,b]
    cv2.imshow("Videooo1",resim1)


    tus = cv2.waitKey(1)
    if tus == ord('q'): break
