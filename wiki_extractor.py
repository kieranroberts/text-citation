import wikipedia
import warnings
import re

from util import is_valid_sentence
from wiki_utils import exclude_substring_sections
        
def wiki_query(query, results=3):
    if len(query)<300:
        return wikipedia.search(query=query, results=results)
    else:
        return None


def page_extractor(page, first_N_lines=10):
#    if not(page.endswith('(disambiguation)')):
    try:
        response = wikipedia.page(page, auto_suggest=False)
        res = {'title' : response.title, 'url' : response.url, 
                    'content' : response.content}
        all_sentences = res['content'].split('.')
        valid_sentences = list(filter(is_valid_sentence, all_sentences))
        #valid_sentences
        res['sentences'] = valid_sentences[:first_N_lines]
        return res
    except wikipedia.exceptions.DisambiguationError as e:
        print('Skipping disambgiuous pages: {}'.format(e.options))
        return False

def wiki_search(query,results=3):
    entries = list()
    pages = wiki_query(query, results=results)
    if pages:
        for page in pages:
            res = page_extractor(page)
            if res:
                keys = list()
                values = list()
                for k,v in res.items():
                    keys.append(k)
                    values.append(v)
                entries.append(dict(zip(keys,values)))
    return entries

                
    
    