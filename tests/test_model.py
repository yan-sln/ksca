# tests/test_model.py

import pytest

from ksca.model import build_cnf, solve_cnf


def test_triplet_generates_four_clauses() -> None:
    cnf = build_cnf([(0, 1, 2)], [])

    assert len(cnf.clauses) == 4
    assert cnf.clauses == [
        [1, 2],
        [1, 3],
        [2, 3],
        [-1, -2, -3],
    ]


def test_pair_generates_one_clause() -> None:
    cnf = build_cnf([], [(0, 1)])

    assert cnf.clauses == [[1, 2]]


def test_triplet_solution_has_exactly_two_true_values() -> None:
    cnf = build_cnf([(0, 1, 2)], [])

    assignment = solve_cnf(cnf)

    assert assignment is not None
    assert sum(assignment[i] for i in range(3)) == 2


def test_invalid_index_is_rejected() -> None:
    with pytest.raises(ValueError):
        build_cnf([(0, 1, 33)], [])


def test_repeated_index_is_rejected() -> None:
    with pytest.raises(ValueError):
        build_cnf([(0, 0, 1)], [])