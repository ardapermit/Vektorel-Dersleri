# perspective trasformation/bükme (tıklamalar ile)
import cv2, numpy as np
goruntu = cv2.imread('resimler/sudoku.png')
goruntu1 = cv2.imread('resimler/sudoku.png')
parca = goruntu1[0:100, 0:200]


n = [[0,0],[0,0],[0,0],[0,0]]
sayac = 0
baslangic = np.float32([[n[0][0],n[0][1]],[n[1][0],n[1][1]],[n[2][0],n[2][1]],[n[3][0],n[3][1]]])
yeniyer = np.float32([[50,60],[300,50],[30,310],[325,300]])


xx = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(goruntu,f"nokta{sayac%4} x,y icin tikla..",(10,30),xx,.9,(0,255,0),1)
cv2.imshow("Orjinal Goruntu", goruntu)


def tiklamaAl(olay,x,y,durum,parametre):
    global sayac, baslangic, yeniyer, xx
    if olay == cv2.EVENT_LBUTTONDOWN :
        goruntu[0:100, 0:200] = parca
        print("\nSol tıklandı",x,y)
        n[sayac%4][0], n[sayac%4][1] = x,y
   
        for a in n: print(a,end=" ")
        sayac += 1
        cv2.putText(goruntu,f"nokta{sayac%4} x,y icin tikla..",(10,30),xx,.9,(0,255,0),1)
        cv2.imshow("Orjinal Goruntu", goruntu)


    # float32([[üstsol x,y],[üstsağ x,y],[altsol x,y],[altsağ x,y]])
    baslangic = np.float32([[n[0][0],n[0][1]],[n[1][0],n[1][1]],[n[2][0],n[2][1]],[n[3][0],n[3][1]]])
    yeniyer = np.float32([[0,0],[sutun,0],[0,satir],[sutun,satir]])


satir,sutun = goruntu.shape[:2]
print(satir,sutun)
