import cv2
import matplotlib.pyplot as plt

image = cv2.imread("pic3.jpg")

brightness_value = 50
brightened_image = cv2.add(image, brightness_value)

cv2.imshow("Brightened Image", brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
