"""
🧪 Prompt SANS Chain of Thought (baseline)
On demande au LLM de répondre directement, sans raisonner.
"""

import sys
sys.path.append("..")
from shared import get_client

client = get_client()

PROBLEM = "Un fermier a 17 moutons. Tous sauf 9 meurent. Combien de moutons reste-t-il ?"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Tu es un assistant. Réponds directement avec le nombre, sans explication."},
        {"role": "user", "content": PROBLEM}
    ],
    temperature=0
)

print("=" * 50)
print("🔴 SANS Chain of Thought")
print("=" * 50)
print(f"Problème : {PROBLEM}")
print(f"Réponse  : {response.choices[0].message.content}")
