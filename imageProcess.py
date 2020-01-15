import cv2

image = cv2.imread('cat.jpg')

# 픽셀 수 및 이미지 크기 확인
print(image.shape)  # shape : [높이 , 넓이, 채널]
print(image.size)

# 이미지 Numpy객체의 특 픽셀을 가리킴
px = image[100 , 100]

# B , G , R 순으로 출력 ( 단 Gray Scale의 경우 B , G , R로 구분되지 않음 )
print(px) # 높이 :  100 , 너비 : 100 표시

# R만 출력하기 (  B G R배열의 [2] -> 3번째 = R )
print(px[2])
