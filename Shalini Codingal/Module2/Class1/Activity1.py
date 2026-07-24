import cv2

image_path = "/Users/shaliniprasad/Downloads/wild_animal_picture_relaxing_tiger_6934816.jpg"
image = cv2.imread(image_path)

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 800, 500)

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")