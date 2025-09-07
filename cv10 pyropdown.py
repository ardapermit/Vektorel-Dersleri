# pyrdown, pyrup
import cv2


img1 = cv2.imread('/squirrel.jpg.png')
print("Resim boyutu1:", img1.shape)


img1Boyutlandirilmis = cv2.pyrDown(img1)
img1Boyutlandirilmis2 = cv2.pyrDown(img1Boyutlandirilmis)


cv2.imshow('Resim',img1)
cv2.imshow('Resim_kucuk',img1Boyutlandirilmis)
cv2.imshow('Resim_kucuk2',img1Boyutlandirilmis2)
cv2.waitKey(0)
cv2.destroyAllWindows()



# filtre
import cv2


img1 = cv2.imread('resimler/squirrel.jpg')
print("Resim boyutu1:", img1.shape)


img1Boyutlandirilmis = cv2.resize(img1, (200,300))
print("Resim boyutu2:", img1Boyutlandirilmis.shape)


g, y, r = img1.shape
print("img1.shape:", g, y, r)


img1Boyutlandirilmis2 = cv2.resize(img1, (g//4,y//4))
img1Boyutlandirilmis2[:,:,0] //= 2
img1Boyutlandirilmis2[:,:,1] //= 2
img1Boyutlandirilmis2[:,:,2] //= 2


cv2.imshow('Resim',img1)
cv2.imshow('Resim_kucuk',img1Boyutlandirilmis)
cv2.imshow('Resim_kucuk2',img1Boyutlandirilmis2)
cv2.waitKey(0)
cv2.destroyAllWindows()







# kamera görüntüsünü parçalama ve birleştirme








