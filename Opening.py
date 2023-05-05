import os
from pdf2image import convert_from_path
import OCR
from docx import Document
import cv2

import Writing_into_word

document = Document()


#
#
# def convert(file):
#     pages = convert_from_path(file, 500 )
#     for page in pages:
#
#
#
# class object:
#     def __init__(self, file):
#         self.file = file
#
#     def open(self):
#         pass

def ocr(self):
    global document
    pages = convert_from_path(self, 500)
    i = 0
    for page in pages:
        if not os.path.exists('hidden/'):
            os.mkdir("hidden/")
        page.save(f'hidden/image{i}.jpg', "JPEG")
        document = Writing_into_word.write((OCR.ocr(cv2.imread(f'hidden/image{i}.jpg'))), document)
        os.remove(f'hidden/image{i}.jpg')

document.save("word.docx")
ocr("name.pdf")


