"""
🔧 Outils disponibles pour l'agent ReAct
Chaque outil est une simple fonction Python.
En vrai projet, recherche_web appellerait une API de recherche.
"""


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
    """Évalue une expression mathématique simple."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Erreur de calcul : {e}"


# Registre des outils — l'agent pioche ici par nom
TOOLS = {
    "recherche_web": {
        "function": recherche_web,
        "description": "Recherche des informations sur le web. Argument : une requête de recherche."
    },
    "calculatrice": {
        "function": calculatrice,
        "description": "Effectue un calcul mathématique. Argument : une expression (ex: '67.8 * 2')."
    }
}
