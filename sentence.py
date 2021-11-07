from sentence_transformers import SentenceTransformer, util
from urllib.parse import urlparse
import json
class Sentence:
    # model = SentenceTransformer('all-mpnet-base-v2')
    
    def __init__(self, content, model):
        self.model = model
        self.content = content
        self.best_candidate = {'title' : None, 'url' : None, 'sentence' : None, 
                                'prob' : 0}
        self.source = None
        self.domain = None
        self.sentence_number = None
        self.sent_len = None
        self.is_section = False

    def __len__(self):
        return len(self.content.split(' '))
    
    def _get_source_(self, prob=0.8):
        if self.best_candidate['prob'] > prob:
            self.source = self.best_candidate
            self.domain = urlparse(self.best_candidate['url']).netloc
            
    def compare(self, source):
        query = self.content
        target_text = Sentence.model.encode(query)
        embeddings = Sentence.model.encode(source['sentences'], 
                                           convert_to_tensor=True)
        cosine_scores = util.pytorch_cos_sim(target_text, embeddings)
        for i in range(len(source['sentences'])):
            if cosine_scores[0][i] > self.best_candidate['prob']:
                self.best_candidate['title'] = source['title']
                self.best_candidate['url'] = source['url']
                self.best_candidate['sentence'] = source['sentences'][i]
                self.best_candidate['prob'] = cosine_scores[0][i]
                self._get_source_()
    
    def set_sentence_number(self, i):
        self.sentence_number = i
    
    def get_sentence_len(self):
        self.sent_len = len(self.content.split(' '))
        


# kdtree
# lsh

class Sentence:
    def __init__(self):
        self.content
        self.is_section
        self.embedding

    def save(self, output_file):
        #...

def get_closest_match(*, sentence: Sentence, source: dict):
    # ...

def get_sentence_embedding(*, content: str) -> Sentence:
    #...
    return Sentence(...)

# from sentence import get_closest_match
# get_closest_match(sentence)

#json.dump(f) / dumps()
#json.load  loads

sentence = Sentence()
sentence.save()