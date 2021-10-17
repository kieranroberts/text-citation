# Based on 
# https://practicaldatascience.co.uk/data-science/how-to-scrape-google-search-results-using-python

import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession

from util import str_to_sentences, is_valid_sentence

def get_source(url):
    """Return the source code for the provided URL. 
    Args: 
        url (string): URL of the page to scrape.
    Returns:
        response (object): HTTP response object from requests_html. 
    """
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.',                      
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

def get_results(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    return response

def parse_results(response):
    
    # These identifiers may change in the future to prevent unofficial scraping
    # of Google search results
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".IsZvec"
    
    hyphen = chr(8212)
    
    results = response.html.find(css_identifier_result)

    output = []
    
    for result in results:

        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
            'text': result.find(css_identifier_text, first=True).text
        }

        # We want to split the text into a list of valid sentences.
        all_sentences = list(
            map(lambda x : x.split(hyphen)[-1], item['text'].split('.'))
        )
        valid_sentences = list()
        for sentence in all_sentences:
            if is_valid_sentence(sentence):
                valid_sentences.append(sentence.lstrip().rstrip())
        item['sentences'] = valid_sentences
        output.append(item)
        
    return output

def google_search(query):
    response = get_results(query)
    return parse_results(response)