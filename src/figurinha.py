class Figurinha:

    def __init__(self, id: int, nome: str, pais: str, posicao: str, raridade: str):
        self.id = id
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

    def __str__(self):
        return (
            f"[{self.id}] {self.nome} | {self.pais} | "
            f"{self.posicao} | Raridade: {self.raridade}"
        )
