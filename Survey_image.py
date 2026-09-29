import matplotlib.pyplot as plt
from PIL import Image

# Image files
files = [
    "xray.jpg",
    "satellite.jpg",
    "microscopy.jpg",
    "ultrasound.png",
    "infrared.jpg"
]

# Modality and application
info = [
    ("X-ray", "Used in hospitals to detect bone fractures."),
    ("Satellite", "Used to observe Earth and monitor land changes."),
    ("Microscopy", "Used to study cells and microorganisms."),
    ("Ultrasound", "Used to examine organs and monitor pregnancy."),
    ("Infrared", "Used for weather monitoring and thermal imaging.")
]

# Display images
for file, (modality, application) in zip(files, info):
    image = Image.open(file)

    print(modality + ":", application)

    plt.imshow(image, cmap="gray")
    plt.title(modality)
    plt.axis("off")
    plt.show()

    