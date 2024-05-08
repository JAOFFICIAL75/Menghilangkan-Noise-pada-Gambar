import cv2



img = cv2.imread("unnamed.jpg")

median = cv2.medianBlur(img, 5)
cv2.imshow("Real Image", img)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)
