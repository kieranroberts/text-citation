from re import split
import nltk
nltk.download('punkt')

def tokenize_and_remove_special_chars(text):
    tokens = nltk.sent_tokenize(text)
    new_tokens = list()
    N = len(tokens)
    for i in range(N):
        t = tokens[i]
        for t0 in t.split('\n\n'):
            print(t0)
            new_tokens.append(t0.replace('\n', ' '))
    
    return new_tokens