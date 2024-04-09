
import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessamento import processa_dados, processa_input
from indices_manager import carregar_indices, adicionar_documento_indices, gerar_hash_documento

def salvar_index_reverso(index_reverso):
    with open(".\\r_index\\index_reverso.pickle", "wb") as f:
        pickle.dump(index_reverso, f)

def calcula_tfidf(dados, user_input):
    index_reverso_carregado = {}
    documentos_indices = carregar_indices()

    dados_processados = processa_dados(dados)
    keywords = processa_input(user_input)
    dados_processados_string = [' '.join(lista) for lista in dados_processados]

    if os.path.exists(".\\r_index\\index_reverso.pickle"):
        with open(".\\r_index\\index_reverso.pickle", "rb") as f:
            index_reverso_carregado = pickle.load(f)
    else:
        print("Arquivo de índice reverso não encontrado. Criando outro.")

    termos_ja_calculados = set(index_reverso_carregado.keys())
    termos_novos = set(keywords) - termos_ja_calculados

    scores = np.zeros(len(dados_processados_string))

    documento_para_idx = {gerar_hash_documento(doc): idx for idx, doc in enumerate(dados_processados_string)}
    
    for i, documento in enumerate(dados_processados_string):
        for termo in keywords:
            if termo in index_reverso_carregado:
                for doc_hash, score in index_reverso_carregado[termo]:
                    idx = documento_para_idx.get(doc_hash)
                    if idx is not None and documento.find(termo) != -1:
                        scores[i] += score
                        break

    if termos_novos:
        documentos_novos = [documento for idx, documento in enumerate(dados_processados_string) if gerar_hash_documento(documento) not in documentos_indices]
        
        if documentos_novos:
            tfidf_vectorizer = TfidfVectorizer(vocabulary=termos_novos)
            tfidf_matrix_novos = tfidf_vectorizer.fit_transform(documentos_novos)
            termos = tfidf_vectorizer.get_feature_names_out()

            for i, documento in enumerate(documentos_novos):
                documento_hash = gerar_hash_documento(documento)
                if documento_hash not in documentos_indices:
                    for termo in termos:
                        if termo in termos_novos:
                            termo_idx = list(termos).index(termo)
                            score = tfidf_matrix_novos[i, termo_idx]
                            if score > 0:
                                if termo not in index_reverso_carregado:
                                    index_reverso_carregado[termo] = []
                                index_reverso_carregado[termo].append((documento_hash, score))
                    adicionar_documento_indices(documento_hash)

        salvar_index_reverso(index_reverso_carregado)
    else:
        print("Termos já indexados, usando resultados anteriores.")

    for termo, ocorrencias in index_reverso_carregado.items():
        print(f"Termo: {termo}")
        for doc, score in ocorrencias:
            print(f"Documento: {doc}: Score: TF-IDF {score}")

    sorted_indices = np.argsort(scores)[::-1]
    for rank, idx in enumerate(sorted_indices):
        print(f"Rank {rank+1}: Documento: {idx} - Score: {scores[idx]}")

    return index_reverso_carregado
