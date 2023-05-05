import cv2
import Scan
import os
from PIL import Image
import time
import socket

serverAddressPort = ("192.168.141.176", 4210)

UDPClientSocket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)


def liftGlass():
    UDPClientSocket.sendto(str.encode("2"), serverAddressPort)
    time.sleep(5)


def stop():
    UDPClientSocket.sendto(str.encode("0"), serverAddressPort)


def down():
    UDPClientSocket.sendto(str.encode("1"), serverAddressPort)
    time.sleep(5)


pdf = Scan.PdfFile("name.pdf")
captured_images = []

url = "http://192.168.222.7:8080/video"  # Camera1
url2 = "http://192.168.222.131:8080/video"  # Camera2

# cap = cv2.VideoCapture(url2)
cap2 = cv2.VideoCapture(0)


async def video():
    while True:
        ret, frame = cap2.read()
        await cv2.imshow('WebCam1', frame)


while True:
    print("yes")
    # ret1, frame1 = cap.read()
    ret2, frame2 = cap2.read()

    # Showing image
    # cv2.imshow('WebCam', frame1)
    # cv2.imshow('WebCam1', frame2)

    # if cv2.waitKey(1) == ord("c"):

    # Bringing the glass down
    down()
    stop()
    # Writing image
    if not os.path.exists("hidden/"):
        os.mkdir("hidden/")
    # cv2.imwrite("hidden//image_1.jpg", frame1)
    cv2.imwrite("hidden//image_2.jpg", frame2)
    cv2.imshow("hidden//image_2.jpg", frame2)
    liftGlass()
    stop()

    # Reading image
    # img1 = Image.open("hidden//image_1.jpg")
    img2 = Image.open("hidden//image_2.jpg")
    img2 = img2.rotate(angle=270, expand=True)

    # Appending to pdf
    # img1converted = img1.convert('RGB')
    img2converted = img2.convert('RGB')
    # captured_images.append(img1converted)
    captured_images.append(img2converted)

    # Writing to docx

    if cv2.waitKey(1) == ord('q'):
        # os.remove("hidden/image_1.jpg")
        os.remove("hidden/image_2.jpg")
        pdf.save(captured_images, img2converted)
        break
# cap.release()
cap2.release()
cv2.destroyAllWindows()
