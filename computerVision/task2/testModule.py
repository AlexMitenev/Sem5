import numpy as np
import cv2

img = cv2.imread("text.bmp", 0)
blur = cv2.GaussianBlur(img, (3, 3), 0)
laplacian = cv2.Laplacian(blur, cv2.CV_64F)

cv2.imshow("image", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()