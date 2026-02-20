"""
🧪 Few-shot Chain of Thought
On montre au LLM DES EXEMPLES de raisonnement étape par étape.
Le LLM comprend le format attendu et l'imite.
"""

import sys
sys.path.append("..")
from shared import get_client

client = get_client()

PROBLEM = "Un fermier a 17 moutons. Tous sauf 9 meurent. Combien de moutons reste-t-il ?"

# On "truque" l'historique avec des faux échanges user/assistant
# pour montrer le format de raisonnement attendu.
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Tu es un assistant. Raisonne étape par étape comme dans les exemples."},

        # Exemple 1
        {"role": "user", "content": "J'ai 3 pommes. J'en achète 5 de plus. J'en donne 2. Combien m'en reste-t-il ?"},
        {"role": "assistant", "content": (
            "Étape 1 : Je commence avec 3 pommes.\n"
            "Étape 2 : J'en achète 5 → 3 + 5 = 8 pommes.\n"
            "Étape 3 : J'en donne 2 → 8 - 2 = 6 pommes.\n"
            "Réponse finale : 6"
        )},

        # Exemple 2
        {"role": "user", "content": "Un train part avec 10 passagers. À l'arrêt, 3 descendent et 5 montent. Combien de passagers ?"},
        {"role": "assistant", "content": (
            "Étape 1 : Le train part avec 10 passagers.\n"
            "Étape 2 : 3 descendent → 10 - 3 = 7 passagers.\n"
            "Étape 3 : 5 montent → 7 + 5 = 12 passagers.\n"
            "Réponse finale : 12"
        )},

        # La vraie question
        {"role": "user", "content": PROBLEM}
    ],
    temperature=0
)

print("=" * 50)
print("🟢 FEW-SHOT Chain of Thought")
print("=" * 50)
print(f"Problème : {PROBLEM}")
print(f"\nRaisonnement du LLM :\n{response.choices[0].message.content}")
