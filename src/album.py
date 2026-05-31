from src.nodo_lista import NodoLista

TOTAL_FIGURINHAS = 640

class Album:

```
def __init__(self):
    self._cabeca = None
    self._tamanho = 0

def adicionar(self, figurinha):
    if self.buscar(figurinha.id) is not None:
        print(f"Figurinha #{figurinha.id} já está colada no álbum.")
        return False

    novo = NodoLista(figurinha)
    novo.proximo = self._cabeca
    self._cabeca = novo
    self._tamanho += 1
    print(f"Figurinha #{figurinha.id} - {figurinha.nome} colada com sucesso!")
    return True

def remover(self, id_figurinha: int):
    atual = self._cabeca
    anterior = None

    while atual is not None:
        if atual.figurinha.id == id_figurinha:
            if anterior is None:
                self._cabeca = atual.proximo
            else:
                anterior.proximo = atual.proximo

            self._tamanho -= 1
            print(f"Figurinha #{id_figurinha} removida do álbum.")
            return True

        anterior = atual
        atual = atual.proximo

    print(f"Figurinha #{id_figurinha} não encontrada no álbum.")
    return False

def buscar(self, id_figurinha: int):
    atual = self._cabeca

    while atual is not None:
        if atual.figurinha.id == id_figurinha:
            return atual.figurinha

        atual = atual.proximo

    return None

def buscar_por_jogador(self, nome: str):
    cabeca_resultado = None
    atual = self._cabeca

    while atual is not None:
        if nome.lower() in atual.figurinha.nome.lower():
            novo = NodoLista(atual.figurinha)
            novo.proximo = cabeca_resultado
            cabeca_resultado = novo

        atual = atual.proximo

    return cabeca_resultado

def buscar_por_selecao(self, pais: str):
    cabeca_resultado = None
    atual = self._cabeca

    while atual is not None:
        if pais.lower() in atual.figurinha.pais.lower():
            novo = NodoLista(atual.figurinha)
            novo.proximo = cabeca_resultado
            cabeca_resultado = novo

        atual = atual.proximo

    return cabeca_resultado

def exibir(self):
    if self._cabeca is None:
        print("O álbum está vazio.")
        return

    print("\n===== ÁLBUM DA COPA 2026 =====")

    atual = self._cabeca

    while atual is not None:
        print(atual.figurinha)
        atual = atual.proximo

    print("================================\n")

def porcentagem(self):
    pct = (self._tamanho / TOTAL_FIGURINHAS) * 100
    print(f"Álbum {self._tamanho}/{TOTAL_FIGURINHAS} ({pct:.1f}% completo)")
    return pct

def tamanho(self):
    return self._tamanho
```
