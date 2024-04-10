import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessamento import processa_dados, processa_input

def salvar_index_reverso(index_reverso):
    if not os.path.exists(".\\r_index"):
        os.makedirs(".\\r_index")
    with open(".\\r_index\\index_reverso.pickle", "wb") as f:
        pickle.dump(index_reverso, f)

def calcula_tfidf(dados, user_input):
    index_reverso_carregado = {}
    dados_processados = processa_dados(dados)
    keywords = processa_input(user_input)
    dados_processados_string = [' '.join(lista) for lista in dados_processados]

    if os.path.exists(".\\r_index\\index_reverso.pickle"):
        with open(".\\r_index\\index_reverso.pickle", "rb") as f:
            index_reverso_carregado = pickle.load(f)
    else:
        print("Arquivo de índice reverso não encontrado. Criando outro.")

    scores = np.zeros(len(dados_processados_string))

    # Reutiliza os scores para termos existentes no índice reverso
    for termo in keywords:
        if termo in index_reverso_carregado:
            for doc_id, score in index_reverso_carregado[termo]:
                scores[doc_id] += score
            print(f"Termo: {termo} já indexado, usando resultados anteriores.")
        else:
            print(f"Termo: {termo} não encontrado no índice reverso. Processando...")

            # Calcula o TF-IDF para o novo termo
            tfidf_vectorizer = TfidfVectorizer()
            tfidf_matrix = tfidf_vectorizer.fit_transform(dados_processados_string)
            term_index = tfidf_vectorizer.vocabulary_.get(termo)

            # Atualiza os scores e o índice reverso para o novo termo
            if term_index is not None:
                for i, doc in enumerate(dados_processados_string):
                    score = tfidf_matrix[i, term_index]
                    if score > 0:
                        if termo not in index_reverso_carregado:
                            index_reverso_carregado[termo] = []
                        index_reverso_carregado[termo].append((i, score))
                        scores[i] += score

            salvar_index_reverso(index_reverso_carregado)

    # Imprime os scores e o ranking dos documentos
    sorted_indices = np.argsort(scores)[::-1]
    for rank, idx in enumerate(sorted_indices):
        print(f"Rank {rank+1}: Documento: {idx} - Score: {scores[idx]}")

    return index_reverso_carregado
