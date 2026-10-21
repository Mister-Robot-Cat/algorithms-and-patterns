"""Unit tests for 3-way quicksort algorithm."""
import random
from algorithms.sorting.quick_sort import quick_sort


def test_quick_sort_empty_and_single():
    assert quick_sort([]) == []
    assert quick_sort([42]) == [42]


def test_quick_sort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]


def test_quick_sort_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]


def test_quick_sort_all_duplicates():
    arr = [7, 7, 7, 7, 7]
    assert quick_sort(arr) == [7, 7, 7, 7, 7]


def test_quick_sort_many_duplicates():
    arr = [3, 1, 2, 3, 1, 3, 2, 1]
    assert quick_sort(arr) == [1, 1, 1, 2, 2, 3, 3, 3]


def test_quick_sort_negatives():
    arr = [-5, 3, -1, 0, 2, -10]
    assert quick_sort(arr) == [-10, -5, -1, 0, 2, 3]


def test_quick_sort_strings():
    arr = ["banana", "apple", "cherry", "date"]
    assert quick_sort(arr) == ["apple", "banana", "cherry", "date"]


def test_quick_sort_in_place():
    arr = [3, 1, 2]
    result = quick_sort(arr)
    assert result is arr
    assert result == [1, 2, 3]


def test_quick_sort_random_list():
    random.seed(42)
    arr = [random.randint(-1000, 1000) for _ in range(150)]
    expected = sorted(arr)
    assert quick_sort(arr) == expected
