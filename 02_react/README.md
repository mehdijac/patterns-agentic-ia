# 🧠🔧 Pattern 2 — ReAct (Reasoning + Acting)

## C'est quoi ?

**ReAct** est un pattern où le LLM alterne entre **réflexion** et **utilisation d'outils** pour répondre à une question. Contrairement au Chain of Thought (qui ne fait que réfléchir), ReAct permet au modèle d'**agir** dans le monde extérieur.

## Le cycle

```
Thought     → "Je dois chercher la population de la France"   (🤖 LLM)
Action      → recherche_web("population France")               (🤖 LLM choisit)
Observation → "67,8 millions d'habitants"                      (💻 Code exécute)
Thought     → "Maintenant je multiplie par 2"                  (🤖 LLM)
Action      → calculatrice("67800000 * 2")                     (🤖 LLM choisit)
Observation → "135600000"                                      (💻 Code exécute)
Final       → "135,6 millions"                                 (🤖 LLM)
```

## Fichiers

| Fichier | Rôle |
|---------|------|
| `tools.py` | Les outils disponibles (recherche simulée, calculatrice) |
| `react_agent.py` | La boucle Thought → Action → Observation |
| `main.py` | Lance l'agent sur des questions test |

## Lancer

```bash
cd 02_react
python main.py
```

## Différence avec Function Calling

ReAct gère l'appel d'outils de manière **artisanale** (JSON dans le prompt, parsing manuel). Function Calling (pattern 3) utilise le mécanisme **natif** de l'API. En production, on combine souvent les deux : le cycle ReAct pour la logique + Function Calling pour la fiabilité.

## Références

- [ReAct: Synergizing Reasoning and Acting (Yao et al., 2022)](https://arxiv.org/abs/2210.03629)
