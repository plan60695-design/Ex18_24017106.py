import cv2
import numpy as np

# 영상 크기 (3:2 비율)
height = 400
width = height * 3 // 2

# 흰색 배경 영상 생성
img = np.zeros((height, width, 3), dtype=np.uint8)
img[:] = (255, 255, 255)

# 중심 좌표
cx, cy = width // 2, height // 2

# 태극 반지름 = 높이의 1/4
r = height // 4

# 1. 큰 반원 2개
# 위쪽 빨강
cv2.ellipse(img, (cx, cy), (r, r), 0, 180, 360, (0, 0, 255), -1)

# 아래쪽 파랑
cv2.ellipse(img, (cx, cy), (r, r), 0, 0, 180, (255, 0, 0), -1)

# 2. 작은 반원 2개
# 왼쪽 아래 빨강
cv2.ellipse(img, (cx - r // 2, cy), (r // 2, r // 2), 0, 0, 180, (0, 0, 255), -1)

# 오른쪽 위 파랑
cv2.ellipse(img, (cx + r // 2, cy), (r // 2, r // 2), 0, 180, 360, (255, 0, 0), -1)

# 바깥 원 테두리
cv2.circle(img, (cx, cy), r, (0, 0, 0), 1)

# 출력
cv2.imshow("Taegeuk", img)
cv2.waitKey(0)
cv2.destroyAllWindows()