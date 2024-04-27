import cv2
import matplotlib.pyplot as plt


img = cv2.imread("pic2.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hist_red = cv2.calcHist([img_rgb], [0], None, [256], [0, 256])
hist_green = cv2.calcHist([img_rgb], [1], None, [256], [0, 256])
hist_blue = cv2.calcHist([img_rgb], [2], None, [256], [0, 256])

plt.figure(figsize=(10, 5))

plt.plot(hist_red, color="red", label="Red")
plt.plot(hist_green, color="green", label="Green")
plt.plot(hist_blue, color="blue", label="Blue")

plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Full Color Histogram")
plt.legend()
plt.grid(True)
plt.savefig("histogram.png")
plt.show()
