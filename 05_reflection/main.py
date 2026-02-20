"""
🚀 Démo Reflection
"""

from reflection_agent import run_reflection

task_1 = (
    "Écris un email professionnel pour demander une augmentation de salaire. "
    "Je travaille dans l'entreprise depuis 3 ans, j'ai mené 2 projets majeurs "
    "et mes évaluations sont excellentes."
)

task_2 = (
    "Écris une description de poste pour un développeur Python senior "
    "dans une startup d'intelligence artificielle."
)

if __name__ == "__main__":
    print("\n🔷 EXEMPLE 1 : Email d'augmentation")
    run_reflection(task_1, iterations=2, verbose=True)

    print("\n\n🔷 EXEMPLE 2 : Description de poste")
    run_reflection(task_2, iterations=1, verbose=True)
