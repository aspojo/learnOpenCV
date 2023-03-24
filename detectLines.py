import math

import cv2
import numpy as np

txt = open("testData-one.txt", encoding='utf-8-sig').readline()
arr = txt.split(",")
image = np.zeros((600, 3200), dtype=np.ubyte)

for i in range(0, 3200 - 1):
    h = int(int(arr[i]) / 1000)
    if h > 499:
        h = 499
    if h < 0:
        h = 0
    for j in range(0, 8):
        image[h - j][i] = 255
cv2.imshow("image", image)

# cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
lines = cv2.HoughLinesP(image, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=0)

if lines is not None:
    for i in range(0, len(lines)):
        # 向上偏移gap像素
        gap = 20
        cv2.line(image, (lines[i][0][0], lines[i][0][1]-gap), (lines[i][0][2], lines[i][0][3]-gap), 200, 3, cv2.LINE_AA)

cv2.imshow("image", image)
cv2.imwrite("image.jpg", image)
cv2.waitKey(0)

#
#
# image = cv2.imread('C:\\Users\\lin.chen1\\Desktop/disk1.jpg')
# output = image.copy()
# img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Find circles
#
# minDist = 100
# param1 = 30  # 500
# param2 = 50  # 500 #smaller value-> more false circles
# minRadius = 5
# maxRadius = 20  # 10
#
# # docstring of HoughCircles: HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) -> circles
# circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, minDist, param1=param1, param2=param2, minRadius=minRadius,
#                            maxRadius=maxRadius)
#
# # If some circle is found
# if circles is not None:
#     # Get the (x, y, r) as integers
#     circles = np.round(circles[0, :]).astype("int")
#     print(circles)
#     # loop over the circles
#     for (x, y, r) in circles:
#         cv2.circle(output, (x, y), r, (0, 255, 0), 2)
# # show the output image
# cv2.imshow("circle", output)
