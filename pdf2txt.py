import os
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import time
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def ocr(pdf_path):
    pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    PDF_file = pdf_path
    # Windows also needs poppler_exe
    path_to_poppler_exe = Path(r"C:\poppler-0.68.0\bin")

    # Put our output files in a sane place...
    out_directory = Path(r'C:\Users\Tahsin Sayed\Desktop\Image_to_text\Form C\Output Text File')

    # Store all the pages of the PDF in a variable
    image_file_list = []
    text_file = r'C:\Users\Tahsin Sayed\Desktop\Image_to_text\Form C\Output Text File\\' + pdf_path.rsplit('\\', 1)[-1].split('.pdf', 1)[0] + ".txt"

    print(text_file)
    with TemporaryDirectory() as tempdir:
        if platform.system() == "Windows":
            
            print('Hello')
            
            pdf_pages = convert_from_path(
                PDF_file, 350, poppler_path=path_to_poppler_exe, fmt="jpeg"
            )

            print('Hello')
            
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
        with open(text_file, "a", encoding='utf-8') as output_file:
            for image_file in image_file_list:
                print(image_file_list.index(image_file), len(image_file_list))
                text = str(((pytesseract.image_to_string(Image.open(image_file)))))

                text = text.replace("-\n", "")


                # Finally, write the processed text to the file.
                output_file.write(text)





for i in range(2):
    for x in os.listdir(r'Form C'):
        if '.pdf' not in x:
            print(x)
            continue

        #Check log file whether x is done converted. 
        
        log_path = r'C:\Users\Tahsin Sayed\Desktop\Image_to_text\Form C\log.txt'
        
        with open(log_path, 'r') as log_file:
            if x + '\n' in log_file.readlines():
                print(x , ' is done already.')
                continue
        file_path = os.getcwd() + '\Form C\\' + x
        # print(Path(file_path))
        # print(Path(file_path).rstrip('\\', 1))
        try:
            ocr(file_path)

            #Append log file with x 
            with open(log_path, 'a') as log_file:
                log_file.write(x + '\n')
                print(x, ' is done and logged.')

        except Exception as e:
            print(e)
            pass 
