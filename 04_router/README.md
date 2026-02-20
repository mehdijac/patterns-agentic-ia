# 🚦 Pattern 4 — Router

## C'est quoi ?

Le **Router Pattern** utilise un LLM comme "standard téléphonique" : il analyse la demande et la redirige vers l'agent spécialisé le plus adapté. Chaque agent a un prompt court et ciblé → meilleure qualité qu'un gros prompt généraliste.

## Architecture

```
Utilisateur : "Traduis ce texte"
        ↓
    🚦 ROUTEUR (LLM #1) → classifie
        ↓
    🤖 Agent Traduction (LLM #2) → exécute
        ↓
    Résultat
```

## Agents disponibles

| Agent | Job |
|-------|-----|
| 🇬🇧 traduction | Traduit du français vers l'anglais |
| 📝 resume | Résume un texte en 2-3 phrases |
| 💻 code | Écrit du code Python |

## Fichiers

| Fichier | Rôle |
|---------|------|
| `agents.py` | Les 3 agents spécialisés |
| `router.py` | Le routeur (classifie + dispatche) |
| `main.py` | Point d'entrée |

## Lancer

```bash
cd 04_router
python main.py
```

## Références

- [Building Effective Agents (Anthropic)](https://www.anthropic.com/research/building-effective-agents)
