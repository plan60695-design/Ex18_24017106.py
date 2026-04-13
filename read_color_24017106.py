import cv2
import numpy as np
import os

# 영상 읽기
image = cv2.imread("Chap4/images/Read_color.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 읽기 오류")

# 영상 크기
h, w = image.shape[:2]

# 4등분 크기
cell_h = h // 4
cell_w = w // 4

# 결과 영상 생성
dst = np.zeros_like(image)

# 4x4 블록 처리
for row in range(4):        # 0,1,2,3
    for col in range(4):    # 0,1,2,3
        y1 = row * cell_h
        y2 = (row + 1) * cell_h
        x1 = col * cell_w
        x2 = (col + 1) * cell_w

        block = image[y1:y2, x1:x2]

        # 문제의 행/열 번호는 1부터 시작하니까 +1 해줌
        r = row + 1
        c = col + 1

        # 짝수행 짝수열 -> 오른쪽 90도
        if r % 2 == 0 and c % 2 == 0:
            block = cv2.rotate(block, cv2.ROTATE_90_CLOCKWISE)

        # 홀수행 홀수열 -> 왼쪽 90도
        elif r % 2 == 1 and c % 2 == 1:
            block = cv2.rotate(block, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # 결과 영상에 복사
        dst[y1:y2, x1:x2] = block

# results 폴더 생성
os.makedirs("./results", exist_ok=True)

# 저장
cv2.imwrite("./results/read_color_converted_학번.jpg", dst)

# 출력
cv2.imshow("original", image)
cv2.imshow("converted", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()