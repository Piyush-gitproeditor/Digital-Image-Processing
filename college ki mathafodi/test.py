import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("Love.jpg")
img2 = cv2.imread("study.jpg")

print(img1.shape)
print(img2.shape)

# Create a single figure window for both images
plt.figure(figsize=(10, 5))

# First image slot
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # Fixes color channels for matplotlib
plt.axis('off')

# Second image slot
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # Fixes color channels for matplotlib
plt.axis('off')

# Show both at once
plt.show()