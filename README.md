# Tesseract-OCR-Python

Tesseract-OCR-Python is a simple Python script that leverages the Tesseract OCR engine to perform Optical Character Recognition (OCR) on images and extract text from them.

## Prerequisites

Before using this script, ensure you have Tesseract OCR installed on your system. You can download and install it from the official [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).

## Installation

1. Install Tesseract OCR by following the instructions provided in the [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).

2. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/Harshak-1744/Tesseract-OCR-Python.git
   ```

3. Navigate to the repository's directory:

   ```bash
   cd Tesseract-OCR-Python
   ```

## Usage

1. Place the image you want to perform OCR on in the same directory as the `ocr.py` script.

2. Open a terminal or command prompt and navigate to the repository's directory.

3. Run the script using the following command:

   ```bash
   python ocr.py <image_path> <output_text_path>
   ```

   Replace `<image_path>` with the path to the input image and `<output_text_path>` with the desired path for the extracted text output.

4. The extracted text will be saved to the specified output text file.

## Example

```bash
python ocr.py testocr.jpg output.txt
```
