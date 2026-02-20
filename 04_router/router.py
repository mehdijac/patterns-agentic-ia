"""
🚦 Routeur — Classifie la demande et dispatche vers le bon agent
Le routeur ne fait JAMAIS le travail — il redirige uniquement.
"""

import sys
import json

sys.path.append("..")
from shared import get_client
from agents import AGENTS

client = get_client()

ROUTER_PROMPT = """Tu es un routeur. Ton SEUL JOB est de décider quel agent doit traiter la demande.

Agents disponibles :
{agents_description}

Réponds UNIQUEMENT avec un JSON :
{{
    "agent": "nom_de_lagent",
    "reason": "pourquoi cet agent en 1 phrase"
}}

Si aucun agent ne convient :
{{
    "agent": "none",
    "reason": "explication"
}}
"""


def build_agents_description() -> str:
    return "\n".join(f"- {name} : {info['description']}" for name, info in AGENTS.items())


def route_and_execute(question: str, verbose: bool = True) -> str:
    """1. Le routeur classifie → 2. L'agent spécialisé exécute."""

    if verbose:
        print(f"\n{'='*60}")
        print(f"❓ Demande : {question}")
        print(f"{'='*60}")

    # Étape 1 : Routage
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": ROUTER_PROMPT.format(agents_description=build_agents_description())},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    try:
        decision = json.loads(response.choices[0].message.content.strip())
    except json.JSONDecodeError:
        return f"Erreur du routeur."

    agent_name = decision.get("agent", "none")
    reason = decision.get("reason", "")

    if verbose:
        print(f"\n🚦 Routeur → agent: '{agent_name}'")
        print(f"   Raison : {reason}")

    # Étape 2 : Exécution
    if agent_name == "none" or agent_name not in AGENTS:
        return f"Aucun agent approprié. Raison : {reason}"

    if verbose:
        print(f"\n🤖 Exécution de l'agent '{agent_name}'...")

    result = AGENTS[agent_name]["function"](question)

    if verbose:
        print(f"\n✅ Résultat :\n{result}")

    return result
