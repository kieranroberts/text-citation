# text-citation
## The files
### write.py
This takes images and uses OCR from Google's tesseract to convert them into strings of text
### wiki_utils.py
This some helper functions to parse wikipedia pages
### util.py
Some helper functions to convert strings of text into "sentences"
### tokenize.py
Have not used this anywhere
### sentence.py
This is a class that stores sentences and possible "sources" of the sentence
### google_extractor.py
A very crude google web scraper to give text from google search results
### extract.py
A class that performs immage to string.
### test.py
Just an example of how it all works.

## How it all works
This follows the sequence in test.py
<ol>
<li>Use ExtractBook on a number of images that make up the pages of the text. 
This part can be skipped if you already have text.</li>
<li>Turn the string containing the body of text int a list of valid sentences. 
The valid sentences are defined as in util.py. It's very crude.</li>
<li>Create a Sentence object for each sentence and search for possible sources through two methods
<ol>
<li>google_search(): this takes top 10 results. Extracts all the "sentences" from the preview text
    of the search.</li>
<li> wiki_search(): this takes just the top result from a wiki search. It then extracts all the sentences.
The reason I restricted this to just the top result is because there are a lot of sentences in a wikipedia
page.</li>
</ol>
</li>
<li>Once it has collected all potential sources, it compares them using cosine similarity
(see specifics of compare() in sentences.py. It also keeps track of the most likely source.</li>
</ol> 

Every below line 44 was just to save the output as a pickle object.