import cv2

imviewx = cv2.imread("d:\\python\\11.jpg")
cv2.imshow("这是谁?", imviewx)

cv2.waitKey(0)

cv2.destroyAllWindows()
