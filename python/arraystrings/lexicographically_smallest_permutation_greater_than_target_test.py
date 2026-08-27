from .lexicographically_smallest_permutation_greater_than_target import Solution


def test_lex_greater_permutation_when_next_permutation_exists() -> None:
    input_s: str = "abc"
    input_target: str = "abb"
    expected_permutation: str = "abc"

    actual_permutation: str = Solution().lexGreaterPermutation(
        input_s, input_target
    )

    assert actual_permutation == expected_permutation


def test_lex_greater_permutation_when_no_greater_exists() -> None:
    input_s: str = "abc"
    input_target: str = "cba"
    expected_permutation: str = ""

    actual_permutation: str = Solution().lexGreaterPermutation(
        input_s, input_target
    )

    assert actual_permutation == expected_permutation


def test_lex_greater_permutation_when_must_increase_earlier_character() -> None:
    input_s: str = "aabb"
    input_target: str = "abba"
    expected_permutation: str = "baab"

    actual_permutation: str = Solution().lexGreaterPermutation(
        input_s, input_target
    )

    assert actual_permutation == expected_permutation


def test_lex_greater_permutation_when_single_character_matches() -> None:
    input_s: str = "a"
    input_target: str = "a"
    expected_permutation: str = ""

    actual_permutation: str = Solution().lexGreaterPermutation(
        input_s, input_target
    )

    assert actual_permutation == expected_permutation


def test_lex_greater_permutation_when_smallest_greater_is_sorted_s() -> None:
    input_s: str = "ab"
    input_target: str = "aa"
    expected_permutation: str = "ab"

    actual_permutation: str = Solution().lexGreaterPermutation(
        input_s, input_target
    )

    assert actual_permutation == expected_permutation


def test_lex_greater_permutation_when_s_is_anagram_of_target() -> None:
    input_s: str = "bac"
    input_target: str = "abc"
    expected_permutation: str = "acb"

    actual_permutation: str = Solution().lexGreaterPermutation(
        input_s, input_target
    )

    assert actual_permutation == expected_permutation
