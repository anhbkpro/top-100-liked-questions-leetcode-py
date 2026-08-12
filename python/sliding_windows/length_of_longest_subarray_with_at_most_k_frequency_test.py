from typing import List

from .length_of_longest_subarray_with_at_most_k_frequency import Solution


def test_max_subarray_length_when_frequency_limit_is_two() -> None:
    input_nums: List[int] = [1, 2, 3, 1, 2, 3, 1, 2]
    input_k: int = 2
    expected_length: int = 6

    actual_length: int = Solution().maxSubarrayLength(input_nums, input_k)

    assert actual_length == expected_length


def test_max_subarray_length_when_frequency_limit_is_one() -> None:
    input_nums: List[int] = [1, 2, 1, 2, 1, 2, 1, 2]
    input_k: int = 1
    expected_length: int = 2

    actual_length: int = Solution().maxSubarrayLength(input_nums, input_k)

    assert actual_length == expected_length


def test_max_subarray_length_when_all_elements_are_the_same() -> None:
    input_nums: List[int] = [5, 5, 5, 5, 5, 5, 5]
    input_k: int = 4
    expected_length: int = 4

    actual_length: int = Solution().maxSubarrayLength(input_nums, input_k)

    assert actual_length == expected_length


def test_max_subarray_length_when_array_has_single_element() -> None:
    input_nums: List[int] = [1]
    input_k: int = 1
    expected_length: int = 1

    actual_length: int = Solution().maxSubarrayLength(input_nums, input_k)

    assert actual_length == expected_length


def test_max_subarray_length_when_all_duplicates_exceed_limit() -> None:
    input_nums: List[int] = [1, 1, 1, 1]
    input_k: int = 1
    expected_length: int = 1

    actual_length: int = Solution().maxSubarrayLength(input_nums, input_k)

    assert actual_length == expected_length
