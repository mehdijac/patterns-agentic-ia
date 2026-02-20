"""
🔧 Outils + Schémas pour Function Calling natif
Deux parties pour chaque outil :
  1. La FONCTION Python (ce qui s'exécute)
  2. Le SCHÉMA JSON (ce qu'on déclare à l'API pour qu'elle sache comment l'appeler)
"""


# === Fonctions Python ===

def recherche_web(query: str) -> str:
    """Simule une recherche web."""
    fake_db = {
        "population france": "La population de la France est d'environ 67,8 millions d'habitants (2024).",
        "population paris": "Paris compte environ 2,1 millions d'habitants intra-muros.",
        "capitale japon": "La capitale du Japon est Tokyo.",
        "pib france": "Le PIB de la France est d'environ 3 050 milliards de dollars (2024).",
    }
    query_lower = query.lower()
    for key, value in fake_db.items():
        if key in query_lower or query_lower in key:
            return value
    return f"Aucun résultat trouvé pour : '{query}'"


def calculatrice(expression: str) -> str:
    """Évalue une expression mathématique."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Erreur de calcul : {e}"


# === Schémas JSON pour l'API OpenAI ===

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "recherche_web",
            "description": "Recherche des informations sur le web.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "La requête de recherche"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculatrice",
            "description": "Effectue un calcul mathématique.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "L'expression à calculer (ex: '67.8 * 2')"}
                },
                "required": ["expression"]
            }
        }
    }
]

TOOL_FUNCTIONS = {
    "recherche_web": recherche_web,
    "calculatrice": calculatrice,
}
