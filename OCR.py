#call cv2 module to read an image
import cv2
#Call pytesseract
import pytesseract
#Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#read imagine using imread function
img = cv2.imread("shoes.png")
#convert image to string and store in a variable
#text = pytesseract.image_to_string(img)
#print the text
#print(text)

#preprocessing starts
#convert the image to greyscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#performing threshold 
rect,thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
#specify structure shape
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(18,18))
#apply dilation 
dilation = cv2.dilate(thresh1,rect_kernel,iterations=1)
#finding contours
contours,hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#output the image
cv2.imshow('image',thresh1)
#waitkey will close the window when user will press any key
cv2.waitKey(0)
#Creating a copy of image
img2 = img.copy()
#A text file is created
file = open("recognize.txt","w+")
file.write("")
file.close()
for cnt in contours:
    x,y,w,h=cv2.boundingRect(cnt)
    #draw a rectangle from copied image
    rect = cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
    #cropping a text block for giving input to ocr
    cropped=img2[y:y+h,x:x+w]
    #open the file to write the text in append mode
    file = open("recognized.txt","a")
    #apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)
    #Add the text into the file
    file.write(text)
    file.write("\n")
    #close the file
    file.close