from PIL import Image

# Open the image file
original_image = Image.open("new.jpg")

# Define the number of images you want to create
num_images = 10

# Loop to create multiple images
for i in range(num_images):
    # Create a copy of the original image
    new_image = original_image.copy()

    # Modify the new image (e.g., resize, rotate, apply filters, etc.)
    # For demonstration purposes, let's rotate each new image by a small angle
    angle = i * (0 / num_images)
    rotated_image = new_image.rotate(angle)

    # Save the new image with a different filename
    rotated_image.save(f"image_{i}.jpg")

    # Optionally, you can also show or display the images
    # rotated_image.show()
