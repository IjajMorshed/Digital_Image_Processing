from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt 
# ---------- Grayscale Image ---------- 
gray_image = Image.open("gray.png").convert("L") 
gray_array = np.array(gray_image) 
print("Grayscale Image") 
print("Width:", gray_array.shape[1]) 
print("Height:", gray_array.shape[0]) 
print("Number of color channels:", 1) 
print("Data type:", gray_array.dtype) 
plt.imshow(gray_array, cmap="gray") 
plt.title("Grayscale Image") 
plt.axis("off") 
plt.show() 
# ---------- Color Image ---------- 
color_image = Image.open("color.png").convert("RGB") 
color_array = np.array(color_image) 
r=color_array[:,:,0]

print("\nColor Image") 
print("Width:", color_array.shape[1]) 
print("Height:", color_array.shape[0]) 
print("Number of color channels:", color_array.shape[2]) 
print("Data type:", color_array.dtype) 
plt.imshow(color_array,cmap="Reds") 
plt.title("Color Image") 
plt.axis("off") 
plt.show()

# plt.figure(figsize=(6, 5))
# # plt.subplots_adjust(wspace=0.05, hspace=0)
# # plt.subplot(1,3,1)
# plt.imshow(r,cmap="Reds")
# plt.axis("off")
# plt.show()