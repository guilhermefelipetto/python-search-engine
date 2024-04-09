import hashlib
import pickle
import os

def salvar_indices(documentos_indices, arquivo='documentos_indices.pickle'):
    with open(arquivo, 'wb') as f:
        pickle.dump(documentos_indices, f)

def carregar_indices(arquivo='documentos_indices.pickle'):
    if os.path.exists(arquivo):
        with open(arquivo, 'rb') as f:
            return pickle.load(f)
    else:
        return {}

def adicionar_documento_indices(documento_hash, arquivo='documentos_indices.pickle'):
    documentos_indices = carregar_indices(arquivo)
    if documento_hash not in documentos_indices:
        documentos_indices[documento_hash] = True
        salvar_indices(documentos_indices, arquivo)

def gerar_hash_documento(documento):
    documento_bytes = documento.encode('utf-8')
    hash_obj = hashlib.md5(documento_bytes)
    return hash_obj.hexdigest()

