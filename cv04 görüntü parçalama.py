# kamera görüntüsünü parçalama ve birleştirme
import cv2, random, numpy as np
alinan = cv2.VideoCapture(0)
# print(alinan.get(0))
g = alinan.get(3)
y = alinan.get(4)
print(g,y)
while True:
    _ , resim = alinan.read()
    r1 = resim[:180,:320]
    r2 = resim[:180:,320:]
    r3 = resim[180:, :320]
    r4 = resim[180:, 320:]
    print(r1.shape,r2.shape)
    cv2.imshow("Video1",r1)
    cv2.imshow("Video2",r2)
    cv2.imshow("Video3",r3)
    cv2.imshow("Video4",r4)
    r5 = np.concat((r2,r1),axis=1)
    r6 = np.concat((r4,r3),axis=1)
    r7 = np.concat((r6,r5))
    cv2.imshow("Video5",r7)
    tus = cv2.waitKey(1)


    if tus == ord('q'): break
