# src/ksca/model.py

from collections.abc import Sequence

from pysat.formula import CNF
from pysat.solvers import Solver

N_VARIABLES = 33

type Triplet = tuple[int, int, int]
type Pair = tuple[int, int]
type Assignment = dict[int, bool]


def _validate_indices(indices: tuple[int, ...]) -> None:
    """Vérifie que les indices désignent des variables distinctes valides."""
    if len(set(indices)) != len(indices):
        raise ValueError(f"Indices répétés : {indices}")

    if any(not 0 <= index < N_VARIABLES for index in indices):
        raise ValueError(f"Indice hors limites : {indices}")


def build_cnf(
    triplets: Sequence[Triplet],
    pairs: Sequence[Pair],
) -> CNF:
    """Construit la CNF représentant les contraintes KSCA."""
    cnf = CNF()

    for i, j, k in triplets:
        _validate_indices((i, j, k))

        x_i, x_j, x_k = i + 1, j + 1, k + 1

        # Exactement deux variables vraies.
        cnf.append([x_i, x_j])
        cnf.append([x_i, x_k])
        cnf.append([x_j, x_k])
        cnf.append([-x_i, -x_j, -x_k])

    for i, j in pairs:
        _validate_indices((i, j))

        # Au moins une variable vraie.
        cnf.append([i + 1, j + 1])

    return cnf


def solve_cnf(cnf: CNF) -> Assignment | None:
    """Renvoie une affectation satisfaisante, ou None si la CNF est UNSAT."""
    with Solver(name="g4", bootstrap_with=cnf.clauses) as solver:
        if not solver.solve():
            return None

        model = solver.get_model()

    if model is None:
        raise RuntimeError("Le solveur n'a pas retourné de modèle.")

    true_literals = set(model)

    return {
        index: index + 1 in true_literals
        for index in range(N_VARIABLES)
    }