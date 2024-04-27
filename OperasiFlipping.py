import cv2

image = cv2.imread("pic4.jpg")

flipped_horizontal = cv2.flip(image, 1)

flipped_vertical = cv2.flip(image, 0)

cv2.imshow("Flipped Horizontal", flipped_horizontal)
cv2.imshow("Flipped Vertical", flipped_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
