from PIL import Image
import os

def encode_image(image_path, output_path, message):
    # Load the input image
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '11111111'  # End-of-message marker

    print("Binary message to encode:", binary_message)  # Debugging output

    # Embed the binary message in the image
    data_index = 0
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            if data_index < len(binary_message):
                pixel = list(pixels[x, y])
                for i in range(3):  # RGB channels
                    if data_index < len(binary_message):
                        pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])
                        data_index += 1
                pixels[x, y] = tuple(pixel)

    # Save the encoded image
    img.save(output_path)
    print(f"Message successfully encoded in {output_path}")

# Paths
input_image_path = "../assets/car.png"
output_image_path = "../assets/encoded_image.png"
message_path = "../assets/secret.txt"

# Check if the input image and message file exist
if os.path.exists(input_image_path) and os.path.exists(message_path):
    with open(message_path, 'r') as file:
        secret_message = file.read().strip()
    encode_image(input_image_path, output_image_path, secret_message)
else:
    print("Input image or message file is missing!")
