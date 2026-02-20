"""
Utilitaire partagé : charge le .env depuis la racine du repo,
quel que soit le dossier depuis lequel on exécute le script.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


def get_client() -> OpenAI:
    """Charge le .env à la racine du repo et retourne un client OpenAI."""

    # Cherche le .env en remontant depuis le dossier courant
    current = Path(__file__).resolve().parent
    for parent in [current, current.parent, current.parent.parent]:
        env_path = parent / ".env"
        if env_path.exists():
            load_dotenv(env_path)
            break

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY non trouvée. "
            "Copiez .env.example → .env à la racine du repo et ajoutez votre clé."
        )

    return OpenAI(api_key=api_key)
