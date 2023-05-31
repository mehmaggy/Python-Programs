import cv2
image = cv2.imread('res.png')

#convert the image to grayscale format
img_gray = cv2.imread(image, cv2.COLOR_BGR2GRAY)

# apply binary thresholding
ret, thresh = cv2.imread(img_gray, 150, 255, cv2.THRESH_BINARY)

# visualize the binary image
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)
cv2.imwrite('image_thres1.jpg', thresh)
cv2.destroyAllWindows()