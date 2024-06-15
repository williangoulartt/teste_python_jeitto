# Desafio Jeitto

Este repositório contém as implementações referentes ao desafio técnico do processo seletivo da Jeitto.

## 1. Função Fibonacci

A implementação da função Fibonacci está localizada no diretório `src/fibonacci`.

### Descrição da Função

A função `fibonacci(n)`:
- Verifica se o valor de `n` é válido (positivo).
- Retorna os valores baseados nos primeiros termos conhecidos da sequência (0 e 1).
- Utiliza uma abordagem iterativa para calcular os termos subsequentes.

### Cenários de Teste

Os testes para a função `fibonacci(n)` estão no arquivo `tests/test_fibonacci.py` e utilizam a biblioteca `unittest`. Os cenários de teste incluem:

- `test_first_term`: Verifica se o primeiro termo é 0.
- `test_second_term`: Verifica se o segundo termo é 1.
- `test_third_term`: Verifica se o terceiro termo é 1.
- `test_tenth_term`: Verifica se o décimo termo é 34.
- `test_negative_term`: Verifica se a função lança uma exceção `ValueError` para um termo negativo.
- `test_zero_term`: Verifica se a função lança uma exceção `ValueError` para zero.
- `test_large_term`: Verifica um termo maior (50º termo), onde o resultado conhecido é 7778742049.

## Como Executar

### Requisitos

- Python 3.x

### Instruções

#### Clone o Repositório

```sh
git clone https://github.com/williangoulartt/teste_python_jeitto.git
cd teste_python_jeitto/src/fibonacci
```

#### Crie e Ative um Ambiente Virtual

```sh
python -m venv venv

# No Linux
source venv/bin/activate  

# No Windows
venv\Scripts\activate
```
#### Para executar a função

```sh
python -m fibonacci.py
```

#### Para executar  os testes

```sh
cd ../../
python -m unittest discover

```

## 2. API FastAPI

A implementação da API FastAPI está localizada no diretório src/fastapi_crud. Esta é uma aplicação CRUD básica usando FastAPI para gerenciar informações de clientes.

### Requisitos

- Python 3.x

### Instruções

#### Clone o Repositório

```sh
git clone https://github.com/williangoulartt/teste_python_jeitto.git
cd teste_python_jeitto/src/fastapi_crud
```

#### Crie e Ative um Ambiente Virtual (Caso tenha criado para executar a função fibonacci não é necessário criar um novo ambiente virtual)

```sh
python -m venv venv

# No Linux
source venv/bin/activate  

# No Windows
venv\Scripts\activate
```
#### Instale as Dependências da Aplicação

```sh
pip install -r requirements.txt
```
caso alguma dependência não seja instalada com o comando anterior, instale-a diretamente:
```sh
pip install nome_da_dependencia (nome no arquivo requirements.txt)

```


#### Execute a Aplicação

```sh
cd fastapi_crud
uvicorn app.main:app --reload
```

#### Acesse a Documentação da API

Abra o navegador e vá para http://127.0.0.1:8000/docs

#### Testes

```sh
pytest
```

#### Estrutura do Projeto

```sh
app/models.py: Define os modelos do SQLAlchemy.
app/schemas.py: Define os esquemas Pydantic.
app/database.py: Configura a conexão com o banco de dados.
app/crud.py: Define as operações CRUD.
app/main.py: Define as rotas FastAPI.
app/tests/: Contém os testes unitários.
```

## 3. API FastAPI
