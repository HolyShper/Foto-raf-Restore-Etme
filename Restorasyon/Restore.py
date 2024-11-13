import cv2
import numpy as np

Hasarlı_Fotoğraf = cv2.imread("Hasarli Fotograf.jpg")
cv2.imshow("Hasarli Fotograf",Hasarlı_Fotoğraf)

Maskelenmiş_Fotoğraf = cv2.imread("Maskelenmis Fotograf.jpg",0)
cv2.imshow("Maskelenmis Fotograf",Maskelenmiş_Fotoğraf)

ret , thresh = cv2.threshold(Maskelenmiş_Fotoğraf, 254, 255 , cv2.THRESH_BINARY)
cv2.imshow("Maske Threshold",thresh)

kernel = np.ones((7,7), np.uint8)
maske = cv2.dilate(thresh , kernel , iterations=1)
cv2.imshow("Maske", maske)

Restorasyon = cv2.inpaint(Hasarlı_Fotoğraf, maske , 3, cv2.INPAINT_TELEA)
cv2.imshow("Restore Edilmis Fotograf", Restorasyon) 
cv2.imwrite("Restore Edilmis Fotograf.jpg",Restorasyon)

cv2.waitKey(0)
cv2.destroyAllWindows()