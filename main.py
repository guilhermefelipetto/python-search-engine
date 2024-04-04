import os
import sys

from calculo_ranking import calcula_tfidf
from preprocessamento import processa_dados, processa_input

if __name__ == "__main__":
    diretorio_atual = os.path.abspath(os.path.dirname(sys.argv[0]))

    dados = [
    "aprender python é uma linguagem de programação",  # deve ter 2
    "A família é a base da sociedade.",  # deve ter 0
    "Existem muitos recursos online para Python.",  ## deve ter 1 
    ]

    user_input = "aprender".split()

    resultado_ranking = calcula_tfidf(dados, user_input)
