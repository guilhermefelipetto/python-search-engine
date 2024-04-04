import numpy as np
import nltk

from nltk.corpus import stopwords

# download das stopwords
nltk.download('stopwords')

termos_irrelevantes = set(stopwords.words('portuguese'))
char_especias = [x for x in "\\./*-+º|!@#$%¨&()?~^[]{}"]


def processa_dados(dados):
    termos_sem_irr = []
    for dado in dados:
        termos = dado.split()
        termos_limpos = []
        for termo in termos:
            termo_limpo = ''.join(char for char in termo if char.isalnum())
            termos_limpos.append(termo_limpo.lower())
        termos_sem_irr.append([termo for termo in termos_limpos if termo not in termos_irrelevantes])
    return termos_sem_irr


def processa_input(user_input):
    def remove_termos_irr():
        termos_sem_irr = []
        for termo in user_input:
            termo_limpo = termo.lower()
            for char_especial in char_especias:
                termo_limpo = termo_limpo.replace(char_especial, "")
            if termo_limpo not in termos_irrelevantes:
                termos_sem_irr.append(termo_limpo)
        return termos_sem_irr
    return remove_termos_irr()
