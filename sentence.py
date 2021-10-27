from sentence_transformers import SentenceTransformer, util

class Sentence:
    model = SentenceTransformer('all-mpnet-base-v2')
    
    def __init__(self, content):
        self.content = content
        self.best_candidate = {'title' : None, 'url' : None, 'sentence' : None, 
                                'prob' : 0}
        self.source = None
        self.sentence_number = None

    
    def _get_source_(self, prob=0.8):
        if self.best_candidate['prob'] > prob:
            self.source = self.best_candidate
            
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
        

        
        
        
        
        
    