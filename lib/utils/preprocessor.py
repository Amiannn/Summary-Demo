from ckipnlp.pipeline import CkipPipeline, CkipDocument
from sklearn.feature_extraction.text import TfidfVectorizer

# tf-idf
MAX_DF       = 0.95  # Ignore words with high df. (Similar effect to stopword filtering)
MIN_DF       = 5     # Ignore words with low df.
SMOOTH_IDF   = True  # Smooth idf weights by adding 1 to df.
SUBLINEAR_TF = True  # Replace tf with 1 + log(tf).

class preprocessor():
    pipeline   = CkipPipeline()
    vectorizer = TfidfVectorizer(
        # max_df=MAX_DF, 
        # min_df=MIN_DF, 
        smooth_idf=SMOOTH_IDF, 
        sublinear_tf=SUBLINEAR_TF
    )
    @staticmethod
    def segmentation(document):
        # sentence segmentation
        document = document.replace('。', '\n')
        doc = CkipDocument(raw=document)
        # word segmentation
        preprocessor.pipeline.get_ws(doc)
        preprocessor.pipeline.get_pos(doc)    
        sentences     = doc.ws
        sentences_pos = doc.pos
        sentences_id  = list(range(len(sentences)))
        return sentences, sentences_pos, sentences_id

    @staticmethod
    def filterOut(sentences, sentences_pos, sentences_id, query):
        res_sens, res_sens_pos, res_sens_id = [], [], []
        for index in range(len(sentences)):
            if len(sentences[index]) == 0:
                continue
            res_sen, res_sen_pos = [], []
            for sen, sen_pos in zip(sentences[index], sentences_pos[index]):
                if sen_pos in query:
                    continue
                res_sen.append(sen)
                res_sen_pos.append(sen_pos)
            res_sens.append(res_sen)
            res_sens_pos.append(res_sen_pos)
            res_sens_id.append(sentences_id[index])
        return res_sens, res_sens_pos, res_sens_id

    @staticmethod
    def tfidf(sentences):
        sens = [' '.join(sentences[i]) for i in range(len(sentences))]
        sens_tfidf = preprocessor.vectorizer.fit_transform(sens).toarray()
        return sens_tfidf