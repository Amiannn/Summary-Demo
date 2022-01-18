import numpy as np

from lib.utils.preprocessor import preprocessor

# punctuation
PUNCTUATION = [
    # ，、；：？！．～「」『』（）《 》〈 〉──……﹏﹏＿
    'PERIODCATEGORY', 
    'PAUSECATEGORY', 
    'SEMICOLONCATEGORY', 
    'COLONCATEGORY',
    'COMMACATEGORY',
    'PARENTHESISCATEGORY', 
    'QUESTIONCATEGORY', 
    'EXCLAMATIONCATEGORY', 
    'DASHCATEGORY', 
    'ETCCATEGORY', 
    'DOTCATEGORY'
    'FW', 
]

class Summer():
    def __init__(self):
        ...
    
    def preprocessing(self, document):
        # sentence and word segmentation
        result = preprocessor.segmentation(document)
        self.sens, self.sens_pos, self.sens_id = result
        
        # remove punctuation
        result = preprocessor.filterOut(self.sens, self.sens_pos, self.sens_id, PUNCTUATION)
        self.clean_sens, self.clean_sens_pos, self.clean_sens_id = result

    def cosine_similarity(self, a, b):
        sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 0.000001) 
        return sim

    def tfidf_scoring(self):
        # sentences tf-idf
        sens_tfidf = preprocessor.tfidf(self.clean_sens)

        # document(sentences center) tf-idf
        doc_tfidf  = np.sum(sens_tfidf, axis=0) / len(sens_tfidf)

        # count cosine similarity
        result = []
        for sen_tfidf, sen_id in zip(sens_tfidf, self.clean_sens_id):
            score = self.cosine_similarity(doc_tfidf, sen_tfidf)
            result.append([score, sen_id])
        result = sorted(result, reverse=True, key=lambda res: res[0])
        return result

    def run(self, document, topk=5):
        # preprocessing
        self.preprocessing(document)

        # scoring
        scoring_result = self.tfidf_scoring()
        scoring_result = sorted(scoring_result[:topk], key=lambda res: res[1])
        result = [
            {
                'score'   : scoring_result[i][0], 
                'sentence': ''.join(self.sens[scoring_result[i][1]]) + '。'
            } for i in range(len(scoring_result))
        ]
        return result