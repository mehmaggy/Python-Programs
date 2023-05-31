
import cv2
image = cv2.imread('res.png')

#convert the image to grayscale format
img = cv2.imread(image, cv2.COLOR_BGR2GRAY)

# apply binary thresholding
ret, thresh = cv2.imread(img, 150, 255, cv2.THRESH_BINARY)
cropped_image = img[60:88, 3:130]
# Display cropped image
cv2.imshow("cropped", cropped_image)
# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)

# visualize the binary image

cv2.waitKey(0)

cv2.destroyAllWindows()