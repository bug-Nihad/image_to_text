import os
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import time
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
# PDF_file = pdf_path
# Windows also needs poppler_exe
path_to_poppler_exe = Path(r"C:\poppler-0.68.0\bin")

print('Hello')
def to_text(file_path, text_file):
    print(file_path)
    text = str(((pytesseract.image_to_string(Image.open(file_path)))))
    with open(text_file, 'a') as file:
        file.write(text)
        print('Done')



image_files = [x for x in os.listdir() if '.jpg' in x]


for x in image_files:
    try:
        image_file_path = x
        text_file_path = 'Yonder' + '.txt'
        to_text(image_file_path, text_file_path)
    except Exception as e:
        print(e)
    
