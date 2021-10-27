import os
import util
from sentence import Sentence
from google_extractor import google_search
from wiki_extractor import wiki_search 
import pickle

home_dir = 'c:/Users/asunder/Code/text-citation/book'

"""
num_pages = 70
page_ordering = dict()

for i in range(1,num_pages+1):
    page_ordering[i] = '{}.png'.format(i)
    
path_to_output = os.path.join(home_dir,'text', 'book_of_craig.txt')

book = ExtractBook(page_ordering=page_ordering, 
                   home_dir=home_dir, 
                   num_pages=num_pages,
                   title = "CRAIG\'S CABIN FORAGING FIELD GUIDE: A SELF TAUGHT GUIDE TO FORAGING")

book.convert_book_to_text()
book.clean_book_text()
book.write_full_book_to_file(path_to_output)
my_text = book.full_book
"""
with open(os.path.join(home_dir,'text', 'book_of_craig.txt')) as f:
    text = f.readlines()

text = ''.join(text)

sentences = util.str_to_sentences(text)

valid_sentences = list()
for s in sentences:
    if util.is_valid_sentence(s):
        valid_sentences.append(s)

def compare_sentences(sentences):
    sentence_objects = list()
    i = 0
    for sentence in sentences:
        s = Sentence(content=sentence)
        if util.is_valid_sentence(sentence):
            query = s.content
            
            sources = google_search(query)
            wiki_sources = wiki_search(query)
            sources.extend(wiki_sources)

            for source in sources:
                s.compare(source)
        
        s.set_sentence_number(i)
        sentence_objects.append(s)
        print(i)
        i += 1
    return sentence_objects

sentence_objects = compare_sentences(sentences)

pickle.dump(sentence_objects, open(os.path.join(home_dir,'book4.p'), 'wb'))

with open(os.path.join(home_dir,'book4.p'), 'rb') as fileobj:
    sentence_objects  = pickle.load(fileobj)



"""
sentence_objects = list()
for sentence in valid_sentences[765:]:
    s = Sentence(content=sentence)
    query = s.content
    
    sources = google_search(query)
    wiki_sources = wiki_search(query)
    sources.extend(wiki_sources)

    for source in sources:
        s.compare(source)
    
    sentence_objects.append(s)
    
    
 
 
import pickle
#favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump(sentence_objects, open(os.path.join(home_dir,'book.p'), 'wb'))
with open(os.path.join(home_dir,'book.p'), 'rb') as fileobj:
    sentence_objects  = pickle.load(fileobj)

probs = list()
for s in sentence_objects:
    probs.append(s.best_candidate['prob'])

very_close = list()
for s in sentence_objects:
    if s.best_candidate['prob'] > 0.75 and s.best_candidate['prob'] <= 0.80:
        very_close.append(s)
    
import importlib
import google_extractor #import the module here, so that it can be reloaded.
importlib.reload(google_extractor)
from google_extractor import google_search # or whatever name you want.

import wiki_extractor
importlib.reload(wiki_extractor)
from wiki_extractor import wiki_search





#tokens = nltk.sent_tokenize(my_text)
"""