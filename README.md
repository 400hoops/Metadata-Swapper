# Metadata Swapper 🖼️ 👉 🖼️

**Metadata Swapper** is a web application that allows you to swap metadata between two images. 📝 This tool is useful when you want to transfer metadata such as EXIF data from one image (e.g., the source image) to another (e.g., the destination image), without altering the image content. 🧼

The app supports multiple image formats like **HEIC**, **PNG**, **TIFF**, and **JPEG**. 🧩  
It also includes **dark mode** 🌙 that remembers your preference using cookies 🍪.

---

## ✨ Features

- 🔄 **Swap metadata** between two images.
- 🖼️ **Supports HEIC, PNG, TIFF, JPEG** formats.
- 🌚 **Dark mode** with persistent theme via cookies.
- 👀 **Live image preview** before swapping.
- ⏳ **Loading indicator** during processing.

---

## 🧰 Technologies Used

- 🐍 **Flask** – Web framework.
- 🖼️ **Pillow (PIL)** – Image handling.
- 📸 **piexif** – EXIF data manipulation.
- 💾 **pyheif** – HEIC image support.
- 🛠️ **ExifTool** – External tool for robust metadata transfer.
- ⚙️ **JavaScript** – Handles UI interactions like preview and dark mode toggle.

---

## 🚀 Installation

### 📦 Prerequisites

- Python 3.x 🐍
- `pip` (Python package manager) 📦

### 🛠️ Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/400hoops/metadata-swapper.git
    cd metadata-swapper
    ```

2. **Create a virtual environment** *(optional but recommended)*:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install ExifTool**:
   - Download from [exiftool.org](https://exiftool.org/)
   - Ensure `exiftool` is in your system’s PATH 🔍

5. **Run the Flask app**:
    ```bash
    python app.py
    ```

6. 🌐 Open `http://127.0.0.1:5000` in your browser.

---

## 📁 Folder Structure

metadata-swapper/
- app.py # Main Flask application
- templates/ # HTML templates (index.html, success.html)
- static/ # CSS & JavaScript
  - style.css
- uploads/ # Uploaded image storage
- Requirements.txt # Python dependencies
- README.md # You're here!


---

## 🌙 Dark Mode

Toggle the dark mode via the button 🌗 in the top-right corner.  
Your theme preference is saved in cookies, so it stays consistent between visits 🍪.

---

## 🧪 Metadata Swapping Flow

1. Drag and drop or select a **source image** (with metadata).
2. Upload a **destination image**.
3. Click **Swap Metadata** 🔁.
4. Download your new image with updated metadata 💾.

---

## 🤝 Contributing

1. Fork the repo 🍴
2. Create a branch (`git checkout -b feature-name`)
3. Make your changes ✅
4. Commit (`git commit -am 'Add feature'`)
5. Push (`git push origin feature-name`)
6. Submit a Pull Request 🚀

---

## 📜 License

Licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- 🛠️ [ExifTool](https://exiftool.org/) – For robust metadata editing.
- 🔥 Flask – Fast and lightweight backend.
- 🖼️ Pillow – Image manipulation.
- 💡 piexif & pyheif – Metadata and HEIC support.

---

Have fun swapping your image metadata! 🖼️✨
