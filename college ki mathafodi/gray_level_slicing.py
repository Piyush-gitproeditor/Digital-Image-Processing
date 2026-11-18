import cv2
import numpy as np
from pathlib import Path

def gray_level_slicing(image_path, A, B, preserve_bg=False, highlight_val=255):
   #A, B: Lower and upper intensity threshold limits.
 
 
  # Load image directly in grayscale (single I/O operation)
  img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  if img is None:
    raise FileNotFoundError(f"Error: Could not load image from {image_path}")

  # Create a boolean mask for the target intensity range [A, B]
  # Vectorized comparison runs at C-speed via NumPy
  mask = (img >= A) & (img <= B)

  if preserve_bg:
    # Copy original to keep background, modify only masked pixels
    output_img = img.copy()
    output_img[mask] = highlight_val #highlight_val: Intensity value assigned to the target range
  else:
    # Create black background array and fill only the masked region
    output_img = np.zeros_like(img)
    output_img[mask] = highlight_val

  return img, output_img


image_path = Path(__file__).with_name("Love.jpg")
img, result = gray_level_slicing(str(image_path), 100, 200)

scale_percent = 50  # Display images at half their original size.
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
display_size = (width, height)

img_resized = cv2.resize(img, display_size, interpolation=cv2.INTER_AREA)
result_resized = cv2.resize(result, display_size, interpolation=cv2.INTER_AREA)

cv2.imshow("Original", img_resized)
cv2.imshow("Sliced", result_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

