# Steganography Exercise for Forensic Students

This repository provides a hands-on exercise for forensic students to understand and practice steganography by hiding and extracting information within graphic files.

## Objectives
- Learn how to hide data in image files using the Least Significant Bit (LSB) method.
- Extract hidden data from an encoded image.
- Understand the role of steganography in cybersecurity and digital forensics.

## Repository Structure
```
Steganography-Exercise
│
├── README.md               # Instructions and details about the exercise
├── scripts
│   ├── encode_image.py      # Script to hide a message in an image
│   ├── decode_image.py      # Script to extract the hidden message
├── assets
│   ├── input_image.png      # Sample input image
│   ├── secret.txt           # File containing the secret message
│   ├── encoded_image.png    # Encoded image (generated after encoding)
├── .gitignore               # Ignore unnecessary files
```

## Prerequisites
- Python 3.x installed on your system.
- Required Python library: `Pillow`.

Install the library using:
```bash
pip install Pillow
```

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Steganography-Exercise.git
   cd Steganography-Exercise
   ```

2. Navigate to the `scripts` directory:
   ```bash
   cd scripts
   ```

3. Replace `input_image.png` in the `assets` folder with your own image if desired.
4. Edit the `secret.txt` file in the `assets` folder to include the message you want to hide.

## Usage

### Encoding a Message
To hide a secret message in an image, run the `encode_image.py` script:
```bash
python encode_image.py
```

This will generate an `encoded_image.png` in the `assets` folder with the hidden message.

### Decoding a Message
To extract the hidden message from the encoded image, run the `decode_image.py` script:
```bash
python decode_image.py
```

## Assignment
- **Task 1**: Encode a text message into an image.
- **Task 2**: Decode the hidden message from the image and verify its accuracy.
- **Task 3**: Write a brief report on the effectiveness of steganography in digital forensics.

## Discussion Points
- What are the implications of steganography in cybersecurity and digital forensics?
- What challenges did you face during this exercise?

## License
This project is licensed under the MIT License.
