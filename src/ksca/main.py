"""Point d'entrée de la résolution SAT du problème KSCA."""

from ksca.data import get_constraint_positions
from ksca.model import N_VARIABLES, build_cnf, solve_cnf


def main() -> None:
    triplet_positions, pair_positions = get_constraint_positions()

    cnf = build_cnf(triplet_positions, pair_positions)

    print(f"Directions : {N_VARIABLES}")
    print(f"Triplets : {len(triplet_positions)}")
    print(f"Paires : {len(pair_positions)}")
    print(f"Clauses CNF : {len(cnf.clauses)}")

    assignment = solve_cnf(cnf)

    if assignment is None:
        print("UNSAT : aucune application ne satisfait les contraintes.")
        return

    print("SAT : une application satisfait les contraintes.")
    for index, value in assignment.items():
        print(f"x_{index} = {int(value)}")


if __name__ == "__main__":
    main()
