# 🧠 LLM Architecture Patterns — Démos Python

Une collection de démos Python illustrant les principaux patterns d'architecture pour applications LLM. Chaque pattern est une démo indépendante, prête à exécuter.

## 📊 Vue d'ensemble des patterns

| # | Pattern | Définition | Avantages | Inconvénients | Appels LLM |
|---|---------|-----------|-----------|---------------|------------|
| 1 | **Chain of Thought (CoT)** | Forcer le LLM à raisonner étape par étape avant de répondre, en montrant son travail intermédiaire. | Améliore fortement la logique et les maths. Très simple à implémenter (une ligne de prompt suffit). | Réponses plus longues = plus lent et plus coûteux. Ne garantit pas que le raisonnement soit correct. | 1 |
| 2 | **ReAct** | Le LLM alterne entre réflexion (Thought) et utilisation d'outils (Action), puis observe le résultat avant de continuer. | Le LLM peut accéder à des données externes (web, BDD, API). Raisonnement traçable étape par étape. | Parsing JSON artisanal = fragile. Risque de boucle infinie si mal configuré. | 1 à N |
| 3 | **Function Calling** | Mécanisme natif de l'API (OpenAI/Anthropic) pour que le LLM appelle des fonctions de manière structurée et garantie. | Format garanti par l'API = pas d'erreur de parsing. Plus fiable que ReAct artisanal. | Dépendant du provider (OpenAI, Anthropic…). Moins de contrôle sur le format de raisonnement. | 1 à N |
| 4 | **Router** | Un LLM "routeur" classifie la demande et la dispatche vers l'agent spécialisé le mieux adapté. | Chaque agent a un prompt court et ciblé = meilleure qualité. Facile à maintenir et étendre. | Coût d'un appel LLM supplémentaire pour le routage. Erreur de routage = mauvais agent. | 2 |
| 5 | **Reflection** | Le LLM génère un brouillon, le critique, puis l'améliore. On peut boucler plusieurs fois. | Qualité nettement supérieure au premier jet. Le LLM est souvent meilleur pour critiquer que pour produire. | Coûteux (2 appels par itération). Rendements décroissants après 2-3 itérations. | 1 + 2×N |
| 6 | **Orchestrator-Workers** | Un LLM "chef d'orchestre" décompose une tâche complexe en sous-tâches, les distribue à des workers spécialisés, puis synthétise les résultats. | Gère des tâches complexes multi-facettes. Les workers peuvent tourner en parallèle. | Complexité d'implémentation élevée. L'orchestrateur peut mal découper la tâche. | 2 + N |
| 7 | **Map-Reduce** | Découpe un gros input en morceaux, traite chaque morceau séparément (Map), puis fusionne les résultats (Reduce). | Contourne les limites de contexte. Parallélisable. Idéal pour les longs documents. | Perte de contexte global entre les morceaux. Le Reduce peut rater des liens inter-morceaux. | N + 1 |
| 8 | **Evaluator-Optimizer** | Comme Reflection, mais avec une évaluation quantitative (score). On boucle tant que le score n'atteint pas un seuil défini. | Critère d'arrêt objectif (score ≥ seuil). Optimisation mesurable et reproductible. | Concevoir un bon scoring est difficile. Risque de sur-optimisation sur le score plutôt que la qualité réelle. | 1 + 2×N |
| 9 | **Prompt Chaining** | Enchaîne plusieurs appels LLM en séquence, chaque étape transformant la sortie de la précédente (pipeline). | Chaque étape est simple et testable indépendamment. Facile à debugger. | Latence cumulative (chaque étape attend la précédente). Une erreur se propage dans tout le pipeline. | N étapes |

## 🔀 Quel pattern choisir ?

```
Ta tâche est simple ?
  └─ OUI → Chain of Thought (CoT)
  └─ NON ↓

Tu as besoin de données externes (web, BDD, API) ?
  └─ OUI → Function Calling (si API compatible) ou ReAct (sinon)
  └─ NON ↓

Tu as plusieurs types de demandes à gérer ?
  └─ OUI → Router Pattern
  └─ NON ↓

Ta tâche est décomposable en sous-tâches indépendantes ?
  └─ OUI → Orchestrator-Workers
  └─ NON ↓

Ton input est trop long pour le contexte du LLM ?
  └─ OUI → Map-Reduce
  └─ NON ↓

Tu veux maximiser la qualité d'un contenu généré ?
  └─ Avec critère mesurable → Evaluator-Optimizer
  └─ Sans critère mesurable → Reflection

Tu as une séquence de transformations à appliquer ?
  └─ OUI → Prompt Chaining
```

## 📁 Structure du repo

```
llm-architecture-patterns/
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
├── 01_chain_of_thought/
│   ├── README.md
│   ├── no_cot_baseline.py
│   ├── cot_zero_shot.py
│   ├── cot_few_shot.py
│   └── compare.py
├── 02_react/
│   ├── README.md
│   ├── tools.py
│   ├── react_agent.py
│   └── main.py
├── 03_function_calling/
│   ├── README.md
│   ├── tools.py
│   ├── agent.py
│   └── main.py
├── 04_router/
│   ├── README.md
│   ├── agents.py
│   ├── router.py
│   └── main.py
└── 05_reflection/
    ├── README.md
    ├── reflection_agent.py
    └── main.py
```

## 🚀 Démarrage rapide

```bash
# 1. Cloner le repo
git clone https://github.com/<ton-username>/llm-architecture-patterns.git
cd llm-architecture-patterns

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Configurer la clé API
cp .env.example .env
# Éditer .env avec votre clé API OpenAI

# 4. Lancer une démo
cd 01_chain_of_thought
python compare.py
```

## ⚠️ Notes

- Toutes les démos utilisent l'API OpenAI (`gpt-4o-mini`) — modèle rapide et économique.
- Le fichier `.env` est à la **racine** du repo. Chaque script le charge avec `python-dotenv`.
- Les outils dans `02_react` et `03_function_calling` sont **simulés** (pas de vraie recherche web) pour que les démos tournent sans clé API supplémentaire.

## 📚 Références

| Pattern | Paper / Source |
|---------|---------------|
| Chain of Thought | [Wei et al., 2022](https://arxiv.org/abs/2201.11903) |
| Zero-shot CoT | [Kojima et al., 2022](https://arxiv.org/abs/2205.11916) |
| ReAct | [Yao et al., 2022](https://arxiv.org/abs/2210.03629) |
| Function Calling | [OpenAI docs](https://platform.openai.com/docs/guides/function-calling) |
| Reflection | [Madaan et al., 2023](https://arxiv.org/abs/2303.17651) |
| Reflexion | [Shinn et al., 2023](https://arxiv.org/abs/2303.11366) |
| Building Agents | [Anthropic, 2024](https://www.anthropic.com/research/building-effective-agents) |

---

*Chaque dossier contient son propre README avec une explication détaillée du pattern, le code commenté et des exemples d'utilisation.*
