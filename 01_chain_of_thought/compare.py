"""
🧪 Comparaison : Sans CoT vs Zero-shot CoT vs Few-shot CoT
Envoie le MÊME problème avec les 3 approches et affiche les résultats.
"""

import sys
sys.path.append("..")
from shared import get_client

client = get_client()

PROBLEM = "Un fermier a 17 moutons. Tous sauf 9 meurent. Combien de moutons reste-t-il ?"


def ask(messages: list) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


# 1. Sans CoT
no_cot = ask([
    {"role": "system", "content": "Réponds directement avec le nombre, sans explication."},
    {"role": "user", "content": PROBLEM}
])

# 2. Zero-shot CoT
zero_shot = ask([
    {"role": "system", "content": "Raisonne étape par étape. Termine par 'Réponse finale : [nombre]'"},
    {"role": "user", "content": PROBLEM}
])

# 3. Few-shot CoT
few_shot = ask([
    {"role": "system", "content": "Raisonne étape par étape comme dans les exemples."},
    {"role": "user", "content": "J'ai 3 pommes. J'en achète 5. J'en donne 2. Combien ?"},
    {"role": "assistant", "content": "Étape 1 : 3 pommes.\nÉtape 2 : 3+5=8.\nÉtape 3 : 8-2=6.\nRéponse finale : 6"},
    {"role": "user", "content": PROBLEM}
])

# Affichage
print(f"\n{'='*60}")
print(f"📝 PROBLÈME : {PROBLEM}")
print(f"   (Bonne réponse : 9)")
print(f"{'='*60}")

print(f"\n🔴 SANS CoT :\n   {no_cot}")

print(f"\n🟡 ZERO-SHOT CoT :")
for line in zero_shot.split("\n"):
    print(f"   {line}")

print(f"\n🟢 FEW-SHOT CoT :")
for line in few_shot.split("\n"):
    print(f"   {line}")

print(f"\n{'='*60}")
