from PIL import Image

# Load the 4K image
img_path = 'image.jpg'  # Ensure this file is in the same directory
img = Image.open(img_path)

# Resize the image to 128x128
img_resized = img.resize((128, 128))

# Save the resized image
img_resized.save('resized_image_128x128.jpg')

# Display the resized image
img_resized.show()

# Load the 128x128 image
img_path_128 = 'resized_image_128x128.jpg'
img_128 = Image.open(img_path_128)

# Upscale the image to 4K (3840x2160)
img_upscaled = img_128.resize((3840, 2160))

# Save the upscaled image
img_upscaled.save('upscaled_image_4K.jpg')

# Display the upscaled image
img_upscaled.show()
