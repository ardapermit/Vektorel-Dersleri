# HoughCircles ile daire tespiti
import cv2, numpy as np


# Kamerayı başlat (veya bir video dosyası da kullanılabilir)
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret: break
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Görüntüyü griye çevir
    # Gürültüyü azaltmak için bulanıklaştır
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)


    # Hough Daire Dönüşümü ile daireleri bul
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=100,
        param1=100,
        param2=30,
        minRadius=30,
        maxRadius=150
    )


    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # Daireyi çiz
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            # Merkeze bir nokta koy
            cv2.circle(frame, (x, y), 2, (0, 0, 255), 3)
            cv2.putText(frame, "Bardak?", (x - 40, y - r - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
   
    cv2.imshow("Yuvarlak", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): break


cap.release() # Temizlik
cv2.destroyAllWindows()
