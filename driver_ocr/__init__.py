from driver_ocr.body import Drive_OCR
from driver_ocr.txt_writer import Txt
import os


def text_from_image(image_path):
    ob = Drive_OCR(image_path)
    text = ob.main()
    return text

