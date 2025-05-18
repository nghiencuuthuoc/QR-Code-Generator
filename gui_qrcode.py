import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import qrcode
import os
import win32clipboard
from io import BytesIO

# Global path for QR image
qr_img_path = os.path.join(os.getcwd(), "qrcode.png")

def generate_qr():
    url = url_entry.get().strip()
    if not url:
        result_label.config(text="❌ Please enter a URL", foreground="red")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_img_path)

    img = Image.open(qr_img_path)
    img = img.resize((200, 200), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    result_label.config(text="✅ QR code generated successfully!", foreground="green")
    copy_button["state"] = "normal"

def copy_to_clipboard():
    try:
        img = Image.open(qr_img_path).convert("RGB")
        output = BytesIO()
        img.save(output, "BMP")
        data = output.getvalue()[14:]  # Skip BMP header
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

        result_label.config(text="📋 QR code copied to clipboard", foreground="blue")
    except Exception as e:
        result_label.config(text=f"⚠️ Failed to copy QR: {e}", foreground="red")

# GUI setup
root = tk.Tk()
root.title("QR Code Generator - PharmApp")
root.geometry("400x600")
root.resizable(False, False)

# Logo
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "assets", "nct_logo.png")
try:
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((150, 150), Image.LANCZOS)
    logo_tk = ImageTk.PhotoImage(logo_img)
    logo_label = ttk.Label(root, image=logo_tk)
    logo_label.image = logo_tk
    logo_label.pack(pady=5)
except Exception as e:
    print("⚠️ Logo not found:", e)

# Subtitle
subtitle = ttk.Label(root, text="QR Code Generator for URLs", font=("Arial", 12))
subtitle.pack(pady=2)

# URL Entry
url_label = ttk.Label(root, text="Enter URL:")
url_label.pack(pady=(20, 0))
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

# Generate button
generate_button = ttk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# QR display
qr_label = ttk.Label(root)
qr_label.pack(pady=10)

# Copy button (disabled initially)
copy_button = ttk.Button(root, text="Copy QR Code to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.pack(pady=5)

# Result message
result_label = ttk.Label(root, text="", font=("Arial", 10))
result_label.pack()

# Footer
footer = ttk.Label(root, text="""
| Copyright 2025 | 🧠 Nghiên Cứu Thuốc | PharmApp |
| www.nghiencuuthuoc.com | Zalo: +84888999311 |
""", justify="center", font=("Arial", 9))
footer.pack(side="bottom", pady=10)

root.mainloop()
