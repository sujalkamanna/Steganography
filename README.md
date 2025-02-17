# Steganography

Steganography is the technique of hiding secret data within a non-secret object, like text, images, or audio, to avoid detection.
Here’s a sample **README** for your steganography project repository on GitHub:

---

# Steganography in Python

This is a simple Python-based steganography tool that hides a secret message within the pixels of an image. The message can be decrypted by providing the correct passcode.

## Features
- Hide a secret message inside an image.
- Encrypt the message with a passcode.
- Decrypt the message using the correct passcode.
- The image is modified without visibly changing the content, allowing for invisible data storage.

## Prerequisites

- Python 3.x
- OpenCV library (for image processing)
  
You can install OpenCV using pip:

```bash
pip install opencv-python
```

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sujalkamanna/Steganography.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Steganography
   ```

3. Install the required dependencies:

   ```bash
   pip install opencv-python
   ```

## Usage

### 1. Hide a Secret Message in an Image

1. Place the image you want to use in the `input` folder (e.g., `input_file.png`).
2. Run the script:

   ```bash
   python steganography.py
   ```

3. The program will prompt you for:
   - The **secret message** you want to hide.
   - A **passcode** that will be used to decrypt the message.

4. After entering the secret message and passcode, the program will:
   - Embed the secret message inside the image.
   - Save the modified image as `encryptedImage.png` in the `output` folder.

5. The image will be opened using your default image viewer, and the modified image will not visually show any difference.

### 2. Decrypt the Hidden Message

1. To decrypt the hidden message, run the script again, and provide the correct passcode.
2. If the passcode matches, the program will extract and display the secret message embedded in the image.

### Example Output

```plaintext
Enter secret message: Hello, this is a secret message!
Enter a passcode: mysecurepass
Decrypted message: Hello, this is a secret message!
```

## File Structure

```
Steganography/
│
├── input/
│   └── input_file.png       # Your input image file
│
├── output/
│   └── encryptedImage.png   # The image with the embedded message
│
├── steganography.py         # Main Python script
└── README.md                # This file
```

## How it Works

- **Encoding**: The ASCII values of the characters in the secret message are embedded into the image's RGB pixel values. Each character is encoded into the image by altering the pixel values across the image's width, height, and RGB channels.
  
- **Decoding**: When decrypting, the script reads the pixel values from the image, converts them back to their respective ASCII values, and reconstructs the original message.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README includes instructions for setting up, using the tool, and understanding how it works. You can modify it as needed based on additional features or changes you make to the project.