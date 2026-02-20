# 🪞 Pattern 5 — Reflection / Self-Critique

## C'est quoi ?

Le **Reflection Pattern** fait critiquer et améliorer sa propre sortie par le LLM. Au lieu d'accepter le premier jet, on boucle : générer → critiquer → améliorer.

## Le cycle

```
📝 GÉNÉRATION (brouillon)
    ↓
🔍 CRITIQUE ("le ton est trop familier, il manque des chiffres")
    ↓
✨ AMÉLIORATION (nouvelle version corrigée)
    ↓
(optionnel : reboucler)
```

## Pourquoi ça marche ?

Le LLM est souvent **meilleur pour critiquer** que pour produire du premier coup. En séparant les deux rôles (même modèle, prompts différents), chaque appel est plus ciblé.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `reflection_agent.py` | Les 3 rôles (générer, critiquer, améliorer) + la boucle |
| `main.py` | Exemples d'utilisation |

## Lancer

```bash
cd 05_reflection
python main.py
```

## Références

- [Self-Refine (Madaan et al., 2023)](https://arxiv.org/abs/2303.17651)
- [Reflexion (Shinn et al., 2023)](https://arxiv.org/abs/2303.11366)
