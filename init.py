import cv2
import numpy as np

img = cv2.imread('imagens/image.png')

width, height = 250,350

pts1 = np.float32([[88,266], [588, 254], [111,974], [605, 957]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))

for x in range (0,4):
    cv2.circle(img, (pts1[x][0],pts1[x][1]),5,(0,0,255),cv2.FILLED)

cv2.imshow('original', img)
cv2.imshow("output", output)
cv2.waitKey(0)