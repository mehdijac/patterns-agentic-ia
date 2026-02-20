# 🔌 Pattern 3 — Function Calling (Tool Use natif)

## C'est quoi ?

**Function Calling** est le mécanisme **natif** de l'API OpenAI pour que le LLM appelle des fonctions. Au lieu de bricoler du JSON dans le prompt (comme ReAct), on déclare nos outils comme des **schémas** et l'API retourne des appels structurés et garantis.

## Différence avec ReAct

| | ReAct (artisanal) | Function Calling (natif) |
|--|-------------------|--------------------------|
| Déclaration des outils | Texte dans le prompt | Schéma JSON passé à l'API |
| Format de sortie | JSON en texte (fragile) | Objet structuré (fiable) |
| Rôle pour les résultats | `role: "user"` (hack) | `role: "tool"` (dédié) |

## Fichiers

| Fichier | Rôle |
|---------|------|
| `tools.py` | Fonctions Python + schémas JSON pour l'API |
| `agent.py` | Boucle avec Function Calling natif |
| `main.py` | Point d'entrée |

## Lancer

```bash
cd 03_function_calling
python main.py
```

## Références

- [OpenAI Function Calling docs](https://platform.openai.com/docs/guides/function-calling)
