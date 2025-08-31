# video dosyasındaki görüntüyü açma
import cv2
alinan = cv2.VideoCapture("file_example_MP4_480_1_5MG.mp4")
while True:
    _ , resim = alinan.read()
    cv2.imshow("Videooo",resim)
    tus = cv2.waitKey(1)
# https://file-examples.com/index.php/sample-video-files/sample-mp4-files/


