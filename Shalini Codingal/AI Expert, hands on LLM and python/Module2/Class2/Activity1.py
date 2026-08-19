import cv2

# Store the image path
image_path = "/Users/shaliniprasad/Downloads/wild_animal_picture_relaxing_tiger_6934816.jpg"

# Read the image
img = cv2.imread(image_path)



# Check if the image exists
if img is None:
    print("Error: Unable to load the image.")
else:
    # Window settings
    window_name = "Wild Tiger Image"
    window_width = 800
    window_height = 500

    # Create a resizable window
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # Set the window size
    cv2.resizeWindow(window_name, window_width, window_height)

    # Show the image
    cv2.imshow(window_name, img)

    # Print image information
    height, width, channels = img.shape
    print("Image Height :", height)
    print("Image Width  :", width)
    print("Channels     :", channels)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()