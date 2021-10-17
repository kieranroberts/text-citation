import re

def str_to_sentences(x):
    sentences = x.split('.')
    sentences = list(map(lambda s : re.sub('^[\s]+', '', s).rstrip(), sentences))
    return sentences
    
def is_valid_sentence(sentence):
    sentence = re.sub('^[ ]+', '', sentence)
    pattern = re.compile(r'^[\'\"A-Za-z]')
    if re.match(pattern, sentence) and len(sentence.lstrip().rstrip().split(' '))>2:
        return True
    else:
        return False