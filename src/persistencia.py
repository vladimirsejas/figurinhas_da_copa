import json
import os

ARQUIVO_DADOS = "dados/dados_album.json"


def salvar(album, repetidas: dict):
    dados = {
        "album": [],
        "repetidas": []
    }

    atual = album._cabeca
    while atual is not None:
        f = atual.figurinha
        dados["album"].append({
            "id": f.id,
            "nome": f.nome,
            "pais": f.pais,
            "posicao": f.posicao,
            "raridade": f.raridade
        })
        atual = atual.proximo

    for id_fig, fila in repetidas.items():
        no = fila._inicio
        while no is not None:
            f = no.figurinha
            dados["repetidas"].append({
                "id": f.id,
                "nome": f.nome,
                "pais": f.pais,
                "posicao": f.posicao,
                "raridade": f.raridade
            })
            no = no.proximo

    os.makedirs("dados", exist_ok=True)
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arq:
        json.dump(dados, arq, ensure_ascii=False, indent=2)

    print(f"Dados salvos em '{ARQUIVO_DADOS}'.")


def carregar():
    if not os.path.exists(ARQUIVO_DADOS):
        print("Nenhum arquivo de dados encontrado. Comecando do zero.")
        return [], []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arq:
        dados = json.load(arq)

    print(f"Dados carregados de '{ARQUIVO_DADOS}'.")
    return dados.get("album", []), dados.get("repetidas", [])