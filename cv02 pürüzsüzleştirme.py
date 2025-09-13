# Gürültü giderme / pürüzsüzleştirme.
import cv2
# kaynak = cv2.VideoCapture('http://192.168.1.7:8080/video')
kaynak = cv2.VideoCapture(0)
# goruntu = cv2.imread("images/tacmahal_noised.jpg", 0)

while kaynak.isOpened():

    durum, goruntu = kaynak.read()
    cv2.imshow("Orjinal", (goruntu))

    goruntu1 = cv2.fastNlMeansDenoising(goruntu, None, 15, 10, 10)
    cv2.imshow("denoised", (goruntu1))

    if cv2.waitKey(1)==ord("q"): break 

cv2.destroyAllWindows() 