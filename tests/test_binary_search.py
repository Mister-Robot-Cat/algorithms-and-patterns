"""Unit tests for binary search algorithms."""
from algorithms.searching.binary_search import binary_search, find_leftmost

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

def test_duplicates():
    arr = [2, 2, 2, 2]
    assert find_leftmost(arr, 2) == 0
    assert find_leftmost(arr, 3) == 4
