"""Unit tests for Prefix Tree (Trie)."""
from structures.trie import Trie


def test_trie_insert_and_search():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.search("appl") is False
    assert trie.search("apples") is False
    assert trie.search("banana") is False


def test_trie_contains():
    trie = Trie()
    trie.insert("algorithm")
    assert "algorithm" in trie
    assert "algo" not in trie
    assert "data" not in trie


def test_trie_len():
    trie = Trie()
    assert len(trie) == 0
    trie.insert("cat")
    assert len(trie) == 1
    trie.insert("car")
    assert len(trie) == 2
    # Duplicate insertion should not increase size
    trie.insert("cat")
    assert len(trie) == 2


def test_trie_starts_with():
    trie = Trie()
    trie.insert("apple")
    assert trie.starts_with("app") is True
    assert trie.starts_with("apple") is True
    assert trie.starts_with("apples") is False
    assert trie.starts_with("b") is False


def test_trie_autocomplete():
    trie = Trie()
    words = ["flow", "flower", "flight", "flat", "fleet"]
    for w in words:
        trie.insert(w)

    assert sorted(trie.autocomplete("fl")) == sorted(words)
    assert sorted(trie.autocomplete("flo")) == ["flow", "flower"]
    assert trie.autocomplete("flight") == ["flight"]
    assert trie.autocomplete("xyz") == []


def test_trie_empty_string():
    trie = Trie()
    assert trie.search("") is False
    assert "" not in trie
    trie.insert("")
    assert trie.search("") is True
    assert "" in trie
    assert len(trie) == 1
    assert trie.starts_with("") is True
