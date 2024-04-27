import cv2
import numpy as np

image = cv2.imread("pic4.jpg")

kernel = np.ones((5, 5), np.float32) / 25

convolved_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("Convolved Image", convolved_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
