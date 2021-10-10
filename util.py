import re

def str_to_sentences(x):
    return x.split('.')
    
def is_valid_sentence(sentence):
    sentence = re.sub('^[ ]+', '', sentence)
    pattern = re.compile(r'^[A-Za-z0-9]')
    if re.match(pattern, sentence):
        return True
    else:
        return False