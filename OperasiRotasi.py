import cv2

image = cv2.imread("pic4.jpg")

height, width = image.shape[:2]

angle = 45

center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
