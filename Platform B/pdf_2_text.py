import os
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import time
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
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

def pdf_to_txt(pdf_path, text_file_path):
    print(pdf_path)
    PDF_file = pdf_path
    # Store all the pages of the PDF in a variable
    image_file_list = []
    with TemporaryDirectory() as tempdir:
        if platform.system() == "Windows":
            pdf_pages = convert_from_path(
                PDF_file, 350, poppler_path=path_to_poppler_exe
            )
        else:
            pdf_pages = convert_from_path(PDF_file, 500)
        # Read in the PDF file at 500 DPI

        # Iterate through all the pages stored above
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            # enumerate() "counts" the pages for us.

            # Create a file name to store the image
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            
            page.save(filename, "JPEG")
            image_file_list.append(filename)

        """
        Part #2 - Recognizing text from the images using OCR
        """
        # print('Converting ' + pdf_path)
        with open(text_file_path, "a") as output_file:
            for image_file in image_file_list:
                print(image_file_list.index(image_file), len(image_file_list))
                text = str(((pytesseract.image_to_string(Image.open(image_file)))))
                text = text.replace("-\n", "")

                # Finally, write the processed text to the file.
                output_file.write(text)


pdf_files = [x for x in os.listdir(r'C:\Users\Tahsin Sayed\Desktop\Image_to_text\Platform B\All Files') if '.pdf' in x]
for x in pdf_files:
    print(pdf_files.index(x), len(pdf_files))
    try:
        image_file_path = 'C:\\Users\\Tahsin Sayed\\Desktop\\Image_to_text\\Platform B\\All Files\\' + x
        if 'document_1' in x:        
            text_file_path = 'C:\\Users\\Tahsin Sayed\\Desktop\\Image_to_text\\Platform B\\All Files\\Form C\\' + x.split('.pdf')[0] + '.txt'
            if os.path.exists(text_file_path):
                continue
            pdf_to_txt(image_file_path, text_file_path)
        elif 'document_2' in x: 
            text_file_path = 'C:\\Users\\Tahsin Sayed\\Desktop\\Image_to_text\\Platform B\\All Files\\Pitch\\' + x.split('.pdf')[0] + '.txt'
            if os.path.exists(text_file_path):
                continue
            pdf_to_txt(image_file_path, text_file_path)
        
    except Exception as e:
        print(e)
