import cv2
import matplotlib.pyplot as plt

image = cv2.imread('ball.jpg')
grey_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

cv2.imshow(grey_img, cmap='gray')
cv2.imshow()