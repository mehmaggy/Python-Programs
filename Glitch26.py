import cv2
import numpy as np
img = cv2.imread("ICT360.png")
points = np.array([[50, 270], [220, 160], [100, 50],[100,50]])

cv2.fillConvexPoly(img, 220, 1)
cv2.threshold("polygon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()