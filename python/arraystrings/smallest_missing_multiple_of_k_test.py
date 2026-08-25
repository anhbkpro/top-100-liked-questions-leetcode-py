from typing import List

from .smallest_missing_multiple_of_k import Solution


def test_missing_multiple_when_k_is_absent() -> None:
    input_nums: List[int] = [8, 2, 3, 4, 6]
    input_k: int = 2
    expected_multiple: int = 10

    actual_multiple: int = Solution().missingMultiple(input_nums, input_k)

    assert actual_multiple == expected_multiple


def test_missing_multiple_when_first_multiple_is_missing() -> None:
    input_nums: List[int] = [1, 4, 7, 10, 15]
    input_k: int = 5
    expected_multiple: int = 5

    actual_multiple: int = Solution().missingMultiple(input_nums, input_k)

    assert actual_multiple == expected_multiple


def test_missing_multiple_when_consecutive_multiples_exist() -> None:
    input_nums: List[int] = [5, 10, 15, 20]
    input_k: int = 5
    expected_multiple: int = 25

    actual_multiple: int = Solution().missingMultiple(input_nums, input_k)

    assert actual_multiple == expected_multiple


def test_missing_multiple_when_nums_contains_only_k() -> None:
    input_nums: List[int] = [3]
    input_k: int = 3
    expected_multiple: int = 6

    actual_multiple: int = Solution().missingMultiple(input_nums, input_k)

    assert actual_multiple == expected_multiple


def test_missing_multiple_when_unrelated_values_are_present() -> None:
    input_nums: List[int] = [1, 2, 3, 4]
    input_k: int = 7
    expected_multiple: int = 7

    actual_multiple: int = Solution().missingMultiple(input_nums, input_k)

    assert actual_multiple == expected_multiple
