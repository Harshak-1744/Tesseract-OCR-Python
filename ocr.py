import subprocess

def ocr(image_path, output_text_path):
    try:
        # Specify the full path to the Tesseract executable
        tesseract_executable = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Run Tesseract OCR command using subprocess
        subprocess.run([tesseract_executable, image_path, output_text_path], capture_output=True, text=True)
        
        # Read the extracted text from the output text file
        with open(output_text_path, 'r', encoding='utf-8') as file:
            extracted_text = file.read()
        
        return extracted_text
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
image_path = 'testocr.jpg'
output_text_path = 'output.txt'
text = ocr(image_path, output_text_path)
print(text)
