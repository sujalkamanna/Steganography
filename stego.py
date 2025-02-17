import cv2
import os

# Provide the full path to the image
img = cv2.imread(r"C:\Users\Sujal\Desktop\Steganography\input\input_file.png")  # Replace with the correct image path

# Check if the image was loaded properly
if img is None:
    print("Error: Unable to load image. Check the file path.")
    exit(1)  # Exit the program if image can't be loaded

# Get image dimensions (height, width, channels)
height, width, _ = img.shape

# Input secret message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Ensure the image is large enough to hold the message
max_message_length = height * width * 3  # 3 because there are 3 color channels (RGB)

if len(msg) > max_message_length:
    print(f"Error: Message is too large to fit in the image. Maximum message length is {max_message_length} characters.")
    exit(1)  # Exit if the message is too large for the image

# Create dictionaries for character encoding and decoding
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Hide the message in the image
m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]  # Embed the ASCII value of the character
    n = n + 1
    m = m + 1
    z = (z + 1) % 3  # Move through the RGB channels

# Save the modified image with the hidden message
cv2.imwrite(r"C:\Users\Sujal\Desktop\Steganography\output\encryptedImage.png", img)

# Open the image using the default viewer (Windows 'start' command)
os.system(r"start C:\Users\Sujal\Desktop\Steganography\output\encryptedImage.png")

# Decrypt the message
message = ""
n = 0
m = 0
z = 0

# Ask for the passcode for decryption
pas = input("Enter passcode for Decryption: ")

# Check if the entered passcode matches the original one
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]  # Decode the hidden message
        n = n + 1
        m = m + 1
        z = (z + 1) % 3  # Move through the RGB channels
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized!")
