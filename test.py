from write import ExtractBook
import os
import nltk
nltk.download('punkt')
import util
from sentence import Sentence
from google_extractor import google_search
from wiki_extractor import wiki_search 

home_dir = 'c:/Users/asunder/Code/text-citation/book'
num_pages = 70
page_ordering = dict()

for i in range(1,num_pages+1):
    page_ordering[i] = '{}.png'.format(i)
    
path_to_output = os.path.join(home_dir,'text', 'book_of_craig.txt')

book = ExtractBook(page_ordering=page_ordering, 
                   home_dir=home_dir, 
                   num_pages=num_pages)

book.convert_book_to_text()
my_text = book.full_book

sentences = util.str_to_sentences(my_text)
valid_sentences = list()
for s in sentences:
    if util.is_valid_sentence(s):
        valid_sentences.append(s)

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
from wiki_extractor import wiki_output





#tokens = nltk.sent_tokenize(my_text)