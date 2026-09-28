from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# ---------- Load Color Image ----------
color_image = Image.open("color.png").convert("RGB")
color_array = np.array(color_image)

# ---------- Convert to Grayscale ----------
gray_image = color_image.convert("L")
gray_array = np.array(gray_image)

# ---------- Information Before Conversion ----------
print("Before Conversion - RGB Image")
print("Width:", color_array.shape[1])
print("Height:", color_array.shape[0])
print("Number of Channels:", color_array.shape[2])
print("Data Type:", color_array.dtype)
print("Data Size (bytes):", color_array.nbytes)

# ---------- Information After Conversion ----------
print("\nAfter Conversion - Grayscale Image")
print("Width:", gray_array.shape[1])
print("Height:", gray_array.shape[0])
print("Number of Channels:", 1)
print("Data Type:", gray_array.dtype)
print("Data Size (bytes):", gray_array.nbytes)

# ---------- Display Images ----------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(color_array)
plt.title("Original RGB Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gray_array, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.subplots_adjust(wspace=0.05)

plt.show()