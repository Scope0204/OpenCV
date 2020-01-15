# 픽셀별로 색상 다루기
import cv2

image = cv2.imread('cat.jpg')
# BRG
image[:,:,0] = 255

cv2.imshow('Image', image)
cv2.waitKey(0)
