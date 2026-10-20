"""Unit tests for binary search algorithms."""
from algorithms.searching.binary_search import (
    binary_search,
    find_leftmost,
    find_rightmost,
)

def test_binary_search_found():
    arr = [1, 3, 5, 7, 9, 11]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 11) == 5

def test_binary_search_not_found():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 4) is None
    assert binary_search(arr, 0) is None
    assert binary_search(arr, 12) is None

def test_find_leftmost():
    arr = [1, 2, 4, 4, 4, 5, 8]
    assert find_leftmost(arr, 4) == 2
    assert find_leftmost(arr, 3) == 2

def test_find_rightmost():
    arr = [1, 2, 4, 4, 4, 5, 8]
    assert find_rightmost(arr, 4) == 5
    assert find_rightmost(arr, 3) == 2
    assert find_rightmost(arr, 0) == 0
    assert find_rightmost(arr, 8) == 7
    assert find_rightmost(arr, 9) == 7

def test_find_rightmost_counts_occurrences():
    arr = [1, 2, 4, 4, 4, 5, 8]
    assert find_rightmost(arr, 4) - find_leftmost(arr, 4) == 3
    assert find_rightmost(arr, 3) - find_leftmost(arr, 3) == 0

def test_empty_sequence():
    assert binary_search([], 1) is None
    assert find_leftmost([], 1) == 0
    assert find_rightmost([], 1) == 0


def test_all_identical_elements():
    arr = [3, 3, 3, 3]
    assert find_leftmost(arr, 3) == 0
    assert find_rightmost(arr, 3) == 4
    assert find_leftmost(arr, 2) == 0
    assert find_rightmost(arr, 2) == 0
    assert find_leftmost(arr, 4) == 4
    assert find_rightmost(arr, 4) == 4


def test_single_element():
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 2) is None
    assert find_leftmost(arr, 5) == 0
    assert find_rightmost(arr, 5) == 1
    assert find_leftmost(arr, 1) == 0
    assert find_rightmost(arr, 10) == 1

