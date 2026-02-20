"""
🧪 Zero-shot Chain of Thought
On ajoute UNE instruction : "Raisonne étape par étape."
Aucun exemple fourni — d'où le nom "zero-shot".
"""

import sys
sys.path.append("..")
from shared import get_client

client = get_client()

PROBLEM = "Un fermier a 17 moutons. Tous sauf 9 meurent. Combien de moutons reste-t-il ?"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": (
                "Tu es un assistant. "
                "Raisonne étape par étape avant de donner ta réponse finale. "
                "Termine toujours par : 'Réponse finale : [nombre]'"
            )
        },
        {"role": "user", "content": PROBLEM}
    ],
    temperature=0
)

print("=" * 50)
print("🟡 ZERO-SHOT Chain of Thought")
print("=" * 50)
print(f"Problème : {PROBLEM}")
print(f"\nRaisonnement du LLM :\n{response.choices[0].message.content}")
