from PIL import Image
import os

def scale_image(input_path):
    # Open the image file
    with Image.open(input_path) as img:
        # Scale down the image by 80%
        new_size = (int(img.width * 0.2), int(img.height * 0.2))
        img = img.resize(new_size, Image.ANTIALIAS)
        
        # Save the image as a .fart file
        output_path = os.path.splitext(input_path)[0] + '.fart'
        img.save(output_path, format='PNG')  # Using PNG format for .fart file
        
    return output_path

# Example usage
input_image_path = 'path/to/your/image.jpg'
scaled_image_path = scale_image(input_image_path)
print(f'Scaled image saved as: {scaled_image_path}')
