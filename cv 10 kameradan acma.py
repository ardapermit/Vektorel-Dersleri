# kameradaki görüntüyü açma
import cv2
alinan = cv2.VideoCapture(0)
while True:
    _ , resim = alinan.read()
    cv2.imshow("Videooo",resim)
    cv2.imshow("Videooo1",resim)
    tus = cv2.waitKey(1)
    if tus == ord('q'): break
