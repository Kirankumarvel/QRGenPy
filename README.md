# 🔲 QRGenPy - QR Code Generator using Python

**QRGenPy** is a minimal and beginner-friendly Python project that generates QR codes from any text or URL. It's perfect for quickly encoding links to blogs, portfolios, contact pages, or any useful data into scannable QR images.

---

## 📸 Demo Output

When you run the script, a file named `qr.png` will be generated with your custom QR code.

---

## 🧰 Features

- ✅ Convert any text or URL into a QR code
- ✅ Saves the QR as a PNG image
- ✅ Lightweight and beginner-friendly
- ✅ No API or internet connection needed

---

## 📦 Requirements

Install the required Python package using pip:

```bash
pip install qrcode[pil]
````

---

## 🚀 Usage

### Step 1: Clone the Repository

```bash
git clone https://github.com/Kirankumarvel/QRGenPy.git
cd QRGenPy
```

### Step 2: Run the Script

```bash
python qr_code_generator.py
```

### 📂 Example Code (`qr_code_generator.py`)

```python
import qrcode

# Data to encode
data = "https://kirankumarvel.wordpress.com/"

# Generate QR code
img = qrcode.make(data)

# Save the image
img.save("qr.png")

print("QR Code generated and saved as 'qr.png'")
```

---

## 📁 Project Structure

```
QRGenPy/
├── qr_code_generator.py
└── README.md
```

---

## 📚 Use Cases

* 🔗 Add QR to resumes, business cards, or flyers
* 📲 Link to your website or blog
* 🧪 Educational or portfolio projects

---

## 🧑‍💻 Author

**Kiran Kumar Vel**
[My WordPress Blog](https://kirankumarvel.wordpress.com/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ⭐️ Like This?

If you found this project useful, consider giving it a ⭐ on GitHub and sharing it!


