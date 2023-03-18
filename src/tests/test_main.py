import pytest
from src.main import finds_pairs


def test_finds_pairs():
    assert finds_pairs([0, 1, 2, 3], 3) == {(0, 3), (1, 2)}


@pytest.mark.parametrize(
    "numbers_list, number_sum, expected_pairs",
    [
        ([0, 1, 2, 3], 3, {(0, 3), (1, 2)}),
        ([1, 9, 5, 0, 20, -4, 12, 16, 7], 12, {(0, 12), (5, 7), (-4, 16)})
    ]
)
def test_finds_pairs_params(numbers_list: list, number_sum: int, expected_pairs: set):
    assert finds_pairs(numbers_list, number_sum) == expected_pairs
