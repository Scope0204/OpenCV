import cv2

# imread(파일 이름, 이미지를 읽는 방법)
# IMREAD_COLOR : 이미지를 컬러로 읽겠다
img_basic = cv2.imread('cat.jpg' , cv2.IMREAD_COLOR)
# imshow(타이틀 이름 , 파일이름 ) : 파일이름에 해당하는 이미지를 화면에 출력
cv2.imshow('Image Basic' , img_basic)
# waitKey(time) : 키보드 입력을 처리하는 함수
# time = 0 : 무한 대기
cv2.waitKey(0)

# 화면의 모든 윈도우를 닫는 함수
cv2.destroyAllWindows()
# 닫고 나서 회색 이미지가 나타남


#BGR 파일을 GRAY로 바꾸겠다 ( 2 = to )
#OpenCV는 [G,R,B] 형태로 저장된다
img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
img_basic = cv2.imread('cat.jpg' , cv2.IMREAD_COLOR)
cv2.imshow('Image Gray' , img_gray)
cv2.waitKey(0)
