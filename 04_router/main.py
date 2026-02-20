"""
🚀 Démo Router Pattern
"""

from router import route_and_execute

demandes = [
    "Traduis en anglais : Le chat dort sur le canapé.",
    "Résume ce texte : L'intelligence artificielle est un domaine de l'informatique qui vise à créer des machines capables de simuler l'intelligence humaine. Elle englobe le machine learning, le deep learning et le traitement du langage naturel.",
    "Écris une fonction Python qui inverse une liste.",
    "Quelle est la météo aujourd'hui ?",
]

if __name__ == "__main__":
    for d in demandes:
        route_and_execute(d, verbose=True)
        print("\n" + "=" * 60 + "\n")
