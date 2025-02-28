# Atividade 1 - Evolução de Software

Objetivo dessa atividade é classificar issues de um projeto open-source bem sucedido em 1) Refatoração 2) Teste de Regressão. Além disso, avaliar o impacto dessas issues na evolução do software.


# Métodos

Utilizando a API do Github, foi feito um dump de mais de 300 issues de forma aleatória. A partir disso, foi utilizado o modelo NLI "Hugging Face Zero-shot-classification facebook/bart-large-mnli" para analisar a issues e classifica-las. Após isso, a issues são salvas em um banco de dados local (PostegreSQL)

## Detalhes para implementação

1. Foi utilizado o TOKEN do GitHub para fazer as requisições á API visando evitar qualquer limitação de tempo, quantidade ou tamannho das requisições.

2. GITHUB_TOKEN e DB_PASSWORD foram registradas como variáveis de ambiente, por motivos de segurança. Bastar usar os dois comandos abaixo no terminal e continuar com a execução.




```sh
$env:GITHUB_TOKEN="SEU_TOKEN"
$env:DB_PASSWORD="SENHA_DO_DB"

```
## Etapas

1. Inicialmente foi preciso fazer o dump das issues do repositório https://github.com/pytorch/pytorch. Para isso, foi utilizado a API do GitHub. Os parametros para as requisições á API estão no método "fetch_issues()"

```python
def fetch_issues(page, per_page):
    params = {"page": page, "per_page": per_page, "state": "closed"}
    response = requests.get(GITHUB_API_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()
```

2. Com as issues em mãos, o próximo passo é analizar as issues e classifica-las. Dito isso, as issues do dump são passado para o modelo Zero-Shot-Classification.

```python
from transformers import pipeline

classificador = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def issue_classification(titulo, descricao):
 
    categorias = ["Refatoração", "Teste de Regressão"]
    
    texto = f"{titulo} {descricao}"
    
    resultado = classificador(texto, candidate_labels=categorias)

    categoria_mais_provavel = resultado["labels"][0]
    pontuacao = resultado["scores"][0]

    limite = 0.6  

    if pontuacao >= limite:
        return categoria_mais_provavel
    else:
        return None

```

3. Após a classificação, temos um conjunto de issues classificadas entre Refatoração e Teste de Regressão. Dessa forma, foram salvas todas elas em um banco de dados relacional (PostegreSQL).

