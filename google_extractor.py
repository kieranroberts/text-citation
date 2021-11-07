# Based on
# https://practicaldatascience.co.uk/data-science/how-to-scrape-google-search-results-using-python

skip_domains = (
    "https://www.amazon.",
    "https://amazon.",
    "https://www.google.",
    "https://google.",
    "https://webcache.googleusercontent.",
    "http://webcache.googleusercontent.",
    "https://policies.google.",
    "https://support.google.",
    "https://books.google.",
    "https://maps.google.",
)



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


def get_results(query):

    query = urllib.parse.quote_plus(query)
    response = get_source(f"https://www.google.co.uk/search?q={query}")

    return response


def parse_results(response, results=5):
    # These identifiers may change in the future to prevent unofficial scraping
    # of Google search results
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".IsZvec"

    results = response.html.find(css_identifier_result)

    output = list()

    for result in results[:results]:
        item = {
            "title": result.find(css_identifier_title, first=True).text,
            "url": result.find(css_identifier_link, first=True).attrs["href"]
        }
        try:
            item["content"] = result.find(css_identifier_text, first=True).text
        except:
            item["content"] = ""

        if not (item["url"].startswith(skip_domains)):
            item_ext = extract_sentence_valid(item)
            if item_ext:
                output.append(item_ext)

    return output

def extract_sentence_valid(item):
    hyphen = chr(8212)
    all_sentences = list(
        map(lambda x: x.split(hyphen)[-1], item["content"].split("."))
    )
    valid_sentences = list()
    for sentence in all_sentences:
        if is_valid_sentence(sentence):
            valid_sentences.append(sentence.lstrip().rstrip())
    if len(valid_sentences) > 0:
        item["sentences"] = valid_sentences
        return item
    else:
        return False

def google_search(query):
    response = get_results(query)
    return parse_results(response)
