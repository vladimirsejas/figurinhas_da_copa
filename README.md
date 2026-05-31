# Album de Figurinhas - Copa 2026
Disciplina: Estrutura de Dados | FATEC Rio Claro

## Como executar
Para executar o projeto, utilize o comando abaixo no terminal a partir da pasta raiz do projeto.
```
pip install -r requirements.txt
python main.py
```

## Estrutura do projeto
```
figurinhas_da_copa/
├── main.py              <- ponto de entrada, menus
├── requirements.txt     <- dependencias do projeto
├── src/
│   ├── __init__.py      <- torna src um pacote Python
│   ├── figurinha.py     <- entidade Figurinha
│   ├── nodo_lista.py    <- no da lista encadeada (album)
│   ├── nodo_fila.py     <- no da fila encadeada (repetidas, trocas, historico)
│   ├── album.py         <- lista encadeada de figurinhas
│   ├── fila.py          <- fila FIFO propria (enqueue/dequeue)
│   ├── historico.py     <- registro de trocas
│   └── persistencia.py  <- salvar/carregar JSON
└── dados/
    └── dados_album.json <- gerado automaticamente ao salvar
```

## Sobre os nos encadeados
O projeto utiliza dois tipos de no por razoes estruturais distintas. O NodoLista e utilizado exclusivamente para armazenar figurinhas dentro do album, compondo a lista encadeada principal da colecao, onde cada no guarda uma figurinha ja colada e aponta para a proxima. O NodoFila e utilizado em operacoes externas ao album, como controle de figurinhas repetidas, trocas e historico, seguindo a logica FIFO (First In, First Out). Em resumo, o NodoLista representa a colecao de figurinhas do album, enquanto o NodoFila representa atividades relacionadas ao album que nao fazem parte diretamente da colecao.

## Requisitos
Python 3.10 ou superior e a biblioteca rich, que pode ser instalada com o comando pip install -r requirements.txt.
