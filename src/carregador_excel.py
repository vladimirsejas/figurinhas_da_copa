import pandas as pd
from src.figurinha import Figurinha


def carregar_figurinhas(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)

    figurinhas = []

    for _, linha in df.iterrows():
        figurinha = Figurinha(
            int(linha["codigo"]),
            linha["jogador"],
            linha["pais"],
            linha["posicao"],
            linha["raridade"]
        )

        figurinhas.append(figurinha)

    return figurinhas