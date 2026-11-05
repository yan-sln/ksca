"""Tests des données géométriques et de leur conversion."""

import pytest

from ksca.data import (
    directions_peres,
    list_to_positions,
    pairs,
    triplets,
)


def test_number_of_directions_and_constraints() -> None:
    assert len(directions_peres) == 33
    assert len(triplets) == 16
    assert len(pairs) == 24


def test_triplets_and_pairs_are_converted() -> None:
    triplet_positions = list_to_positions(triplets, directions_peres)
    pair_positions = list_to_positions(pairs, directions_peres)

    assert len(triplet_positions) == 16
    assert all(len(group) == 3 for group in triplet_positions)
    assert len(pair_positions) == 24
    assert all(len(group) == 2 for group in pair_positions)


def test_float_precision_is_normalized() -> None:
    reference = [(1.0, 0.7071067811865475, 0.0)]
    groups = [[(1.0, 0.7071067811865476, 0.0)]]

    assert list_to_positions(groups, reference) == [[0]]


def test_unknown_direction_raises_value_error() -> None:
    reference = [(1.0, 0.0, 0.0)]
    groups = [[(0.0, 1.0, 0.0)]]

    with pytest.raises(ValueError, match="absente"):
        list_to_positions(groups, reference)


def test_duplicate_reference_direction_raises_value_error() -> None:
    reference = [
        (1.0, 0.7071067811865475, 0.0),
        (1.0, 0.7071067811865476, 0.0),
    ]

    with pytest.raises(ValueError, match="identiques"):
        list_to_positions([], reference)


def test_invalid_vector_dimension_raises_value_error() -> None:
    with pytest.raises(ValueError, match="3 coordonnées"):
        list_to_positions([[(1.0, 0.0)]], [(1.0, 0.0, 0.0)])
