from RRPA.Modules.Core.Abstract.ObjectScanning.ObjectTextifier import AbstractObjectTextifier
import pytesseract
import cv2
import numpy as np


pytesseract.pytesseract.tesseract_cmd = r'D:\Programms\Tesseract-OCR-5.3\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "D:\Programms\Tesseract-OCR-5.3\tessdata"'


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


def preprocess(image):
    image = get_grayscale(image)
    image = cv2.bilateralFilter(image, 11, 17, 17)  # Blur to reduce noise
    #image = cv2.GaussianBlur(image, (3, 3), 0)
    return image


class STDCVObjectTextifier(AbstractObjectTextifier):

    def textify(self, _object):
        img = preprocess(_object)
        text = pytesseract.image_to_string(img, lang='rus', config=tessdata_dir_config) # lang=rus
        text = text.strip()
        print("text=", text)
        return text
