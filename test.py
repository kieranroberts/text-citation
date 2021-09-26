from write import ExtractBook
import os

home_dir = 'c:/Users/asunder/Code/text-citation/book'
num_pages = 70
page_ordering = dict()

for i in range(1,num_pages+1):
    page_ordering[i] = '{}.png'.format(i)
    
path_to_output = os.path.join(home_dir,'text', 'book_of_craig.txt')

book = ExtractBook(page_ordering=page_ordering, 
                   home_dir=home_dir, 
                   num_pages=num_pages)