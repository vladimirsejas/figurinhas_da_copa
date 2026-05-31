from src.nodo_fila import NodoFila


class Historico:

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._total = 0

    def registrar(self, descricao: str):
        novo = NodoFila(descricao)
        if self._fim is None:
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._total += 1
        print(f"[Histórico] {descricao}")

    def exibir(self):
        if self._inicio is None:
            print("Nenhuma troca registrada ainda.")
            return
        print("\n===== HISTÓRICO DE TROCAS =====")
        atual = self._inicio
        i = 1
        while atual is not None:
            print(f"{i}. {atual.figurinha}")
            atual = atual.proximo
            i += 1
        print("================================\n")

    def total(self):
        return self._total
