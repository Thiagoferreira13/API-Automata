# API Automata

Uma API RESTful desenvolvida com FastAPI para simulação e teste de diferentes tipos de autômatos: AFD (Autômato Finito Determinístico), AP (Autômato com Pilha) e MT (Máquina de Turing).

## Características

* Criação e teste de AFDs, APs e MTs
* Representação visual dos autômatos usando GraphViz
* Teste de aceitação de strings
* Documentação interativa com Swagger e ReDoc
* Endpoints RESTful bem documentados
* Geração de diagramas em PNG

## Requisitos

* Python 3.7+
* GraphViz
* FastAPI
* Automata-lib
* Pydantic
* Uvicorn

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Thiagoferreira13/API-Automata.git
cd api-automata
```

2. Instale as dependências:
```bash
pip install fastapi
pip install uvicorn
pip install automata-lib
pip install pydantic
pip install graphviz
```

3. Instale o GraphViz no seu sistema:
   * Ubuntu/Debian: `sudo apt-get install graphviz`
   * MacOS: `brew install graphviz`
   * Windows: Baixe e instale do [site oficial](https://graphviz.org/download/)

## Executando a API

1. Inicie o servidor:
```bash
uvicorn main:app --reload
```

2. Acesse a documentação:
   * Swagger UI: http://localhost:8000/docs
   * ReDoc: http://localhost:8000/redoc

## Estrutura do Projeto

```
api-automata/
├── main.py
├── routers/
│   ├── afdRoute.py
│   ├── apRoute.py
│   └── mtRoute.py
├── services/
│   ├── afdService.py
│   ├── apService.py
│   └── mtService.py
├── schemas/
│   ├── afdSchema.py
│   ├── apSchema.py
│   └── mtSchema.py
└── tests/
    └── testes.txt
```

## Endpoints da API

### AFD (Autômato Finito Determinístico)
* `POST /api/afd/criar`: Cria novo AFD
* `POST /api/afd/testar`: Testa string no AFD atual
* `GET /api/afd/info`: Obtém informações do AFD
* `GET /api/afd/visualizar`: Gera visualização do AFD

### AP (Autômato com Pilha)
* `POST /api/ap/criar`: Cria novo AP
* `POST /api/ap/testar`: Testa string no AP atual
* `GET /api/ap/info`: Obtém informações do AP
* `GET /api/ap/visualizar`: Gera visualização do AP

### MT (Máquina de Turing)
* `POST /api/mt/criar`: Cria nova MT
* `POST /api/mt/testar`: Testa string na MT atual
* `GET /api/mt/info`: Obtém informações da MT
* `GET /api/mt/visualizar`: Gera visualização da MT

## Exemplos de Uso

### 1. Criando um AFD
* Exemplo: Cria um AFD que aceita números binários representando múltiplos de 3
```json
{
  "estados": ["q0", "q1", "q2"],
  "simbolos": ["0", "1"],
  "transicoes": {
    "q0": {"0": "q1", "1": "q0"},
    "q1": {"0": "q2", "1": "q0"},
    "q2": {"0": "q2", "1": "q2"}
  },
  "estado_inicial": "q0",
  "estados_finais": ["q2"]
}
```

### 2. Criando um AP
* Exemplo: Cria um AP que aceita a linguagem a^n b^n
```json
{
  "estados": ["q0", "q1", "q2"],
  "simbolos_entrada": ["a", "b"],
  "simbolos_pilha": ["Z", "A"],
  "transitions": {
    "q0": {
      "a": {
        "Z": ["q0", ["A", "Z"]],
        "A": ["q0", ["A", "A"]]
      },
      "b": {
        "A": ["q1", []]
      }
    },
    "q1": {
      "b": {
        "A": ["q1", []]
      },
      "": {
        "Z": ["q2", ["Z"]]
      }
    }
  },
  "estado_inicial": "q0",
  "estados_finais": ["q2"],
  "simbolo_inicial_pilha": "Z"
}
```

### 3. Criando uma MT
* Exemplo: Cria uma máquina de turing que aceita a linguagem  a^n b^n c^n

```json
{
  "estados": ["q0", "q1", "qf"],
  "simbolos_entrada": ["a", "b"],
  "simbolos_fita": ["a", "b", "_"],
  "transicoes": {
    "q0": {
      "a": ["q1", "b", "R"],
      "_": ["qf", "_", "R"]
    },
    "q1": {
      "a": ["q1", "a", "R"],
      "b": ["q0", "b", "L"]
    }
  },
  "estado_inicial": "q0",
  "estados_finais": ["qf"],
  "simbolo_branco": "_"
}
```

## Contribuindo

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.


