## Evolução do Projeto

O Sistema de Álbum de Figurinhas da Copa do Mundo 2026 não surgiu pronto em sua forma atual. Sua construção ocorreu de maneira gradual, à medida que novas necessidades.
Inicialmente, o projeto foi idealizado numa proposta simples de gerenciamento de figurinhas. O foco estava na criação das classes principais e na aplicação dos fundamentos da Programação Orientada a Objetos. As figurinhas eram manipuladas diretamente pelo sistema, permitindo operações básicas de cadastro, consulta e organização dos dados. Digitadas uma a uma.
Ao aplicar conceitos de Estrutura de Dados, o álbum passou a utilizar uma lista encadeada como mecanismo principal de armazenamento. Cada figurinha passou a ser representada dentro da estrutura por meio de um nó específico, implementado pela classe NodoLista. Essa mudança permitiu trabalhar diretamente com encadeamento de elementos, percorrimento de estruturas dinâmicas e gerenciamento manual de referências.
Houve a separação das as figurinhas repetidas da coleção principal. Para resolver esse problema foi implementada uma estrutura de fila independente. A fila passou a ser responsável pelo armazenamento das figurinhas repetidas, simulando o comportamento encontrado em coleções reais. Para essa funcionalidade foi criada a classe NodoFila. Enquanto o NodoLista é utilizado exclusivamente na organização interna do álbum, o NodoFila é utilizado para controlar o fluxo das figurinhas repetidas e das operações relacionadas às trocas. Esse foi mum ponto importante a ser observado as funções de nós e cada um dentro da sua estrutura.
Conforme o projeto crescia, tornou-se necessário registrar as ações realizadas pelo usuário. Foi então criado um sistema de histórico capaz de armazenar operações importantes realizadas durante a utilização do programa, permitindo um controle mais completo sobre os eventos ocorridos na coleção.

Senti a necessidade de automatizar os dados das figurinhas e solucionei pensando incialmente em um planilha excell. Pensei em um Faker mas descartei pois queria dados reais do album e fiz pesquisas para conseguir a informações necessárias.
Sendo essa uma das maiores transformações do projeto que  aconteceu então quando o modelo baseado em cadastro manual foi substituído por uma base de dados externa. Foi criada uma planilha Excel contendo 865 figurinhas da Copa do Mundo de 2026, cada uma representando um jogador único da competição. Além do código identificador, cada registro passou a armazenar informações como seleção, nome do jogador, posição em campo e nível de raridade.

A integração dessa base de dados foi possível graças à utilização da biblioteca Pandas. Por meio dela, os dados da planilha puderam ser carregados e transformados em objetos utilizados pelo sistema. O uso do Pandas permitiu trabalhar com uma quantidade muito maior de informações sem a necessidade de cadastramento manual.

Para garantir a leitura correta do arquivo XLSX foi utilizada a biblioteca OpenPyXL. Essa biblioteca atua como suporte para o acesso à planilha Excel, permitindo que os dados sejam carregados automaticamente durante a inicialização da aplicação.

Com a base de dados integrada, o projeto deixou de funcionar como um simples cadastro de figurinhas e passou a simular efetivamente um álbum de figurinhas. Foi implementado um sistema de abertura de pacotes no qual cinco figurinhas são sorteadas aleatoriamente a partir da base de dados carregada. As figurinhas inéditas são inseridas no álbum principal, enquanto as repetidas são encaminhadas automaticamente para a fila de repetidas.

A experiência foi ampliada com a introdução das raridades. Cada figurinha passou a possuir uma classificação específica e probabilidades diferentes de aparecimento durante os sorteios, aproximando ainda mais o comportamento do sistema ao de um álbum real.

Outro recurso importante incorporado ao projeto foi a persistência de dados utilizando arquivos JSON. Essa funcionalidade permite salvar o estado atual da coleção e recuperar todas as informações em futuras execuções do programa. Dessa forma, o usuário pode continuar sua coleção exatamente do ponto em que ela foi interrompida.

À medida que novas funcionalidades eram adicionadas, surgiu também a necessidade de melhorar a apresentação visual das informações. Para isso foi incorporada a biblioteca Rich. Sua utilização permitiu criar tabelas formatadas, painéis informativos e uma interface muito mais organizada dentro do terminal. Graças ao Rich, a visualização do álbum, das figurinhas repetidas, do progresso da coleção e dos resultados das consultas tornou-se mais clara e profissional.

O resultado final é um sistema que reúne Programação Orientada a Objetos, listas encadeadas, filas, manipulação de arquivos Excel, persistência em JSON, modularização e interface avançada em terminal. Mais do que um simples cadastro de figurinhas, o projeto evoluiu para uma simulação completa de um álbum da Copa do Mundo de 2026 baseado em uma coleção real composta por 865 jogadores.

## Estrutura do Projeto

```text
figurinhas_da_copa/
│
├── DOCS/
│   ├── Captura de tela 2026-05-31 082257.png
│   ├── Captura de tela 2026-05-31 082440.png
│   ├── Captura de tela 2026-05-31 082536.png
│   ├── Captura de tela 2026-05-31 082615.png
│   ├── Captura de tela 2026-05-31 082745.png
│   └── Captura de tela 2026-05-31 082829.png
│
├── dados/
│   └── dados_album.json
│
├── src/
│   ├── album.py
│   ├── carregador_excel.py
│   ├── figurinha.py
│   ├── fila.py
│   ├── historico.py
│   ├── nodo_fila.py
│   ├── nodo_lista.py
│   └── persistencia.py
│
├── figurinhas.xlsx
├── main.py
├── README.md
└── requirements.txt
```

!## Registro Visual do Sistema

### Menu Principal

![Menu Principal](DOCS/Captura%20de%20tela%202026-05-31%20082257.png)

### Abertura de Pacotes e Gerenciamento do Álbum

![Abertura de Pacotes](DOCS/Captura%20de%20tela%202026-05-31%20082440.png)

### Visualização do Álbum Completo - Parte 1

![Álbum Completo](DOCS/Captura%20de%20tela%202026-05-31%20082536.png)

### Visualização do Álbum Completo - Parte 2

![Álbum Completo](DOCS/Captura%20de%20tela%202026-05-31%20082615.png)

### Consulta de Progresso da Coleção

![Progresso da Coleção](DOCS/Captura%20de%20tela%202026-05-31%20082745.png)

### Busca por Seleção

![Busca por Seleção](DOCS/Captura%20de%20tela%202026-05-31%20082829.png)