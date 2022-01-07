import cv2

def sum(num1, num2):
    return num1+num2

def prod(num1, num2):
    return num1*num2

def sub(num1, num2):
    return num1-num2

image = cv2.imread('C:/Users/N/Desktop/Test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
  
cv2.waitKey(0)
cv2.destroyAllWindows()