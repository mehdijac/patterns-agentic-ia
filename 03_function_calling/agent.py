"""
🧠 Agent Function Calling — Utilise le mécanisme natif de l'API
L'API retourne directement un objet "tool_calls" structuré.
Plus de JSON artisanal à parser.
"""

import sys
import json

sys.path.append("..")
from shared import get_client
from tools import TOOL_SCHEMAS, TOOL_FUNCTIONS

client = get_client()


def run_function_calling_agent(question: str, max_steps: int = 5, verbose: bool = True) -> str:
    """Lance un agent avec Function Calling natif d'OpenAI."""

    # Le system prompt est BEAUCOUP plus simple que dans ReAct
    # car l'API gère la mécanique des outils.
    messages = [
        {"role": "system", "content": "Tu es un assistant utile. Utilise les outils quand nécessaire."},
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
            tools=TOOL_SCHEMAS,       # ← On déclare les outils disponibles
            tool_choice="auto",        # ← Le LLM décide s'il utilise un outil
            temperature=0
        )

        msg = response.choices[0].message

        # Pas d'outil → réponse directe
        if not msg.tool_calls:
            if verbose:
                print(f"💬 Réponse directe : {msg.content}")
            return msg.content

        # Appel d'outil(s)
        messages.append(msg)

        for tool_call in msg.tool_calls:
            func_name = tool_call.function.name
            func_args = json.loads(tool_call.function.arguments)

            if verbose:
                print(f"🔧 Appel outil : {func_name}({func_args})")

            if func_name in TOOL_FUNCTIONS:
                first_arg = list(func_args.values())[0]
                result = TOOL_FUNCTIONS[func_name](first_arg)
            else:
                result = f"Outil inconnu : {func_name}"

            if verbose:
                print(f"👁️  Résultat : {result}")

            # role="tool" → rôle dédié de l'API (pas un hack avec "user")
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

    return "Erreur : nombre maximum d'étapes atteint."
