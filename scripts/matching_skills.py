# scripts/matching_skills.py

# Requisitos definidos no Job Profiling da EGK
requisitos_vaga = {"Python", "SQL", "Osasco", "Git"}

# Perfil extraído do candidato
perfil_candidato = {"Python", "SQL", "Osasco"}

def calcular_match_score(vaga, candidato):
    print("🧠 Calculando score de aderência do candidato...")
    
    # Encontra as habilidades em comum
    skills_em_comum = vaga.intersection(candidato)
    
    # Cálculo simples de porcentagem
    score = (len(skills_em_comum) / len(vaga)) * 100
    return score

if __name__ == "__main__":
    score_final = calcular_match_score(requisitos_vaga, perfil_candidato)
    print(f"📊 O candidato tem {score_final:.2f}% de compatibilidade com a vaga da EGK.")