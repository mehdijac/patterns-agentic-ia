"""
🤖 Agents spécialisés
Chaque agent a UN SEUL JOB et un prompt optimisé pour cette tâche.
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
        temperature=0
    )
    return response.choices[0].message.content


def agent_traduction(text: str) -> str:
    return call_llm(
        "Tu es un traducteur professionnel français → anglais. "
        "Traduis le texte donné. Ne donne QUE la traduction.",
        text
    )


def agent_resume(text: str) -> str:
    return call_llm(
        "Tu es un expert en synthèse. "
        "Résume le texte en 2-3 phrases maximum.",
        text
    )


def agent_code(text: str) -> str:
    return call_llm(
        "Tu es un développeur Python senior. "
        "Écris du code propre et commenté. Inclus un exemple d'utilisation.",
        text
    )


AGENTS = {
    "traduction": {"function": agent_traduction, "description": "Traduit du texte en anglais"},
    "resume":     {"function": agent_resume,     "description": "Résume un texte"},
    "code":       {"function": agent_code,       "description": "Écrit du code Python"},
}
