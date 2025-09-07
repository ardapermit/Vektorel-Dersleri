import cv2
goruntu = cv2.VideoCapture(0)
while True:
    r = cv2.imread("resimler/ardaad.png")
    _ , r = goruntu.read()
    r1 = cv2.imread("resimler/what.png")
    print("r.shape: ",r.shape,"  r1.shape: ",r1.shape)

    for a in range(r1.shape[0]):
        for b in range(r1.shape[1]):
            if not(r1[a,b][0]>200 and r1[a,b][1]>200 and r1[a,b][2]>200):
                x = r.shape[0]-r1.shape[0]+a
                y = r.shape[1]-r1.shape[1]+b
                r[x,y] = r1[a,b]

    cv2.imshow("Zemin ", r)
    # cv2.imshow("Logo ", r1)

    if cv2.waitKey(1)==ord("q"): break

cv2.destroyAllWindows()
