# importing cv2
import cv2
 
# path
image_path = r'swap.png'
image = cv2.imread(image_path)
 
# Displaying the image
cv2.imshow('', image)
cv2.waitKey(0)
cv2.destroyAllWindows()