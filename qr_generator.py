# qr_generator.py

import qrcode

def generate_qr(url, filename="qrcode.png"):
    # Tạo QR Code
    qr = qrcode.QRCode(
        version=1,  # 1–40, càng cao càng chứa được nhiều dữ liệu
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Chế độ sửa lỗi cao
        box_size=10,  # Kích thước mỗi ô vuông
        border=4,  # Viền
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Tạo hình ảnh từ QR
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR code saved as {filename}")

if __name__ == "__main__":
    url = input("🔗 Enter the URL to generate QR code: ")
    filename = input("💾 Enter filename to save (default: qrcode.png): ").strip()
    if not filename:
        filename = "qrcode.png"
    generate_qr(url, filename)
