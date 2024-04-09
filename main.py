import os
import sys

from calculo_ranking import calcula_tfidf
from preprocessamento import processa_dados, processa_input

if __name__ == "__main__":
    diretorio_atual = os.path.abspath(os.path.dirname(sys.argv[0]))

    dados = [
    "aprender python é uma linguagem de programação",  # 0
    "A família é a base da sociedade.",  # 1
    "Existem muitos recursos online para Python.",  # 2 
    ]

    user_input = "aprender python".split()

    resultado_ranking = calcula_tfidf(dados, user_input)
