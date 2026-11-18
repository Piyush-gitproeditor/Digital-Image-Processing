import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def power_law_transformation(image, gamma):
    lookup_table = np.array([((i / 255.0) ** gamma) * 255 
                             for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, lookup_table)
image_path = Path(__file__).resolve().parent / 'study.jpg'
img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Could not read image at {image_path}")
else:
    img_brightened = power_law_transformation(img, gamma=0.4)
    img_darkened = power_law_transformation(img, gamma=2.2)
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.title('Gamma = 0.4 (Brightened)')
    plt.imshow(img_brightened, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.title('Gamma = 2.2 (Darkened)')
    plt.imshow(img_darkened, cmap='gray', vmin=0, vmax=255)
    plt.axis('off')
    
    plt.show()
