import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("/Users/shaliniprasad/Downloads/wild_animal_picture_relaxing_tiger_6934816.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load the image. Please check the file path.")
else:
    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("RGB Image")
    plt.axis("off")
    plt.show()

    # Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")
    plt.show()

    # Crop the image
    # Rows 100 to 300, Columns 200 to 400
    cropped_image = image[100:300, 200:400]

    # Convert cropped image to RGB for display
    cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
    plt.imshow(cropped_rgb)
    plt.title("Cropped Region")
    plt.axis("off")
    plt.show()