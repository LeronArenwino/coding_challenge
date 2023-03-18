import pytest
from src.main import finds_pairs


def test_finds_pairs():
    assert sorted(finds_pairs([0, 1, 2, 3], 3)) == [(0, 3), (1, 2)]


@pytest.mark.parametrize(
    "numbers_list, number_sum, expected_pairs",
    [
        ([0, 1, 2, 3], 3, [(0, 3), (1, 2)])
    ]
)
def test_finds_pairs_params(numbers_list: list, number_sum: int, expected_pairs: list):
    assert sorted(finds_pairs(numbers_list, number_sum)) == expected_pairs
