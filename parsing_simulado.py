# scripts/parsing_simulado.py
import json

# Simulação de um texto bruto extraído de um arquivo PDF por uma IA
curriculo_bruto = """
João Silva, Residente em Osasco - SP. 
Experiência de 2 anos em Análise de Dados e SQL.
Certificação em Python Avançado.
"""

def simular_parsing_ia(texto):
    print("🤖 IA processando e padronizando o texto do currículo...")
    
    # Lógica simples de busca textual (Simulando PLN)
    dados_extraidos = {
        "nome": "João Silva",
        "localizacao": "Osasco - SP" if "Osasco" in texto else "Outra",
        "habilidades": [],
    }
    
    if "SQL" in texto:
        dados_extraidos["habilidades"].append("SQL")
    if "Python" in texto:
        dados_extraidos["habilidades"].append("Python")
        
    return json.dumps(dados_extraidos, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    resultado = simular_parsing_ia(curriculo_bruto)
    print(resultado)
