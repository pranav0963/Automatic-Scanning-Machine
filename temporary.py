import cv2
import OCR
import os
from PIL import Image
from docx import Document
import Writing_into_word

captured_images = []

url = "http://192.168.66.167:8080/video" # Camera1
url2 ="http://192.168.161.131:8080/video" # Camera2

document = Document()

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(0)

while True:
    ret1, frame1 = cap.read()
    ret2, frame2 = cap2.read()

    # Showing image
    cv2.imshow('WebCam', frame1)
    cv2.imshow('WebCam1', frame2)

    if cv2.waitKey(1) == ord("c"):

        # Writing image
        cv2.imwrite("image_1.jpg", frame1)
        cv2.imwrite("image_2.jpg", frame2)

        # Reading image
        img1 = Image.open("image_1.jpg")
        img2 = Image.open("image_1.jpg")

        # Appending to pdf
        text1 = OCR.ocr(img1)
        text2 = OCR.ocr(img2)

        # Writing to docx
        document = Writing_into_word.write(text1, document)
        document = Writing_into_word.write(text2, document)
        document.save("word.docx")

    if cv2.waitKey(1) == ord('q'):
        os.remove("image_1.jpg")
        os.remove("image_2.jpg")
        break

cv2.destroyAllWindows()
cap.release()
cap2.release()
