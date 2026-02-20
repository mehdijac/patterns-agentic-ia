"""
🚀 Démo Function Calling
"""

from agent import run_function_calling_agent

questions = [
    "Quelle est la population de la France multipliée par 2 ?",
    "Quelle est la capitale du Japon ?",
    "Combien font 2 + 2 ?",
]

if __name__ == "__main__":
    for q in questions:
        answer = run_function_calling_agent(q, verbose=True)
        print(f"\n🏁 RÉSULTAT FINAL : {answer}")
        print("\n" + "=" * 60 + "\n")
