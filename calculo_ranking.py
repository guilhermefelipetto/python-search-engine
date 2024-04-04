import os
import pickle
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessamento import processa_dados, processa_input

def calcula_tfidf(dados, user_input):
    """Calcula os rankings com TF-IDF usando scikit-learn"""
    # Processamento dos dados e das palavras-chave
    dados_processados = processa_dados(dados)
    keywords = processa_input(user_input)
    dados_processados_string = [' '.join(lista) for lista in dados_processados]

    # Verifica se há novos termos para calcular o TF-IDF
    termos_ja_calculados = set(index_reverso_carregado.keys())
    termos_novos = set(keywords) - termos_ja_calculados

    scores = np.zeros(len(dados_processados_string))

    if os.path.exists(".\\r_index\\index_reverso.pickle"):
        with open(".\\r_index\\index_reverso.pickle", "rb") as f:
            index_reverso_carregado = pickle.load(f)
    
    else:
        print("Arquivo de indice reverso nao encontrado. Criando outro.")
        index_reverso_carregado = {}
    
    if termos_novos:
        # Calcula TF-IDF para os novos termos
        tfidf_vectorizer = TfidfVectorizer(vocabulary=keywords)
        tfidf_matrix = tfidf_vectorizer.fit_transform(dados_processados_string)

        termos = tfidf_vectorizer.get_feature_names_out()

        # Atualiza o índice reverso com os novos termos
        novo_index = {}
        for i, termo in enumerate(termos):
            for j, score in enumerate(tfidf_matrix[:, i].toarray().flatten()):
                if score > 0:
                    if termo not in novo_index:
                        novo_index[termo] = []
                    novo_index[termo].append((j, score))

        for termo, ocorrencias in novo_index.items():
            if termo not in index_reverso_carregado:
                index_reverso_carregado[termo] = []
            index_reverso_carregado[termo].extend(ocorrencias)

        salvar_index_reverso(index_reverso_carregado)
    else:
        print("Termos já indexados, usando resultados anteriores.")

    # Imprime o índice reverso
    for termo, ocorrencias in index_reverso_carregado.items():
        print(f"Termo: {termo}")
        for doc, score in ocorrencias:
            print(f"Documento: {doc}: Score: TF-IDF {score}")

    # Calcula e imprime os rankings
    sorted_indices = np.argsort(scores)[::-1]
    for rank, idx in enumerate(sorted_indices):
        print(f"Rank {rank+1}: Documento: {idx+1} - Score: {scores[idx]}")
    
    def salvar_index_reverso(index_reverso):
        with open(".\\r_index\\index_reverso.pickle", "wb") as f:
            pickle.dump(index_reverso, f)

    return index_reverso_carregado
