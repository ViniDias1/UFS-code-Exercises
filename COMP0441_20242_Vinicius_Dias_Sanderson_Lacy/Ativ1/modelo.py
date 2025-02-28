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
