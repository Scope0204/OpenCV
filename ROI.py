#ROI : Region of interest  = 관심 영역
#관심있는 부분을 뽑아내 추출

import cv2

image = cv2.imread('cat.jpg')

# Numpy Slicing : ROI 처리 기능
roi = image[300:450 , 50:200]

# ROI 단위로 이미지 복사하기
image[0:150 , 0:150] = roi

cv2.imshow('Image', image)
cv2.waitKey(0)
