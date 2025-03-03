from PIL import Image
import os

def encode_image(image_path, message_path, output_path):
    # Load the image
    img = Image.open(image_path)
    encoded = img.copy()

    # Read the secret message
    with open(message_path, 'r') as file:
        message = file.read()
    binary_message = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'  # End of message marker
    data_index = 0

    # Encode the message into the image
    for y in range(img.height):
        for x in range(img.width):
            pixel = list(img.getpixel((x, y)))
            for i in range(3):  # RGB channels
                if data_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
            encoded.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    # Save the encoded image
    encoded.save(output_path)
    print(f"Message successfully encoded in {output_path}")

# Paths
image_path = "../assets/emas7.jpg"
message_path = "../assets/secret.txt"
output_path = "../assets/encoded_image.jpg"

# Check if files exist
if os.path.exists(image_path) and os.path.exists(message_path):
    encode_image(image_path, message_path, output_path)
else:
    print("Input image or secret message file is missing!")
