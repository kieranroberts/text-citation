from PIL import Image
import pytesseract
class Page:
    def __init__(self, *, image_path: str, pytesseract_cmd: str):
        self.image_path = image_path
        pytesseract.pytesseract.tesseract_cmd = self.pystessreact
        self.text = pytesseract.image_to_string(Image.open(self.image_path))

    @property
    def text(self):
        return pytesseract.image_to_string(Image.open(self.image_path))
