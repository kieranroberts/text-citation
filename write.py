from extract import ExtractPage
import os
import re

class ExtractBook:
    
    def __init__(self, page_ordering, home_dir, num_pages, title):
        self.page_ordering = page_ordering # dictionary {1 : 'page_1.png', etc.}
        self.home_dir = home_dir
        self.num_pages = num_pages
        self.full_book = None
        self.title = title
        self.text = self.convert_book_to_text()
    
    def convert_book_to_text(self):
        total_str = str()
        for i in range(1,self.num_pages+1):
            path_to_image = os.path.join(self.home_dir, self.page_ordering[i])
            page_extractor = ExtractPage(path_to_image=path_to_image)
            total_str +=  page_extractor.extract_text()
        
        self.full_book = total_str
    
    def clean_book_text(self):
        self.full_book = re.sub(r"([0-9]+\.)([A-Za-z]+)", r"\g<1> \g<2>", self.full_book)
        self.full_book = re.sub(r"([A-Za-z]+\.)([A-Za-z]+)", r"\g<1> \g<2>", self.full_book)
        self.full_book = re.sub(r"([0-9]+\.)([0-9]{1}[A-Za-z]+)", r"\g<1> \g<2>", self.full_book)
        self.full_book = re.sub(r"\x0c", "", self.full_book)
        self.full_book = re.sub(self.title, "", self.full_book)
        self.full_book = self.title + "\n\n" + self.full_book
    
    def reorder_contents_page(self):
        pass
    
    def write_full_book_to_file(self, path_to_output):
        with open(path_to_output, 'w') as txt:
            txt.write(self.full_book)
            

book.save()

# pip install black  # formatter