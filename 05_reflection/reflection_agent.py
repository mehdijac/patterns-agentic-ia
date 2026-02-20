"""
🪞 Agent Reflection — Génère → Critique → Améliore
Même modèle, 3 prompts différents pour 3 rôles distincts.
"""

import sys
sys.path.append("..")
from shared import get_client

client = get_client()


def call_llm(system_prompt: str, user_message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content


def generate(task: str) -> str:
    """Produit un premier jet."""
    return call_llm(
        "Tu es un rédacteur professionnel. Produis un premier brouillon. Fais de ton mieux.",
        task
    )


def critique(task: str, draft: str) -> str:
    """Analyse un brouillon et liste ses faiblesses."""
    return call_llm(
        "Tu es un relecteur exigeant. Liste 3-5 points faibles ou améliorations. Sois précis et constructif.",
        f"DEMANDE ORIGINALE :\n{task}\n\nBROUILLON À ÉVALUER :\n{draft}"
    )


def improve(task: str, draft: str, criticism: str) -> str:
    """Réécrit en corrigeant les faiblesses identifiées."""
    return call_llm(
        "Tu es un rédacteur senior. Réécris en corrigeant TOUS les points soulevés.",
        f"DEMANDE :\n{task}\n\nBROUILLON :\n{draft}\n\nCRITIQUES :\n{criticism}"
    )


def run_reflection(task: str, iterations: int = 2, verbose: bool = True) -> str:
    """Lance la boucle Generate → Critique → Improve."""

    if verbose:
        print(f"\n{'='*60}")
        print(f"📝 Tâche : {task}")
        print(f"🔄 Itérations : {iterations}")
        print(f"{'='*60}")

    # Premier brouillon
    draft = generate(task)
    if verbose:
        print(f"\n--- Brouillon initial ---\n{draft}")

    # Boucle Critique → Amélioration
    for i in range(1, iterations + 1):
        if verbose:
            print(f"\n--- Itération {i}/{iterations} : Critique ---")

        criticism = critique(task, draft)
        if verbose:
            print(criticism)
            print(f"\n--- Itération {i}/{iterations} : Amélioration ---")

        draft = improve(task, draft, criticism)
        if verbose:
            print(draft)

    if verbose:
        print(f"\n{'='*60}")
        print("✅ Version finale ci-dessus")
        print(f"{'='*60}")

    return draft
