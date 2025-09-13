# Eşikleme threshold
import cv2


# kaynak = cv2.VideoCapture('http://192.168.1.7:8080/video')
kaynak = cv2.VideoCapture(0)
# goruntu = cv2.imread("images/yesil_elma_1.jpg", 0)


while kaynak.isOpened():


    durum, goruntu = kaynak.read()
    gri_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)


    a, Cevrilmis = cv2.threshold(gri_goruntu, 50, 200, cv2.THRESH_BINARY)


    cv2.imshow("Orjinal1", cv2.pyrDown(gri_goruntu))
    cv2.imshow("Cevrilmis sekli", cv2.pyrDown(Cevrilmis))


    if cv2.waitKey(1)==ord("q"): break


cv2.destroyAllWindows()

