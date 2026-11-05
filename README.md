# KSCA — Modélisation SAT

Ce projet poursuit le travail réalisé dans le dépôt [Free-Will-Theorem](https://github.com/yan-sln/Free-Will-Theorem), et plus particulièrement dans le script [`ForceBrute.py`](https://github.com/yan-sln/Free-Will-Theorem/blob/main/ForceBrute.py).

L'objectif est d'étudier le lemme KSCA (*Kochen-Specker-Conway-Abramsky*) à partir des 33 directions de Peres, en reformulant le problème sous la forme d'un problème de satisfaisabilité propositionnelle (**SAT**).

## Démarche

Le script `ForceBrute.py` explore exhaustivement les différentes attributions de valeurs 0 ou 1 aux 33 directions de Peres, afin de vérifier s'il existe une coloration respectant les contraintes du lemme KSCA.

Nous poursuivons cette démarche en utilisant une approche logique :

1. **Reprendre les données géométriques** : les 33 directions de Peres, les 16 triplets orthogonaux et les 24 paires orthogonales supplémentaires.
2. **Traduire les contraintes en logique propositionnelle** : chaque direction est représentée par une variable booléenne.
3. **Construire une formule en forme normale conjonctive (CNF)** correspondant aux contraintes du problème.
4. **Résoudre la formule avec PySAT**, qui fournit une affectation satisfaisante ou indique qu'aucune solution n'existe.

Pour chaque triplet orthogonal, exactement deux directions doivent recevoir la valeur 1. Pour chaque paire orthogonale supplémentaire, au moins une des deux directions doit recevoir la valeur 1.

Cette modélisation permet de confier la recherche à un solveur SAT plutôt que d'énumérer explicitement toutes les affectations possibles.

## Technologies

- Python 3.12+
- [PySAT](https://pysathq.github.io/) : modélisation et résolution SAT
- [uv](https://docs.astral.sh/uv/) : gestion de l'environnement et des dépendances
- [pytest](https://docs.pytest.org/) : tests
- [Ruff](https://docs.astral.sh/ruff/) : linting et formatage

## Installation et exécution

Depuis la racine du projet :

```bash
uv venv
source .venv/bin/activate

uv pip install -e ".[dev]"

uv run ruff check .
uv run ruff format --check .
uv run pytest

uv run python -m ksca.main
```

## Organisation du projet

```text
.
├── pyproject.toml
├── README.md
├── src/
│   └── ksca/
│       ├── __init__.py
│       ├── data.py
│       ├── model.py
│       └── main.py
└── tests/
    ├── test_data.py
    └── test_model.py
```

- `data.py` contient les directions de Peres, les triplets et les paires, ainsi que leur conversion en indices.
- `model.py` construit la formule CNF et interroge le solveur SAT.
- `main.py` orchestre la conversion des données, la construction du modèle et la résolution.
- `tests/` regroupe les tests des données et de la modélisation.

## Résultat attendu

Le programme indique si la formule est :

- **SAT** : une affectation des 33 variables satisfait l'ensemble des contraintes.
- **UNSAT** : aucune affectation ne satisfait simultanément toutes les contraintes.

L'objectif est de retrouver, par une approche SAT, l'impossibilité d'une application respectant les contraintes du lemme KSCA.