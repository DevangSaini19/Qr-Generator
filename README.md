# QR Code Generator in Python

A simple Python project that generates a QR code from a text string using the **qrcode** library.

## 📌 Features

* Generate QR codes from any text or URL.
* Save the generated QR code as a PNG image.
* Beginner-friendly and easy to customize.

## 📂 Project Structure

```
.
├── main.py
├── qrcode.png
└── README.md
```

## 🛠️ Requirements

* Python 3.x
* qrcode
* Pillow (required for image generation)

Install the required package:

```bash
pip install "qrcode[pil]"
```

## 🚀 Usage

1. Clone the repository.

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Run the Python file.

```bash
python main.py
```

3. After execution, a file named **`qrcode.png`** will be created in the project directory.

## 💻 Example Code

```python
import qrcode

data = "I love coding"

qr = qrcode.make(data)

qr.save("qrcode.png")

print("QR Code Generated Successfully")
```

## 📷 Output

Input:

```
I love Coding
```

Output:

```
QR Code Generated Successfully
```

Generated File:

```
qrcode.png
```

## 🎯 Future Improvements

* Generate QR codes from URLs.
* Customize QR code colors.
* Change the size and border of the QR code.
* Add a logo in the center of the QR code.
* Create a simple GUI using Tkinter.
* Build a web version using Flask or Django.

## 📄 License

This project is open source and available under the MIT License.
