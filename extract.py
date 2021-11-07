from PIL import Image
import pytesseract
#import wikipedia
from typing import List


pytesseract.pytesseract.tesseract_cmd = 'c:\\Users\\asunder\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

class ExtractPage:
    
    def __init__(self, path_to_image):
        self.path_to_image = path_to_image
    
    def extract_text(self):
        return pytesseract.image_to_string(Image.open(self.path_to_image))


class Page:
    def __init__(self, *, image_path: str):
        self.image_path = image_path
        self.text = pytesseract.image_to_string(Image.open(self.image_path))

    @property
    def text(self):
        return pytesseract.image_to_string(Image.open(self.image_path))
