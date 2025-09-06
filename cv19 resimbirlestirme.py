# Resim birleştirme add ile
import cv2
import matplotlib.pyplot as plt
r1 = cv2.imread('bayrak1.png')
r2 = cv2.imread('resimler/sincap1.png')


birlesik = cv2.add(r1, r2)


cv2.imshow('Resim birleştirme:', birlesik)


print("Resim1[10,20] renkleri:",r1[10,20])
print("Resim2[10,20] renkleri:",r2[10,20])
print("birlesik[10,20] renkleri:",birlesik[10,20])


cv2.waitKey(0)
cv2.destroyAllWindows()

—--------------------------

import cv2
alinan = cv2.VideoCapture(0)


while True:
    # img = cv2.imread("resimler/sincap.jfif")
    aa, img = alinan.read()


    # Setting All parameters
    t_lower = 100 # Lower Threshold
    t_upper = 200 # Upper threshold
    aperture_size = 3 # Aperture size
    img=cv2.resize(img, (750, 500))


    # Applying the Canny Edge filter
    # with Custom Aperture Size
    edge = cv2.Canny(img, t_lower, t_upper,apertureSize=aperture_size)
    cv2.imshow('original', img)
    cv2.imshow('edge', edge)
    if cv2.waitKey(1)==ord("q"): break
   
cv2.destroyAllWindows()
