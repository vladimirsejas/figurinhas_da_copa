from src.nodo_fila import NodoFila


class Fila:

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def enqueue(self, figurinha):
        novo = NodoFila(figurinha)
        if self._fim is None:
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._tamanho += 1

    def dequeue(self):
        if self.esta_vazia():
            print("Fila vazia!")
            return None
        figurinha = self._inicio.figurinha
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return figurinha

    def peek(self):
        if self.esta_vazia():
            return None
        return self._inicio.figurinha

    def limpar(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def esta_vazia(self):
        return self._tamanho == 0

    def tamanho(self):
        return self._tamanho

    def exibir(self):
        if self.esta_vazia():
            print("Fila vazia.")
            return
        atual = self._inicio
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo
