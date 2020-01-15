#특정 범위 픽셀을 바꿀 떄
import cv2
import time

image = cv2.imread('cat.jpg')


# 방법 1 : 해당 좌표로 일일이 찾아가ㄴ 바꾸는 방법
# #time.time() : 현 시간
# start_time = time.time()
# for i in range(0 , 100):
#     for j in range(0, 100):
#         image[i,j] = [255,255,255]
# #걸린 시간
# print("---%s second ---" % (time.time() - start_time))

# 방법 2 : 슬라이싱 기법을 통해 좌표를 바꿈
start_time = time.time()
# x : 0~99 , y : 0~99
image[0:100 , 0:100] = [0,0,0]
print("---%s second ---" % (time.time() - start_time))

cv2.imshow('Image' , image)
cv2.waitKey(0)
