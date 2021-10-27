from jinja2 import Environment, FileSystemLoader
import os

from sentence import Sentence

template_dir = 'c:/users/asunder/Code/text-citation/'
output_dir = 'c:/users/asunder/Code/text-citation/book/text/'

#sentence = Sentence(content='asd')
content1 = 'Reading about nature is fine, but if a person walks in the woods and listens carefully, he can learn more than what is in books'
sentence1 = Sentence(content=content1)
sentence1.best_candidate = {
    'title': 'Reading about nature is fine, but if a person walks in the ...',
    'url': 'https://quotefancy.com/quote/817473/George-Washington-Carver-Reading-about-nature-is-fine-but-if-a-person-walks-in-the-woods',
    'sentence': 'Reading about nature is fine, but if a person walks in the woods and listens carefully, he can learn more than what is in books, for they speak with the',
    'prob': 0.9095}
sentence1.sentence_number = 10

content3 = ''
sentence3 = Sentence(content=content3)
sentence3.best_candidate = {
    'title': '',
    'url': '',
    'sentence': '',
    'prob': 0}
sentence3.sentence_number = 11

content2 = 'The leaves can be steeped to make a water that when applied to the skin itselfantimicrobial stimulates blood circulation and reduces congestion'
sentence2 = Sentence(content=content2)
sentence2.best_candidate = {
    'title': 'The medicinal plants of Myanmar - NCBI',
    'url': 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6033956/',
    'sentence': 'and leaves contain heating properties used to stimulate circulation and',
    'prob': 0.6768}
sentence2.sentence_number = 1001

sentences = [sentence1, sentence3, sentence2]

file_loader = FileSystemLoader(os.path.join(template_dir,'templates'))
env = Environment(loader=file_loader)

template = env.get_template('about.html')

output = template.render(sentences=sentences)
"""
output = template.render(title=sentence.best_candidate['title'],
                         url=sentence.best_candidate['url'],
                         text=sentence.best_candidate['sentence'],
                         prob=sentence.best_candidate['prob'],
                         content=sentence.content)
"""


path_to_output = os.path.join(output_dir, 'test_page.html')
with open(path_to_output, 'w') as f:
    f.write(output)

"""
from jinja2 import Environment, FileSystemLoader
import os

template_dir = 'c:/users/asunder/Code/text-citation/templates/'
output_dir = 'c:/users/asunder/Code/text-citation/book/text/'

content = 'This is about page'

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

path_to_template = os.path.join(template_dir, 'test_template.html')
template = env.get_template(path_to_template)

output = template.render(content=content)
path_to_output = os.path.join(template_dir, 'test_page.html')
with open(path_to_output, 'wb') as f:
    f.write()
"""