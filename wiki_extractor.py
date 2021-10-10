import wikipedia
import warnings
import re

from util import is_valid_sentence
from wiki_utils import exclude_substring_sections
        
def wiki_search(query, results=10):
    return wikipedia.search(query=query, results=results)


def page_extractor(page):
    if not(page.endswith('(disambiguation)')):
        try:
            response = wikipedia.page(page, auto_suggest=False)
            res = {'title' : response.title, 'url' : response.url, 
                        'content' : response.content}
            all_sentences = res['content'].split('.')
            valid_sentences = list(filter(is_valid_sentence, all_sentences))
            res['sentences'] = valid_sentences
            return res
        except wikipedia.exceptions.DisambiguationError as e:
            print('Skipping disambgiuous pages: {}'.format(e.options))
            return False
    

                
    
    