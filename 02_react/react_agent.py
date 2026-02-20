"""
🧠 Agent ReAct — La boucle Thought → Action → Observation
1. On envoie la question + la liste des outils au LLM
2. Le LLM répond avec un Thought et une Action (ou une réponse finale)
3. Si Action → on exécute l'outil → on renvoie l'Observation au LLM
4. On boucle jusqu'à la réponse finale
"""

import sys
import json

sys.path.append("..")
from shared import get_client
from tools import TOOLS

client = get_client()

SYSTEM_PROMPT = """Tu es un assistant qui raisonne étape par étape et utilise des outils quand nécessaire.

## Outils disponibles :
{tools_description}

## Format OBLIGATOIRE :

Si tu as besoin d'un outil :
{{
    "thought": "ton raisonnement ici",
    "action": "nom_de_loutil",
    "action_input": "argument pour l'outil"
}}

Si tu as la réponse finale :
{{
    "thought": "ton raisonnement final",
    "final_answer": "ta réponse complète ici"
}}

IMPORTANT : Réponds UNIQUEMENT avec du JSON valide. UN SEUL bloc par réponse.
"""


def build_tools_description() -> str:
    lines = []
    for name, info in TOOLS.items():
        lines.append(f"- **{name}** : {info['description']}")
    return "\n".join(lines)


def run_react_agent(question: str, max_steps: int = 5, verbose: bool = True) -> str:
    """Lance la boucle ReAct pour répondre à une question."""

    system_msg = SYSTEM_PROMPT.format(tools_description=build_tools_description())
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": question}
    ]

    if verbose:
        print(f"\n{'='*60}")
        print(f"❓ Question : {question}")
        print(f"{'='*60}")

    for step in range(1, max_steps + 1):
        if verbose:
            print(f"\n--- Étape {step} ---")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0
        )
        llm_output = response.choices[0].message.content.strip()

        try:
            parsed = json.loads(llm_output)
        except json.JSONDecodeError:
            if verbose:
                print(f"⚠️  Réponse non-JSON : {llm_output[:100]}...")
            messages.append({"role": "assistant", "content": llm_output})
            messages.append({"role": "user", "content": "Erreur : JSON invalide. Recommence."})
            continue

        thought = parsed.get("thought", "")
        if verbose:
            print(f"💭 Thought : {thought}")

        # Réponse finale → on sort
        if "final_answer" in parsed:
            final = parsed["final_answer"]
            if verbose:
                print(f"✅ Réponse finale : {final}")
            return final

        # Appel d'outil
        action = parsed.get("action", "")
        action_input = parsed.get("action_input", "")
        if verbose:
            print(f"🔧 Action : {action}({action_input!r})")

        if action in TOOLS:
            observation = TOOLS[action]["function"](action_input)
        else:
            observation = f"Erreur : outil '{action}' inconnu."

        if verbose:
            print(f"👁️  Observation : {observation}")

        messages.append({"role": "assistant", "content": llm_output})
        messages.append({"role": "user", "content": f"Observation : {observation}"})

    return "Erreur : nombre maximum d'étapes atteint."
