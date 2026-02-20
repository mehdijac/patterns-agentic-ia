# 🧠 Pattern 1 — Chain of Thought (CoT)

## C'est quoi ?

**Chain of Thought** consiste à demander au LLM de **raisonner étape par étape** avant de donner sa réponse finale. Chaque étape écrite devient du **contexte** qui aide le modèle à produire la suite — comme poser un calcul sur papier au lieu de le faire de tête.

## Les 2 variantes

| Variante | Principe | Quand l'utiliser |
|----------|----------|------------------|
| **Zero-shot CoT** | Ajouter "Raisonne étape par étape" dans le prompt | Rapide, bon pour la plupart des cas |
| **Few-shot CoT** | Fournir des exemples de raisonnement dans le prompt | Quand on veut un format précis ou un domaine spécifique |

## Fichiers

| Fichier | Rôle |
|---------|------|
| `no_cot_baseline.py` | Prompt naïf — réponse directe, pas de raisonnement |
| `cot_zero_shot.py` | On ajoute juste "raisonne étape par étape" |
| `cot_few_shot.py` | On donne 2 exemples de raisonnement avant la question |
| `compare.py` | Lance les 3 et affiche les résultats côte à côte |

## Lancer

```bash
# Depuis la racine du repo
cd 01_chain_of_thought
python compare.py
```

## Résultat attendu

Problème test : *"Un fermier a 17 moutons. Tous sauf 9 meurent. Combien reste-t-il ?"*

- **Sans CoT** → risque de répondre 8 (fait 17-9 machinalement)
- **Avec CoT** → raisonne et trouve 9 (comprend "tous sauf 9")

## Références

- [Chain-of-Thought Prompting (Wei et al., 2022)](https://arxiv.org/abs/2201.11903)
- [Large Language Models are Zero-Shot Reasoners (Kojima et al., 2022)](https://arxiv.org/abs/2205.11916)
