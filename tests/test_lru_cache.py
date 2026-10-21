"""Unit tests for LRUCache."""
from structures.lru_cache import LRUCache

def test_lru_cache_basic():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)
    assert cache.get("b") is None  # Evicted
    assert cache.get("a") == 1
    assert cache.get("c") == 3

def test_lru_cache_update_existing():
    cache = LRUCache(2)
    cache.put("x", 10)
    cache.put("x", 20)
    assert cache.get("x") == 20

# Refined on 2026-10-21
