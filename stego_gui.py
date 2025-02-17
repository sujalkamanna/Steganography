import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

class SteganographyApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Image Steganography")
        self.window.geometry("800x750")  # Reduced height
        self.window.configure(bg="#f0f5f9")
        self.img = None
        self.setup_styles()
        self.setup_gui()

    def setup_styles(self):
        style = ttk.Style()
        style.configure('Custom.TButton',
                       font=('Helvetica', 9, 'bold'),
                       padding=5)  # Reduced padding
        
        style.configure('Title.TLabel',
                       font=('Helvetica', 20, 'bold'),  # Reduced font size
                       background='#f0f5f9',
                       foreground='#1e3d59')
        
        style.configure('Subtitle.TLabel',
                       font=('Helvetica', 10),  # Reduced font size
                       background='#f0f5f9',
                       foreground='#1e3d59')

        style.configure('TLabelframe', background='#f0f5f9')
        style.configure('TLabelframe.Label', 
                       background='#f0f5f9', 
                       font=('Helvetica', 9, 'bold'))  # Reduced font size

    def setup_gui(self):
        main_frame = ttk.Frame(self.window)
        main_frame.pack(padx=10, pady=5, fill='both', expand=True)  # Reduced padding

        # Title section
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill='x', pady=(0, 10))  # Reduced padding
        
        title_label = ttk.Label(title_frame, 
                               text="Image Steganography",
                               style='Title.TLabel')
        title_label.pack()

        # Image Frame
        self.image_frame = ttk.LabelFrame(main_frame, text="Image Preview")
        self.image_frame.pack(pady=5, padx=5, fill='both')  # Reduced padding

        # Select Image Button
        self.select_btn = ttk.Button(self.image_frame,
                                   text="Select Image",
                                   style='Custom.TButton',
                                   command=self.select_image)
        self.select_btn.pack(pady=5)  # Reduced padding

        # Selected Image Path Label
        self.path_label = ttk.Label(self.image_frame,
                                  text="No image selected",
                                  wraplength=700)
        self.path_label.pack(pady=2)  # Reduced padding

        # Image preview label
        self.image_label = ttk.Label(self.image_frame)
        self.image_label.pack(pady=5)  # Reduced padding

        # Create a frame for encryption and decryption side by side
        operation_frame = ttk.Frame(main_frame)
        operation_frame.pack(fill='both', expand=True, pady=5)

        # Encryption Frame (Left side)
        encrypt_frame = ttk.LabelFrame(operation_frame, text="Encryption")
        encrypt_frame.pack(side='left', pady=5, padx=5, fill='both', expand=True)

        # Message Entry
        ttk.Label(encrypt_frame, text="Enter Secret Message:",
                 style='Subtitle.TLabel').pack(pady=2)
        self.msg_entry = ttk.Entry(encrypt_frame, width=40)
        self.msg_entry.pack(pady=2)

        # Password Entry
        ttk.Label(encrypt_frame, text="Enter Password:",
                 style='Subtitle.TLabel').pack(pady=2)
        self.pass_entry = ttk.Entry(encrypt_frame, width=40, show="*")
        self.pass_entry.pack(pady=2)

        # Encrypt Button
        self.encrypt_btn = ttk.Button(encrypt_frame,
                                    text="Encrypt and Save",
                                    style='Custom.TButton',
                                    command=self.encrypt_and_save)
        self.encrypt_btn.pack(pady=5)

        # Decryption Frame (Right side)
        decrypt_frame = ttk.LabelFrame(operation_frame, text="Decryption")
        decrypt_frame.pack(side='right', pady=5, padx=5, fill='both', expand=True)

        # Decrypt Password Entry
        ttk.Label(decrypt_frame, text="Enter Password for Decryption:",
                 style='Subtitle.TLabel').pack(pady=2)
        self.decrypt_pass_entry = ttk.Entry(decrypt_frame, width=40, show="*")
        self.decrypt_pass_entry.pack(pady=2)

        # Decrypt Button
        self.decrypt_btn = ttk.Button(decrypt_frame,
                                    text="Decrypt",
                                    style='Custom.TButton',
                                    command=self.decrypt_message)
        self.decrypt_btn.pack(pady=5)

        # Result Frame
        result_frame = ttk.LabelFrame(main_frame, text="Result")
        result_frame.pack(pady=5, padx=5, fill='both')

        self.result_label = ttk.Label(result_frame,
                                    text="",
                                    wraplength=700)
        self.result_label.pack(pady=5)

    def show_image(self, image_path):
        try:
            image = Image.open(image_path)
            
            # Set a max width for the preview, and maintain aspect ratio
            max_width = 400  # Maximum width for display
            aspect_ratio = image.width / image.height
            new_width = min(image.width, max_width)
            new_height = int(new_width / aspect_ratio)
            
            # Ensure the height is not too large
            max_height = 400  # Maximum height for display
            if new_height > max_height:
                new_height = max_height
                new_width = int(max_height * aspect_ratio)
            
            # Resize the image
            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying image: {str(e)}")

    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp"), ("All files", "*.*")]
        )
        if file_path:
            self.img = cv2.imread(file_path)
            if self.img is not None:
                self.path_label.config(text=f"Selected: {file_path}")
                self.show_image(file_path)
            else:
                messagebox.showerror("Error", "Failed to load image")

    def encrypt_and_save(self):
        if self.img is None:
            messagebox.showerror("Error", "Please select an image first!")
            return

        msg = self.msg_entry.get()
        password = self.pass_entry.get()

        if not msg or not password:
            messagebox.showerror("Error", "Please enter both message and password!")
            return

        d = {chr(i): i for i in range(255)}
        m = n = z = 0
        encrypted_img = self.img.copy()
        
        try:
            for i in range(len(msg)):
                encrypted_img[n, m, z] = d[msg[i]]
                n = n + 1
                m = m + 1
                z = (z + 1) % 3

            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
            )

            if save_path:
                cv2.imwrite(save_path, encrypted_img)
                self.img = encrypted_img
                messagebox.showinfo("Success", "Image encrypted and saved successfully!")
                self.show_image(save_path)

        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt_message(self):
        if self.img is None:
            messagebox.showerror("Error", "Please select the encrypted image first!")
            return

        input_password = self.decrypt_pass_entry.get()
        original_password = self.pass_entry.get()
        
        if not input_password:
            messagebox.showerror("Error", "Please enter the decryption password!")
            return

        if input_password != original_password:
            messagebox.showerror("Error", "Incorrect password!")
            return

        try:
            # Create decoding dictionary
            c = {i: chr(i) for i in range(255)}
            
            # Decrypt message
            message = ""
            n = m = z = 0
            msg_length = len(self.msg_entry.get())

            for i in range(msg_length):
                message += c[self.img[n, m, z]]
                n = n + 1
                m = m + 1
                z = (z + 1) % 3

            # Update result with decrypted message
            self.result_label.config(
                text=f"Decrypted message: {message}",
                foreground='#1e3d59',
                font=('Helvetica', 12)
            )

        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def run(self):
        # Center the window on the screen
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
        
        # Add a custom icon (optional)
        try:
            self.window.iconbitmap('icon.ico')  # Replace with your icon path
        except:
            pass
        
        self.window.mainloop()

def main():
    app = SteganographyApp()
    app.run()

if __name__ == "__main__":
    main()
