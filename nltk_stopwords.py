# armazena as stopwords para não tem que ficar fazendo download a cada execucao

import os
import pickle
import nltk
from nltk.corpus import stopwords


def get_stopwords():
    stopwords_file_path = 'stopwords_portuguese.pickle'
    
    if os.path.exists(stopwords_file_path):
        with open(stopwords_file_path, 'rb') as f:
            termos_irrelevantes = pickle.load(f)
    else:
        nltk.download('stopwords')
        termos_irrelevantes = set(stopwords.words('portuguese'))
        with open(stopwords_file_path, 'wb') as file:
            pickle.dump(termos_irrelevantes, file)
    
    return termos_irrelevantes
