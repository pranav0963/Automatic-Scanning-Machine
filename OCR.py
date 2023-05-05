import cv2
import numpy as np
import pytesseract as pyt



def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    return (image)


def ocr(image):
    # Setting parameters
    PSM = 6
    OEM = 3
    myconfig = r"--psm {} --oem {}".format(PSM, OEM)

    # Converting to grayscale
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Rotating
    img_rotated = cv2.rotate(imgGray, rotateCode=0)
    # Noise removal
    img_final = noise_removal(img_rotated)
    # text
    text = pyt.image_to_string(img_final, config=myconfig)

    return text
