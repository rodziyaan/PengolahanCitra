import cv2
import numpy as np

image = cv2.imread("pic4.jpg", cv2.IMREAD_GRAYSCALE)

min_intensity = np.min(image)
max_intensity = np.max(image)
stretched_image = ((image - min_intensity) / (max_intensity - min_intensity)) * 255

cv2.imshow("Contrast Stretched Image", stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
