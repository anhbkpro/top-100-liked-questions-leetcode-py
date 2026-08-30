from typing import List

from .removing_minimum_and_maximum_from_array import Solution


def test_minimum_deletions_when_both_ends_are_used() -> None:
    input_nums: List[int] = [2, 10, 7, 5, 4, 1, 8, 6]
    expected_deletions: int = 5

    actual_deletions: int = Solution().minimumDeletions(input_nums)

    assert actual_deletions == expected_deletions


def test_minimum_deletions_when_removing_from_the_left_is_best() -> None:
    input_nums: List[int] = [0, -4, 19, 1, 8, -2, -3, 5]
    expected_deletions: int = 3

    actual_deletions: int = Solution().minimumDeletions(input_nums)

    assert actual_deletions == expected_deletions


def test_minimum_deletions_when_array_has_single_element() -> None:
    input_nums: List[int] = [101]
    expected_deletions: int = 1

    actual_deletions: int = Solution().minimumDeletions(input_nums)

    assert actual_deletions == expected_deletions


def test_minimum_deletions_when_array_has_two_elements() -> None:
    input_nums: List[int] = [1, 2]
    expected_deletions: int = 2

    actual_deletions: int = Solution().minimumDeletions(input_nums)

    assert actual_deletions == expected_deletions


def test_minimum_deletions_when_min_and_max_are_at_opposite_ends() -> None:
    input_nums: List[int] = [5, 4, 3, 2, 1]
    expected_deletions: int = 2

    actual_deletions: int = Solution().minimumDeletions(input_nums)

    assert actual_deletions == expected_deletions


def test_minimum_deletions_when_min_and_max_are_adjacent() -> None:
    input_nums: List[int] = [3, 1, 2]
    expected_deletions: int = 2

    actual_deletions: int = Solution().minimumDeletions(input_nums)

    assert actual_deletions == expected_deletions
