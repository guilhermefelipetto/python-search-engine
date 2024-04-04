# banco de dados
dados1 = [
    "python é uma linguagem de programação",
    "aprender python é bom",
    "vestibulares na unicamp",
    "programar em java é bom",
    "banco de dados sql",
    "Python é uma linguagem de programação poderosa.",
    "Aprender Python é essencial para qualquer desenvolvedor.",
    "Python é amplamente utilizado em ciência de dados.",
    "O mercado de trabalho valoriza profissionais com conhecimento em Python.",
    "Existem muitos recursos online para aprender Python.",
    "Python oferece uma sintaxe simples e legível.",
    "Muitas empresas adotam Python para desenvolvimento de software.",
    "Python possui uma vasta comunidade de desenvolvedores.",
    "Python é uma escolha popular para automação de tarefas.",
    "A demanda por programadores Python está em constante crescimento.",
    "O sol brilha no céu azul.",
    "As flores desabrocham na primavera.",
    "A água é essencial para a vida.",
    "O vento sopra suavemente nas árvores.",
    "A lua brilha no céu durante a noite.",
    "Os pássaros cantam pela manhã.",
    "A felicidade está nas pequenas coisas da vida.",
    "O mar é calmo ao entardecer.",
    "A amizade é um tesouro precioso.",
    "A família é a base da sociedade.",
]

import numpy as np

dados = [
    "python é uma linguagem de programação",
    "A família é a base da sociedade.",
    "Existem muitos recursos online para aprender Python.",
]

user_input = "em COMO? aprender! python?".split()

termos_irrelevantes = [
    'e',
    'em',
    'ou',
    'mas',
    'porque',
    'como',
    'quando',
    'se',
    'embora',
    'apesar',
    'ainda',
    'enquanto',
    'logo',
    'pois',
    'portanto',
    'assim',
    'porém',
    'também',
    'então',
    'logo',
    'outra',
    ]

char_especias = [x for x in "?!."]


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


def matriz(dados, user_input):
    palavras_unicas = set(processa_input(user_input))

    matriz = np.zeros((len(dados), len(palavras_unicas)), dtype=float)

    for i, sentenca in enumerate(dados):
        for palavra in sentenca:
            if palavra in palavras_unicas:
                j = list(palavras_unicas).index(palavra)
                matriz[i, j] += 1
    
    return matriz, list(palavras_unicas)


dados_processados = processa_dados(dados)
input_usuario = processa_input(user_input)

matriz, palavras_unicas = matriz(dados_processados, input_usuario)


def soma_linhas(matriz):
    linhas_somadas = []
    for linha in matriz:
        soma = sum(linha)
        linhas_somadas.append(soma)
    
    return sorted(linhas_somadas, reverse=True)


print(matriz, palavras_unicas)
print(soma_linhas(matriz))
