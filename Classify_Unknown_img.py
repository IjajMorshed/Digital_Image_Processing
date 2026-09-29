from PIL import Image
import numpy as np

# image = Image.open("test_binary.png")
image = Image.open("test_grayscale.png")
# image = Image.open("test_color.png")
img = np.array(image)

if img.ndim == 2:
    unique = np.unique(img)

    if len(unique) == 2:
        print("Binary image")
        print("Reason: detected" , len(unique), "unique pixel values.")
    else:
        print("Grayscale image")
        print("Reason: single channel with", len(unique), "unique pixel values.")

elif img.ndim == 3:
    print("Full-color image")
    print("Reason:", img.shape[2], "channels detected.")

else:
    print("Unknown image type")