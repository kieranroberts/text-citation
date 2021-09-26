from PIL import Image
import pytesseract
#import wikipedia

pytesseract.pytesseract.tesseract_cmd = 'c:\\Users\\asunder\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

class ExtractPage:
    
    def __init__(self, path_to_image):
        self.path_to_image = path_to_image
    
    def extract_text(self):
        return pytesseract.image_to_string(Image.open(self.path_to_image))