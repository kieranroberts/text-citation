import re

def str_to_sentences(x):
    sentences = x.split('\n\n')
    sentences = [re.split('\.(?![0-9A-Za-z])', x) for x in sentences]
    sentences = [item for sent in sentences for item in sent if item != ' ']
    sentences = [re.sub('\n', '', sent) for sent in sentences]
    sentences = list(map(lambda s : re.sub('^[\s]+', '', s), sentences))
    return sentences
    
def is_valid_sentence(sentence):
    sentence = re.sub('^[ ]+', '', sentence)
    pattern = re.compile(r'^[\'\"A-Za-z]')
    if re.match(pattern, sentence) and len(sentence.lstrip().rstrip().split(' '))>3:
        return True
    else:
        return False