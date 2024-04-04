import pickle

with open(".\\r_index\\index_reverso.pickle", "rb") as f:
    dados = pickle.load(f)

print(dados)