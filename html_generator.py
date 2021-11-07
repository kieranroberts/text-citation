from jinja2 import Environment, FileSystemLoader
import os
from sentence import Sentence
import pickle

template_dir = 'c:/users/asunder/Code/text-citation/'
output_dir = 'c:/users/asunder/Code/text-citation/book/text/'
home_dir = 'c:/users/asunder/Code/text-citation/book/'

#sentence = Sentence(content='asd')

file_loader = FileSystemLoader(os.path.join(template_dir,'templates'))
env = Environment(loader=file_loader)

template = env.get_template('about.html')


with open(os.path.join(home_dir,'book5.p'), 'rb') as fileobj:
    sentences  = pickle.load(fileobj)

output = template.render(sentences=sentences)

path_to_output = os.path.join(output_dir, 'test_page.html')
with open(path_to_output, 'w', encoding="utf-8") as f:
    f.write(output)