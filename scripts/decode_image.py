from PIL import Image
import os

def decode_image(image_path):
    # Load the encoded image
    img = Image.open(image_path)
    binary_message = ''

    # Extract the binary message
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            for i in range(3):  # RGB channels
                binary_message += str(pixel[i] & 1)

    # Debug: Print the first 100 bits of the binary message
    print("Extracted binary message (first 100 bits):", binary_message[:100])

    # Convert binary message to text
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if byte == '11111111':  # End of message marker
            break
        try:
            message += chr(int(byte, 2))
        except ValueError:
            print(f"Invalid byte encountered: {byte}")
            break

    return message

# Path
encoded_image_path = "../assets/encoded_image.png"

# Check if the encoded image exists
if os.path.exists(encoded_image_path):
    hidden_message = decode_image(encoded_image_path)
    print("Hidden message:", hidden_message)
else:
    print("Encoded image file is missing!")
